"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():

    #
    # Inserte su código aquí
    #
    data_raw = pd.read_fwf('clusters_report.txt', colspecs=[(3,5), (9,14), (25,29), (40,119)], header = None)
    data_raw.drop(data_raw.index[:3], inplace = True)
    data_raw.reset_index(drop = True, inplace = True)

    df = pd.DataFrame()
    df['cluster']= data_raw[0]
    df['cantidad_de_palabras_clave'] = data_raw[1]
    df['porcentaje_de_palabras_clave'] = data_raw[2].str.replace(',','.')

    df.dropna(inplace = True)
    df.reset_index(drop = True, inplace = True)

    df['cluster']= df['cluster'].str.strip().astype(int)
    df['cantidad_de_palabras_clave'] = df['cantidad_de_palabras_clave'].str.strip().astype(int)
    df['porcentaje_de_palabras_clave'] = df['porcentaje_de_palabras_clave'].str.strip().astype(float)

    list_1 = []
    [list_1.append(i) for i in data_raw[3]]
    pal_claves = ' '.join(list_1).replace('control multi', 'control.multi')

    list_2 = []
    [list_2.append(i.strip()) for i in pal_claves[:-1].split('.')]
    
    df['principales_palabras_clave'] = pd.concat([pd.Series(i) for i in list_2]).reset_index(drop= True)
    df['principales_palabras_clave'] = df['principales_palabras_clave'].str.replace('  ',' ').str.replace('  ',' ').str.replace('  ',' ')

    return df
