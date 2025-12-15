import pandas as pd
import streamlit as st
import joblib

df_dados = pd.read_csv('dados.csv')

df_dados.drop('Unnamed: 0', axis=1, inplace= True)
df_dados.drop('price', axis=1, inplace= True)
atributos = list(df_dados.columns)

x_numericos_keys = ['host_listings_count', 'latitude', 'longitude', 'accommodates', 'bathrooms', 'bedrooms', 'beds', 'extra_people', 'minimum_nights', 'month', 'year', 'n_amenities']

x_tf_keys = ['host_is_superhost', 'instant_bookable']

x_numericos = dict.fromkeys(x_numericos_keys,0)

x_tf = dict.fromkeys(x_tf_keys,0)

x_listas = {}

for col in df_dados:

    valor = df_dados.loc[0, col]

    if 'type' in col:

        objeto_tipo = str(col).split('_')[0]

        nome_tipo = str(col).split('_')[2]

        if f'{objeto_tipo}_type' in x_listas.keys():
        
            
            x_listas[f'{objeto_tipo}_type'].append(nome_tipo)
        else:
            x_listas[f'{objeto_tipo}_type'] = [nome_tipo]
    elif 'cancellation' in col:

        categoria = str(col).replace('cancellation_policy_', '')

        categoria = categoria#.title().replace('_', ' ')

        if 'cancellation_policy' in x_listas.keys():
    
            
            x_listas['cancellation_policy'].append(categoria)
        else:
            x_listas['cancellation_policy'] = [categoria]


for item in x_numericos:

    if item == 'latitude' or item == 'longitude':
        valor = st.number_input(f'{item}', step= 0.00001, value= 0.0, format='%.5f')
    elif item == 'extra_people':
        valor = st.number_input(f'{item}', step= 0.01, value= 0.0, format='%.2f')
    else:
        valor = st.number_input(f'{item}', step= 1, value= 0)
    
    x_numericos[item] = valor

for item in x_tf:
    valor = st.selectbox(f'{item}', ('Sim', 'Não'))

    x_tf[item] = 1 if valor == 'Sim' else 0

dicionario = {}

for item, lista_opcoes in x_listas.items():
    
    valor = st.selectbox(f'{item}', lista_opcoes)

    for opcao in lista_opcoes:
        coluna_dummy = f'{item}_{opcao}'
        
        if valor == opcao:

            dicionario[coluna_dummy] = 1
        else:
            dicionario[coluna_dummy] = 0


botao = st.button('Prever Valor do Imóvel')

if botao:
    dicionario.update(x_numericos)
    dicionario.update(x_tf)
    
    valores_x = pd.DataFrame(dicionario, index=[0])
    
    valores_x = valores_x[atributos]  # Reordenando colunas de maneira simplificada

    modelo = joblib.load('modelo.joblib')

    preco = modelo.predict(valores_x)

    st.write(f'O preço da diária do imóvel é estimado em: R$ {preco[0]}')
