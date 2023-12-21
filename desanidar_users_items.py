import pandas as pd
import ast
from multiprocessing import Pool


columnas_anexo=["user_id","items_count","steam_id","user_url","item_id","item_name","playtime_forever","playtime_2weeks"]

def procesar(elemento):
    dicc=ast.literal_eval(elemento)

    nuevo=pd.DataFrame(dicc["items"])
    for i in range(0,4):
        nuevo[columnas_anexo[i]]=dicc[columnas_anexo[i]]
    
    return nuevo

if __name__ == "__main__":
    
    nombre="datasets_default/australian_users_items.json"

    with open(nombre,"r",encoding="utf-8") as arch:
        lista=arch.readlines()

    num_procesos=4

    pool1=Pool(processes=num_procesos)

    pool2=Pool(processes=num_procesos)

    print("procesando...")

    resultados = pool2.starmap(procesar,[(elemento,) for elemento in lista])    

    anexo=pd.concat(resultados,ignore_index=True)
    print("guardando....")    
    
    anexo.to_parquet("datasets/users_items.parquet",index=False)
    print("parquet creado")