import pandas as pd
import xlwings as xw

def todosdados(dados_df):
    # criando workbook e instanciando a sheet
    wb = xw.Book(r'C:\Users\Souza\Desktop\puto\macro.xlsm')
    layout = wb.sheets["Layout"]


    # df tds dados
    #dados_df = pd.read_excel(r"C:\Users\Souza\Desktop\puto\basedados\dados.xlsx")
    # passando o valor desejado

    layout["F3"].options(pd.DataFrame, header=1, index=True, expand='table').value = dados_df


if __name__ == '__main__':
    todosfiltrado(dados_df)















