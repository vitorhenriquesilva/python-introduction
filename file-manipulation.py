#Criacao e edicao de arquivos
#Para manipulacao de arquivos utilizamos a funcao open
#Ex: open (nome, modo)
#Modos:
#r - Somente leitura
#w - Escrita (caso o arquivo ja exista, ele sera apagado e um novo arquivo vazio sera criado
#a - leitura e escrita (adiciona o novo conteudo ao fim do arquivo
#r+ - Lietura e escrita
#w+ - Escrita (o modo w+, assim como o w, tambem apaga o conteudo anterior do arquivo)
#a+ - leitura e escrita (abre o arquivo para atualizacao)

arquivo = open("arquivo.txt")

#1.0 - Imprimindo em lista
#linhas = arquivo.readlines()
#print(linhas)

#1.1 - Imprimindo o arquivo
#print(arquivo.read())

#1.2 - Imprimindo linha por linha
#linhas = arquivo.readlines()
#for linha in linhas:
#   print(linha)

#Criando um arquivo
w = open ("Arquivo2.txt", "w")
w.write("Esse � um arquivo modificado pelo python\n")
#E sempre bom fechar o arquivo apos sua criacao
w.close()