import pandas as pd

# Carregando a planilha
planilha = pd.read_excel("matriculas.xlsx")

# Escolhendo a coluna desejada
coluna_desejada = planilha["matricula"]

# Iterando sobre as linhas e salvando em um arquivo de texto
with open("extraido.txt", "w") as arquivo_txt:
    for valor_linha in coluna_desejada:
        linha_formatada = str(valor_linha) + "\n"
        arquivo_txt.write(linha_formatada)

print("Extração concluída e salva em extraido.txt")
