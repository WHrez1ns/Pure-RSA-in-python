# Algoritmo de RSA PURO em python
 Um script python tentando replicar o comportamento da criptografia de chave pública RSA

# Depurando o código
 O algoritmo implementado utiliza o RSA para criptografar e descriptografar uma mensagem, seguindo os passos definidos na descrição do problema.

 O código começa importando as bibliotecas necessárias: *random*, *sympy* e *gcd* do módulo *math*.

 O passo 1 é implementado em um *loop while* que gera dois números primos aleatórios. Isso é feito utilizando a função *randint()* da biblioteca *random*, que gera um número aleatório entre os limites definidos. Para verificar se o número é primo, é utilizada a função *isprime()* da biblioteca *sympy*.

 Em seguida, o código define a função *gerar_chaves()*, que *implementa os passos 2, 3, 4 e 5 do algoritmo*. Essa função recebe como parâmetros os números primos *p* e *q* e retorna as chaves *pública* e *privada*.

 Dentro da função, primeiro é calculado *N (pq)* e *Z ((p-1)(q-1))*. Em seguida, um número aleatório e coprimo com *Z* é escolhido utilizando a função *randrange()* da biblioteca *random* e um *loop while* que verifica *se o maior divisor comum entre E e Z é igual a 1*.

 Depois, é calculado o *inverso multiplicativo de E em relação a Z* utilizando a função *inverso_modular()*, que implementa o *algoritmo de Euclides estendido*.

 Por fim, as chaves *pública* e *privada* são retornadas em uma *tupla*.

 A função *criptografar()* recebe uma mensagem e a *chave pública* e retorna a mensagem *criptografada*. Para isso, ela *converte cada caractere da mensagem* para o seu *código ASCII*, *eleva esse valor à potência E* e faz o *módulo N*. O resultado é *armazenado* em uma *lista* e essa *lista* é retornada.

 A função *descriptografar()* recebe a mensagem *criptografada* e a *chave privada* e retorna a *mensagem original*. Para isso, ela *eleva cada valor da lista criptograma à potência D* e faz o *módulo N*. Em seguida, *converte o resultado para o caractere correspondente* no *código ASCII* e *junta* todos os *caracteres* em uma *única string*.

 A função *inverso_modular()* *verifica* se *A* e *M* *são coprimos*, ou seja, *se o maior divisor comum entre eles é 1*. Se isso *não for verdadeiro*, a função retorna *None*. Caso contrário, ela utiliza o *algoritmo de Euclides estendido* para *encontrar* o *inverso multiplicativo de A em relação a M*. O resultado é retornado fazendo o *módulo M*.

 O *algoritmo de Euclides estendido* é implementado na função *euclides_estendido()*. Essa função *recebe dois números* *A* e *B* e *retorna* o *maior divisor comum entre eles* e os valores *X* e *Y* que *satisfazem* a equação *AX + BY = gcd(A,B)*. O algoritmo é *implementado* de *forma recursiva*.

 # Por fim 
 O código *chama as funções necessárias para gerar as chaves*, *criptografar* e *descriptografar* a *mensagem* e *imprimir* os *resultados* na tela. A *mensagem original*, a *mensagem criptografada* e a *mensagem decifrada* são impressas na tela para *verificação*.

# Considerações finais
 Nunca trabalhei em algo tão insano quanto isso - por mim :D