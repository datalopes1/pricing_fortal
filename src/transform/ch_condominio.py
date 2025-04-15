import pandas as pd 

chaves = pd.read_json("data/raw/chaves_condominio.json")

# Limpeza do dados da Chaves na Mão
## Processos iniciais
chaves.drop(index=[670], inplace=True)
chaves.dropna(subset='preco', inplace=True)
chaves.drop_duplicates(inplace=True)

## Limpeza das colunas com dtype FLOAT
for col in ['preco', 'condo']:
    chaves.fillna({col: '0'}, inplace=True)
    chaves[col] = chaves[col].astype(str).str.replace('[^0-9]', '', regex=True)
    chaves[col] = chaves[col].astype(float)

## Limpeza das colunas com dtype INT
chaves.fillna({'area': 0, 'quartos': 0,'banheiros': 0, 'vagas': 0}, inplace=True)
chaves['area'] = chaves['area'].astype(int)
chaves['banheiros'] = chaves['banheiros'].astype(int)
chaves['vagas'] = chaves['vagas'].astype(int)
chaves['quartos'] = chaves['quartos'].astype(int)

## Limpeza da localização > bairro
chaves['localizacao'] = chaves['localizacao'].astype(str).str.split(',', expand=True)[0]

chaves.rename(columns={'localizacao': 'bairro', 'condo': 'condominio'}, inplace=True)
chaves = chaves[['tipo', 'bairro', 'area', 'quartos', 'banheiros', 'vagas', 'condominio', 'preco']]
chaves.reset_index(drop=True, inplace=True)

## Salvando os dados em .csv 
chaves.to_csv("data/processed/chaves_condominio.csv", index=False)
print("Dados salvos na pasta data/processed/")
