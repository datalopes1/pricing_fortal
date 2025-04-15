import pandas as pd
import sqlite3
from datetime import datetime

lopes = pd.read_csv("data/processed/lopes_imoveis.csv")
lopes['_source'] = 'Imobiliária Lopes'
lopes['_datetime'] = datetime.now()

chaves_aptos = pd.read_csv("data/processed/chaves_aptos.csv")
chaves_aptos['_source'] = 'Chaves na Mão'
chaves_aptos['_datetime'] = datetime.now()

chaves_casas = pd.read_csv("data/processed/chaves_casas.csv")
chaves_casas['_source'] = 'Chaves na Mão'
chaves_casas['_datetime'] = datetime.now()

chaves_cond = pd.read_csv("data/processed/chaves_condominio.csv")
chaves_cond['_source'] = 'Chaves na Mão'
chaves_cond['_datetime'] = datetime.now()

conn = sqlite3.connect('data/db_imoveis.db')
lopes.to_sql('imoveis', conn, if_exists='replace', index=False)
chaves_aptos.to_sql('imoveis', conn, if_exists='append', index=False)
chaves_casas.to_sql('imoveis', conn, if_exists='append', index=False)
chaves_cond.to_sql('imoveis', conn, if_exists='append', index=False)
conn.close()