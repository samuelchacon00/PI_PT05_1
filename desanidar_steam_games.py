import pandas as pd
import json

nombre="datasets_default/output_steam_games.json"

with open(nombre,"r",encoding="utf-8") as arch:
    lineas=arch.readlines()

dicc=[json.loads(n) for n in lineas]
df=pd.DataFrame(dicc)
df.dropna(inplace=True)
df.to_csv("datasets/steam_games.csv",sep=";",index=False)
