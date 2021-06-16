#Dicion�rios
#Criando o dicion�rio
#Um dicion�rio � uma lista de associa��es compostas por chave e valor
#Para a cria��o do dicion�rio utiliza-se as chaves
#J� para buscar algum valor espec�fico, uitliza-se colchetes com a palavra chave
#Essa palavra chave � case-sensitive
dicionario_sites = {"Diego": "diegomariano.com", "Google": "google.com", "Udemy": "udemy.com"}
#Imprimindo o dicion�rio utilizando as palavras chaves
for chave in dicionario_sites:
    print(chave + ": " + dicionario_sites[chave])

#Retornando chaves e valores com ".items()"
#tupla - conjunto de dados imut�veis, que � o resultado da sa�da abaixo
for i in dicionario_sites.items():
    print(i)

#Tamb�m � poss�vel retornar apenas os valores com o ".values"
for i in dicionario_sites.values():
    print(i)
#Por fim, retornamos as chaves com o ".keys"
for i in dicionario_sites.keys():
    print(i)