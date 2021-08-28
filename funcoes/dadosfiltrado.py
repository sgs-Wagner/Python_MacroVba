import pandas as pd
import xlwings as xw

def dadosfiltrado(dados_df):
    
    lista_colunas = ['nome', 'cargo']
    filtro_df = dados_df[lista_colunas]
    
    # criando workbook e instanciando a sheet
    wb = xw.Book(r'C:\Users\Souza\Desktop\puto\macro.xlsm')
    layout = wb.sheets["Layout"]
    
    #5 funcao 2 = printar filtro_df
    layout["M3"].options(pd.DataFrame, header=1, index=True, expand='table').value = filtro_df


if __name__ == '__main__':
    dadosfiltrado(dados_df)















