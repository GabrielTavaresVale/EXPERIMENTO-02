from importlib.resources import open_binary
from tkinter import N
from venv import create
import numpy as np
import csv
import pandas as pd
import sys 
import struct
from array import array
nome_do_arquivo = 'COSMO_artigo.csv'

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
        # Para ler apenas os 10000 primeiros valores
        
        
            
        # Salva a latitude no array, se não existir
        valor_da_dimensao=float(linha[indice_da_coluna])
        if valor_da_dimensao not in lista_de_indices:
            lista_de_indices.append(valor_da_dimensao)
        numero_da_linha += 1
    return lista_de_indices

def procurar_valor_da_chuva_no_dataset(nome_do_arquivo, lat, long):
    with open(nome_do_arquivo, 'r') as arquivo:
        reader = csv.reader(arquivo)
        numero_da_linha = 0
        for linha in reader:
            if numero_da_linha == 0:
                numero_da_linha += 1
                continue
            
                
            
                
            numero_da_linha += 1
            if float(linha[3]) == lat and float(linha[4]) == long:
                return linha[10]
        return -1
def escrever_no_arquivo_binario(nome_do_arquivo,preciptacao):
    with open(nome_do_arquivo, 'r') as arquivo:
        reader = csv.reader(arquivo)
        numero_da_linha = 0
        cont=0
        for linha in reader:
            if numero_da_linha == 0:
                numero_da_linha += 1
                continue
            
                
            
                
            
                
            preciptacao=float(linha[10])
            array_de_chuvas=[]
            array_de_chuvas.append(preciptacao)
            numero_da_linha+=1
            
            
            


            
            
            
        handle=open('chuvas-cosmo-Dataset.bin','ab')
        handle.write(struct.pack('<%dd'% len(array_de_chuvas),*array_de_chuvas))
        handle.close
        cont+=1

            
            
            
            
            

            


def criar_array_de_atributo(nome_do_arquivo,listas_de_latitudes,listas_de_longitudes, indice_atributo):
    n=0

    for lat in listas_de_latitudes:
      for long in listas_de_longitudes:
          precipitacao = procurar_valor_da_chuva_no_dataset(nome_do_arquivo, lat, long)
          #escrever_no_arquivo_binario(nome_arquivo_de_saida, precipitacao)
          escrever_no_arquivo_binario(nome_do_arquivo,precipitacao)
          
          
          
          
          
          
          # Trocar por escrever em sequencia em um arquivo binario

lista_de_latitudes = criar_lista_de_indices_para_dimensao(nome_do_arquivo, 3)
lista_de_longitudes = criar_lista_de_indices_para_dimensao(nome_do_arquivo, 4)

criar_array_de_atributo(nome_do_arquivo,lista_de_latitudes,
                                        lista_de_longitudes, indice_atributo=10)