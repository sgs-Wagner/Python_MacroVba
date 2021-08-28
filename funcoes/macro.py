import pandas as pd
# minhas funcoes:
import dadosfiltrado as ft
import todosdados as td

def main():

    td.todosdados(dados_df)
    ft.dadosfiltrado(dados_df)
    input("########## nilson boiola")


if __name__ == '__main__':
    dados_df = pd.read_excel(r"C:\Users\Souza\Desktop\puto\basedados\dados.xlsx")
    main()