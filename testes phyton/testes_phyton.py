#Em Python, fazemos isso utilizando a fun��o input(), que � literalmente �entrada� em ingl�s.

#A fun��o input() recebe como par�metro uma string que ser� mostrada como aux�lio ao usu�rio, 
#geralmente o informando que tipo de dado o programa est� aguardando receber.



nome = input("Escreva seu nome: ")

print('Seu nome �:', nome)


#A fun��o print() tamb�m funciona para gravar dados em arquivos.
#Para isso, utilizamos o par�metro file= da fun��o print.
#Tamb�m precisamos de um arquivo aberto, o que � feito utilizando-se a fun��o open.
#Veja o exemplo abaixo:


with open('arquivo.txt', 'w') as arquivo:
    print("Escreva isso dentro do arquivo,", file=arquivo)
    print("Escreva outra linha dentro do arquivo.", file=arquivo)
    
#Se abrirmos o arquivo.txt, veremos o seguinte conte�do:

#Escreva isso dentro do arquivo,
#Escreva outra linha dentro do arquivo.
