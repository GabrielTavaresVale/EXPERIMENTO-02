import numpy as np
import csv
from collections import OrderedDict
import struct
nome_do_arquivo = 'COSMO_artigo.csv'

def salvar_lista_de_doubles_em_binario(nome_do_arquivo, lista_de_valores):
    arquivo_de_saida = open(nome_do_arquivo,"wb")
    s = struct.pack('d'*len(lista_de_valores), *lista_de_valores)
    
    arquivo_de_saida.write(s)
    
    arquivo_de_saida.close()

def criar_lista_de_indices_para_dimensao(nome_do_arquivo, indice_da_coluna):
    with open(nome_do_arquivo, 'r') as arquivo:
      reader = csv.reader(arquivo)

      numero_da_linha = 0
      lista_de_indices = []
      # ---------------------Ler Índices---------------------
      for linha in reader:
        # Para pular a primeira linha
        if numero_da_linha == 0:
          numero_da_linha += 1
          continue

        # Para ler apenas os 100 primeiros valores
        
            

        # Salva a latitude no array, se não existir
        valor_da_dimensao=float(linha[indice_da_coluna])
        lista_de_indices.append(valor_da_dimensao)
        numero_da_linha += 1
      
      
    return lista_de_indices

lista_de_tempo = criar_lista_de_indices_para_dimensao(nome_do_arquivo, 1)
#lista_de_latitudes = criar_lista_de_indices_para_dimensao(nome_do_arquivo, 3)
#lista_de_longitudes = criar_lista_de_indices_para_dimensao(nome_do_arquivo, 4)
#lista_de_preciptacao= criar_lista_de_indices_para_dimensao(nome_do_arquivo,10)
#print(lista_de_latitudes)
#print(lista_de_longitudes)
#print(lista_de_preciptacao)


salvar_lista_de_doubles_em_binario("indice-tempo-total-cosmo.bin", lista_de_tempo)
#salvar_lista_de_doubles_em_binario("long-Total-cosmo.bin", lista_de_longitudes)
#salvar_lista_de_doubles_em_binario("precipitacao-Total-cosmo.bin", lista_de_preciptacao)
