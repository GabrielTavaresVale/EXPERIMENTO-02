import numpy as np
import csv
nome_do_arquivo = 'COSMO_artigo.csv'

def identificar_limites_da_janela(nome_do_arquivo):
    numero_da_linha = 0
    with open(nome_do_arquivo, 'r') as arquivo:
        reader = csv.reader(arquivo)
        menor_latitude = 99999
        menor_longitude = 99999
        maior_latitude = -99999
        maior_longitude = -99999
        numero_da_linha = 0
        for linha in reader:
          if numero_da_linha == 0:
            numero_da_linha += 1
            continue
          #if numero_da_linha >= 100: 
              #print("100 linhas lidas")
              #break
          latitude, longitude , precipitacao = float(linha[3]), float(linha[4]), float(linha[11])

          if latitude < menor_latitude:
            menor_latitude = latitude
          if longitude < menor_longitude:
            menor_longitude = longitude
              
          if latitude > maior_latitude :
            maior_latitude = latitude
          if longitude > maior_longitude :
            maior_longitude = longitude

          numero_da_linha += 1  
          if numero_da_linha % 1000000 == 0:
            print(numero_da_linha, " Linhas lidas")
    return (menor_latitude, menor_longitude, maior_latitude, maior_longitude)
                
def criar_array_de_chuva(nome_do_arquivo, menor_latitude, menor_longitude, maior_latitude, maior_longitude):
    tamanho_latitude = maior_latitude - menor_latitude +1
    tamanho_longitude = maior_longitude - menor_longitude +1
    tamanho_latitude, tamanho_longitude = int(round(tamanho_latitude, 0)), int(round(tamanho_longitude, 0))

    array_de_chuva = np.full((73, tamanho_latitude * 10, tamanho_longitude * 10), -1, dtype=float)
    with open(nome_do_arquivo, 'r') as arquivo:
      reader = csv.reader(arquivo)
      indice_tempo = 0
      numero_da_linha = 0
      quantidade_repetidos = 0
      for linha in reader:
        if numero_da_linha == 0:
          numero_da_linha += 1
          continue

        if numero_da_linha % 100000 == 0:
            print("Lida linha", numero_da_linha)

        #if numero_da_linha % 1000 == 0:
        #    break

        latitude, longitude, precipitacao = float(linha[3]), float(linha[4]), float(linha[10])
        latitude_arredondada = round(latitude, 1)
        longitude_arredondada = round(longitude, 1)
        latitude_transladada = latitude_arredondada - menor_latitude
        longitude_transladada = longitude_arredondada - menor_longitude
        




        latitude_escalonada = int(latitude_transladada * 10)
        longitude_escalonada = int(longitude_transladada * 10)

        if array_de_chuva[indice_tempo, latitude_escalonada, longitude_escalonada] != -1:
            # print("Valor Repetido")
            quantidade_repetidos += 1
        else:
            array_de_chuva[indice_tempo, latitude_escalonada, longitude_escalonada] = precipitacao

        if indice_tempo < 72:
            indice_tempo = indice_tempo + 1
        else:
            indice_tempo = 0
        numero_da_linha += 1
    #print("Repetidos: ", quantidade_repetidos)
    #print(menor_latitude)
    #print(menor_longitude)
    #print(maior_latitude)
    #print(maior_longitude)
    lista_lat=np.array(latitude_transladada)
    lista_lat.ravel().astype('double').tofile("latitude-t-cosmo.bin")
    lista_long= np.array(longitude_transladada)
    lista_long.ravel().astype('double').tofile("longitude-t-cosmo.bin")
    return array_de_chuva
menor_latitude, menor_longitude, maior_latitude, maior_longitude = identificar_limites_da_janela(nome_do_arquivo)

array_de_chuva = criar_array_de_chuva(nome_do_arquivo, menor_latitude, menor_longitude, maior_latitude, maior_longitude)
print (array_de_chuva)

#array_de_chuva.ravel().astype('double').tofile("arquivo10-cosmo.bin")


    
 
