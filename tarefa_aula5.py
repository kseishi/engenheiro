import pandas as pd

# Ler o arquivo CSV
file_path = "C:\\Users\\mobilemed\\Documents\\engenharia_dados\\awari-engenharia-de-dados-docker\\exercicios\\topyoutube.csv"
df = pd.read_csv(file_path)

# Substituir valores ausentes por 0 na coluna "Total Views"
df["Total Views"].fillna(0, inplace=True)

# Remover vírgulas e converter a coluna "Total Views" para float
df["Total Views"] = df["Total Views"].str.replace(",", "").astype(float)

# Multiplicar a coluna "Total Views" por 100 milhões
df["Total Views"] *= 100000000


# Mostrar as 10 primeiras linhas
print("As 10 primeiras linhas:")
print(df.head(10))

# Mostrar os top 10 usuários por número de inscritos
top_10_users = df.sort_values(by="Total Views", ascending=False).head(10)
print("\nTop 10 usuários:")
print(top_10_users)

# Salvar o DataFrame modificado em um novo arquivo CSV
new_csv_path = "topyoutube_modified.csv"
df.to_csv(new_csv_path, index=False)
print(f"\nDados salvos em {new_csv_path}")