# numero = 200
# hora = 10
# valor = 400
# salario = hora * valor
# print("Seu salário é: ", + salario)
# print("Seu número é: ", + numero)



#aula 2

#esse codigo lê codigos

# print("") #serve para mostra coisas para outros usuarios

# #criando uma variavel para valvar texto

# string1 = "bom dia, hoje está frio"

# print(string1) #forma de mostrar o texto salvo  na variavel

# # \n serve para pular linha
# # \t serve para dar TAB (espaço) dentro do texto

# print("*\n**\n***\n****\n*****\n******")

# #Len serve para lê as quantidades de caracteres

# print(len(string1)) #print para mostrar as quantidades de caracteres

# #Fazendo uma verificação e mostrando para o usuário se foi ou não foi cadastrado.

# while True:

#     texto = input("Digite o seu nome: ")  #salvar o texto da pessoa na variavel, INPUT usado para coletar dados que você escreve

#     cara = len(texto)  #Len vai a quantidade de caracteres no TEXTO e salvar na variavel
    
#     if cara > 10: #if & else é usado para verificar
#         print("Nome muito grande! Limite de 10 caracteres")
    
#     else: #segunda condição
#         print("Cadastro realizado!")
#         break #comando para encerrar o laço de repetição, BREAK é usado para parar o laço.
    

#Indexação

# nome = 'Amanda Ayumi I. Magalhães'

# print(nome[6]) #mostra a posição de uma letra dentro da variavel, sempre usa [posição];
#print(nome[6:]) #mostra tudo depois da eguinte posição;
# print(nome[:6]) #mostra tudo antes da posição de uma letra na variavel;
# print(nome[0:16]) #mostra uma parte do texto que você escolhe;
# print(nome[-1]) #mostra a última posição do texto;
# print(nome[:-1]) #mostra tudo antes da última da posição;
# print(nome[::2]) #pula um número da posição e seleciona outra letra e pula dnv;

#Função Find

# nome = 'amanda.ayumi@gmail.com'

# print(nome.find('@'))

#Função Count

# print(nome.count('.'))

# nome = 'Amanda '
# sobrenome = 'Ayumi'
# print(nome + sobrenome)

#Função STR() transforma número em letra

# idade = 15

# print("Minha idade é " + str(idade) + " anos")
# print(f" Minha idade é {idade} anos") #forma mais fácil de usar variável no meio do texto;

# nome = 'ctrlplay - escola de Tecnologia e Inovação'
# divido = nome.split()
# print(nome.upper()) #deixa tudo letra grande;
# print(nome.lower()) #deixa tudo letra pequena;
# print(nome.split()) #divide tudo em grupos;
# print(divido[2]) #mostra uma parte dos textos que foram separados por SPLIT;

#Entrada de Dados INPUT()

# nome = input("Digite o seu nome: ") #para texto;
# idade = int(input("Digite a sua idade: ")) #para número;
# altura = float(input("Digite a sua altura: ")) #para números quebrados;

# print(f"O nome da cliente é {nome} e ela tem {idade} anos e {altura:.2f} de altura")