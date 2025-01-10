# janela para selecionar a pasta do nosso computador
import os
import shutil # copia pastas, arquivos etc 
import datetime

from tkinter.filedialog import askdirectory 
nome_da_pasta_selecionada = askdirectory()

#print(nome_da_pasta_selecionada)

lista_arquivos = os.listdir(nome_da_pasta_selecionada)
#print(lista_arquivos)

# fazer o backup dos arquivos que estão nessa pasta
nome_pasta_backup = "backup"  #cria a pasta backup
nome_completo_pasta_backup = f"{nome_da_pasta_selecionada}/{nome_pasta_backup}" 
if not os.path.exists(nome_completo_pasta_backup):#
    os.mkdir(nome_completo_pasta_backup) # cria a pasta backup

data_atual = datetime.datetime.today().strftime("%Y-%m-%d   %H%M%S")
print(data_atual)

for arquivo in lista_arquivos:
    nome_completo_arquivo = f"{nome_da_pasta_selecionada}/{arquivo}" 
    nome_final_arquivo = f"{nome_completo_pasta_backup}/{data_atual}/{arquivo}"

    if not os.path.exists(f"{nome_completo_pasta_backup}/{data_atual}"):#
        os.mkdir(f"{nome_completo_pasta_backup}/{data_atual}")


    if "." in arquivo: # copia arquivos, pois todo arquivo termina com um ponto
        shutil.copy2(nome_completo_arquivo,nome_final_arquivo)# copia o arquivo para nome_final_arquivo
    elif not "backup" in arquivo: # copia pastas, neste caso nao vai copiar a msma pasta criada "backup"
        shutil.copytree(nome_completo_arquivo,nome_final_arquivo)

    


