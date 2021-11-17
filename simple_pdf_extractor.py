from genericpath import exists, isfile
import camelot as cm
import pandas as pd
import os
import seaborn as sb
import matplotlib.pyplot as plt

input_pdf = cm.read_pdf("india_factsheet_economic_n_hdi.pdf", flavor="lattice", pages=" 1,2")

# for n in input_pdf:
#     print(n)

input_pdf[2].df

df = input_pdf[2].df.loc[11:14, 1:3].reset_index(drop=True)
df.columns = ["KPI", "2001", "2011"]

#Tratar os dados da coluna "2001" e "2011" como tipo float
df.loc[:,["2001","2011"]] = df.loc[:,["2001","2011"]].astype("float")

df.to_csv("table_from_pdf.csv")
df.to_excel("table_from_pdf.xlsx")

msg = "Arquivo encontrado" if(os.path.exists("table_from_pdf.csv")) else "Arquivo não encontrado"
print(msg)

filepath = os.getcwd()
filepath = filepath + "/table_from_pdf.csv"
#checking file type
try:
    msg = "Path do arquivo válido" if isfile(filepath) else "Path do arquivo inválido"
    print(msg)
except:
    print(f'Erro durante operação de validação . {Exception}')

try:
    with open(filepath) as file_path:
        df2 = pd.read_csv(file_path)
        print(df2)

except IOError:
    print(f'Erro durante operação do arquivo \'.csv\' ')

df_melted = df.melt("KPI", var_name="YEAR", value_name="PERCENTAGE")
sb.barplot(x = "KPI", y= "PERCENTAGE", hue= "YEAR", data= df_melted)
plt.show()