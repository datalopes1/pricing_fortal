from sqlalchemy import create_engine
import pandas as pd

# Criar conexões com os bancos
sqlite_engine = create_engine('sqlite:///data/db_imoveis.db')
postgres_engine = create_engine(
    'postgresql://user:pass@host/database'
)

# Ingerir os dados no banco de dados em cloud
df = pd.read_sql("SELECT * FROM imoveis", sqlite_engine)

df.to_sql(
    'raw_imoveis',
    postgres_engine,  
    if_exists='replace',
    index=False,
    method='multi'  
)

print('Ingestão de dados completa.')