import pandas as pd
import ast
from multiprocessing import Pool

def procesar(i,df):
    nueva_tabla=pd.DataFrame(df.at[i,"reviews"])
    nueva_tabla["user_id"]=df.at[i,"user_id"]
    nueva_tabla["user_url"]=df.at[i,"user_url"]
    #nuevo=pd.concat([nuevo,nueva_tabla],ignore_index=True)
    #print(str(t)+" | "+str(i),end="\r")
    return nueva_tabla

if __name__=="__main__":
    n_reviews="datasets_default/australian_user_reviews.json"

    with open(n_reviews,"r",encoding="utf-8") as arch:
        contenido=arch.read()

    contenido=contenido.replace("\n",",")

    dicc=ast.literal_eval(contenido)

    df=pd.DataFrame(dicc)

    encabezado=["user_id","user_url","funny","posted","last_edited","item_id","help_ful","recommend","review"]
    nuevo=pd.DataFrame(columns=encabezado)

    t=len(df)

    pool=Pool(processes=4)
    print("procesando...")

    resultados = pool.starmap(procesar,[(i,df) for i in df.index])    
    nuevo=pd.concat(resultados,ignore_index=True)

    print("guardando...")
    nuevo.to_csv("datasets/user_reviews.csv",index=False,sep=";")