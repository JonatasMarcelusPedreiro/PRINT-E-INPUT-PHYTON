#Em Python, fazemos isso utilizando a função input(), que é literalmente ‘entrada’ em inglês.

#A função input() recebe como parâmetro uma string que será mostrada como auxílio ao usuário, 
#geralmente o informando que tipo de dado o programa está aguardando receber.



nome = input("Escreva seu nome: ")

print('Seu nome é:', nome)


#A função print() também funciona para gravar dados em arquivos.
#Para isso, utilizamos o parâmetro file= da função print.
#Também precisamos de um arquivo aberto, o que é feito utilizando-se a função open.
#Veja o exemplo abaixo:


with open('arquivo.txt', 'w') as arquivo:
    print("Escreva isso dentro do arquivo,", file=arquivo)
    print("Escreva outra linha dentro do arquivo.", file=arquivo)
    
#Se abrirmos o arquivo.txt, veremos o seguinte conteúdo:

#Escreva isso dentro do arquivo,
#Escreva outra linha dentro do arquivo.
