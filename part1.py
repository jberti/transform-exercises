import pandas as pd

#Load data from csv files
def main():
    dados_2010_1 = pd.read_csv('assets/emprestimos-20101.csv')
    dados_2010_2 = pd.read_csv('assets/emprestimos-20102.csv')
    dados_2011_1 = pd.read_csv('assets/emprestimos-20111.csv')
    dados_2011_2 = pd.read_csv('assets/emprestimos-20112.csv')
    dados_2012_1 = pd.read_csv('assets/emprestimos-20121.csv')
    dados_2012_2 = pd.read_csv('assets/emprestimos-20122.csv')
    dados_2013_1 = pd.read_csv('assets/emprestimos-20131.csv')
    dados_2013_2 = pd.read_csv('assets/emprestimos-20132.csv')
    dados_2014_1 = pd.read_csv('assets/emprestimos-20141.csv')
    dados_2014_2 = pd.read_csv('assets/emprestimos-20142.csv')
    dados_2015_1 = pd.read_csv('assets/emprestimos-20151.csv')
    dados_2015_2 = pd.read_csv('assets/emprestimos-20152.csv')
    dados_2016_1 = pd.read_csv('assets/emprestimos-20161.csv')
    dados_2016_2 = pd.read_csv('assets/emprestimos-20162.csv')
    dados_2017_1 = pd.read_csv('assets/emprestimos-20171.csv')
    dados_2017_2 = pd.read_csv('assets/emprestimos-20172.csv')
    dados_2018_1 = pd.read_csv('assets/emprestimos-20181.csv')
    dados_2018_2 = pd.read_csv('assets/emprestimos-20182.csv')
    dados_2019_1 = pd.read_csv('assets/emprestimos-20191.csv')
    dados_2019_2 = pd.read_csv('assets/emprestimos-20192.csv')
    dados_2020_1 = pd.read_csv('assets/emprestimos-20201.csv')

    #Merge all in one dataframe
    books_loan = pd.concat([dados_2010_1,dados_2010_2,dados_2011_1,dados_2011_2,dados_2012_1,dados_2012_2,dados_2013_1,dados_2013_2,dados_2014_1,
                                    dados_2014_2,dados_2015_1,dados_2015_2,dados_2016_1,dados_2016_2,dados_2017_1,dados_2017_2,dados_2018_1,dados_2018_2,
                                    dados_2019_1,dados_2019_2,dados_2020_1],ignore_index=True)
    
    books_loan = books_loan.drop_duplicates()

    more_data = pd.read_parquet('assets/more_data.parquet')

    #merge with more data
    books_loan = books_loan.merge(more_data)

    books_loan.to_csv('result1.csv')

if __name__ == "__main__":
    main()