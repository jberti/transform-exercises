import pandas as pd
import numpy as np

def main():
    #load file from previous script
    result2 = pd.read_csv('result1.csv')

    #delete an unecessary column
    result2.drop(columns=['registro_sistema'], inplace=True)

    #transform a column to string
    result2['matricula_ou_siape'] = result2['matricula_ou_siape'].astype(str)
    
    #create new column
    result2.insert(13,'CDU',None,True)

    #insert values based on a set of rules
    result2.loc[(result2['localizacao'] < 99),'CDU'] = 'Generalidades. Ciência e conhecimento'
    result2.loc[(result2['localizacao'] > 100) & (result2['localizacao'] < 199),'CDU'] = 'Filosofia e psicologia'
    result2.loc[(result2['localizacao'] > 200) & (result2['localizacao'] > 299),'CDU'] = 'Religião'
    result2.loc[(result2['localizacao'] > 300) & (result2['localizacao'] > 399),'CDU'] = 'Ciências sociais'
    result2.loc[(result2['localizacao'] > 400) & (result2['localizacao'] > 499),'CDU'] = 'Classe vaga. Provisoriamente não ocupada'
    result2.loc[(result2['localizacao'] > 500) & (result2['localizacao'] > 599),'CDU'] = 'Matemática e ciências naturais'
    result2.loc[(result2['localizacao'] > 600) & (result2['localizacao'] > 699),'CDU'] = 'Ciências aplicadas'
    result2.loc[(result2['localizacao'] > 700) & (result2['localizacao'] > 799),'CDU'] = 'Belas artes'
    result2.loc[(result2['localizacao'] > 800) & (result2['localizacao'] > 899),'CDU'] = 'Linguagem. Língua. Linguística'
    result2.loc[(result2['localizacao'] > 900) & (result2['localizacao'] > 999),'CDU'] = 'Geografia. Biografia. História'

    #save to file
    result2.to_csv('result2.csv')

if __name__ == "__main__":
    main()