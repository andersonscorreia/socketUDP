import os
from datetime import datetime
from tkinter.messagebox import YES
'''
def caminho(pasta):
    caminho = os.path.dirname(os.path.abspath(__file__))
    caminho += '\\'+pasta
    return(caminho)
    

a= ['a','b']
c = ''
for i in a:
    c = c+i 

#print(c)
d = 'abcdef'
c = d.upper()

if 'A' in d.upper():
    print('aaa')
else:
    print('bbb')




def listFiles():
    arquivos = os.listdir(caminho('server_files'))
    return(arquivos)

def listTamanho(NomeArquivos):
    for i in NomeArquivos:
        print(i)

listTamanho(listFiles)
'''

print(datetime.today().strftime('%Y-%m-%d %H:%M'))