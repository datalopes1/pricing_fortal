import pandas as pd 

lopes = pd.read_json("data/raw/lopes.json")

# Limpeza do dados da Imobiliária Lopes
## Processos iniciais
lopes.dropna(subset='preco', inplace=True)

## Limpeza das colunas com dtype FLOAT
for col in ['preco', 'condo']:
    lopes.fillna({col: '0'}, inplace=True)
    lopes[col] = lopes[col].astype(str).str.replace('[^0-9]', '', regex=True)
    lopes[col] = lopes[col].astype(float)

## Limpeza das colunas com dtype INT
for col in ['area', 'quartos', 'banheiros', 'vagas']:
    lopes.fillna({col: 0}, inplace=True)
    lopes[col] = lopes[col].astype(str).str.replace('[^0-9d]', '', regex=True)
    lopes[col] = lopes[col].astype(int)

## Limpeza da localização > bairro
lopes['localizacao'] = lopes['localizacao'].astype(str).str.split(',', expand=True)[1]
lopes['localizacao'] = lopes['localizacao'].astype(str).str.split('-', expand=True)[0]
lopes['localizacao'] = lopes['localizacao'].astype(str).str.strip()

lopes.rename(columns={'localizacao': 'bairro', 'condo': 'condominio'}, inplace=True)
lopes = lopes[['tipo', 'bairro', 'area', 'quartos', 'banheiros', 'vagas', 'condominio', 'preco']]

## Salvando em formato .csv
lopes.to_csv("data/processed/lopes_imoveis.csv", index=False)