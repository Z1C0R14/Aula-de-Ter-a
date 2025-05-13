import pandas as pd

# Criando um DataFrame:
Dados = {
    "Nome": ["Alex", "Reinaldo", "Isac", "Diego"],
    "Idade": [20, 19, 19, 20],
    "Cidade": ["SP", "Cornolandia", "Bollywood", "Cruzeiro"]
}

df = pd.DataFrame(Dados)

#Selecionando uma coluna:
Idades = df["Idade"]

#Filtrando linhas:
InteriorDeSaoPaulo = df[df["Cidade"] == "Cruzeiro"]

#Adicionando uma nova coluna:
df["Nome e Cidade"] = df["Nome"] + " " + df["Cidade"]

#Exibindo o DataFrame:
print(df)
print(Idades)
print(InteriorDeSaoPaulo)
