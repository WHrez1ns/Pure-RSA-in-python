##########################################################################################
# Construa  o  algoritmo com  a  linguagem  de  programação  de  sua  preferência,  ele  #
# deve escolher dois valores aleatórios para p e q, gerar chaves pública e privada de    #
# acordo com os quatropassos apresentados. O algoritmo deve ser capaz de criptografar e  #
# decriptografar a frase “The information security is of significant importanceto ensure #
# the privacy of communications”.                                                        #
##########################################################################################

# Passo 1 - Escolher de forma aleatória dois números primos grandes (p q)
# Passo 2 - Calcular N => N = p.q
# Passo 3 - Encontre o valor Z => m.m.c de p-1*q-1
# Passo 4 - Encontrar o valor de E => E > 1 < Z
# Passo 5 - Definir D => inverso multiplicativo de E
# Chaves Públicas: N e E
# Chaves Privadas: P, Q e D
# Encriptar => (textoplano^E) % N
# Decriptar => (textoplano^D) % N

import random  # importando a biblioteca Random para gerar números aleatórios
import sympy  # importando a biblioteca Sympy para trabalhar com matemática simbólica
# importando o gcd do math (Greatest Common Divisor) para realizar o cálculo de maior divisor comum
from math import gcd

# Passo 1

# Essa é a função que gera as chaves pública e privada. Ela recebe dois números primos p e q, calcula n como o produto de p e q e z como o produto de p-1 e q-1.


def gerar_chaves(p, q):
    n = p * q
    z = (p - 1) * (q - 1)

    # Escolher um número aleatório e coprime com Z
    e = random.randrange(1, z)
    while gcd(e, z) != 1:
        e = random.randrange(1, z)

    # Calcular o inverso multiplicativo de E em relação a Z
    d = inverso_modular(e, z)

    # Retornar as chaves pública e privada
    return ((n, e), (n, d))


# Função Criptografar


def criptografar(mensagem, chave_publica):
    n, e = chave_publica
    criptograma = [(ord(char) ** e) % n for char in mensagem]
    return criptograma


# Função Decriptografar


def descriptografar(criptograma, chave_privada):
    n, d = chave_privada
    mensagem = [chr((char ** d) % n) for char in criptograma]
    return ''.join(mensagem)


# Calculo do inverso modular


def inverso_modular(a, m):
    # Verificar se a e m são coprimos
    if gcd(a, m) != 1:
        return None

    # Encontrar o inverso multiplicativo de A em relação a M utilizando o algoritmo de Euclides estendido
    _, x, _ = euclides_estendido(a, m)
    return x % m


# Algoritmo de euclides estendido


def euclides_estendido(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = euclides_estendido(b % a, a)
        return gcd, y - (b // a) * x, x


lista_primos = []

print("Gerando N primos...")
while len(lista_primos) < 2:
    primo = 0
    while not sympy.isprime(primo):
        # obs: o correto seria elevado a 6 e 7 para gerarem numeros maiores, mas o meu processador é bem do ruim então para rodar eu diminui :D
        primo = random.randint(10**6, 10**7)
    lista_primos.append(primo)

print("Calculando...")
p = lista_primos[0]
q = lista_primos[1]
mensagem = 'The information security is of significant importanceto ensure the privacy of communications'
chave_publica, chave_privada = gerar_chaves(p, q)
print("Gerando...")
criptograma = criptografar(mensagem, chave_publica)
print("Criptografia...")
mensagem_decifrada = descriptografar(criptograma, chave_privada)
print("Decriptografia...")

print("---------------------------------------------------------------------------------------------------------")
print("Mensagem original:", mensagem)
print("---------------------------------------------------------------------------------------------------------")
print("Mensagem criptografada:", criptograma)
print("---------------------------------------------------------------------------------------------------------")
print("Mensagem decifrada:", mensagem_decifrada)
print("---------------------------------------------------------------------------------------------------------")
