#Dicionários
#Criando o dicionário
#Um dicionário é uma lista de associações compostas por chave e valor
#Para a criação do dicionário utiliza-se as chaves
#Já para buscar algum valor específico, uitliza-se colchetes com a palavra chave
#Essa palavra chave é case-sensitive
dicionario_sites = {"Diego": "diegomariano.com", "Google": "google.com", "Udemy": "udemy.com"}
#Imprimindo o dicionário utilizando as palavras chaves
for chave in dicionario_sites:
    print(chave + ": " + dicionario_sites[chave])

#Retornando chaves e valores com ".items()"
#tupla - conjunto de dados imutáveis, que é o resultado da saída abaixo
for i in dicionario_sites.items():
    print(i)

#Também é possível retornar apenas os valores com o ".values"
for i in dicionario_sites.values():
    print(i)
#Por fim, retornamos as chaves com o ".keys"
for i in dicionario_sites.keys():
    print(i)