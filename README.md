# Machine Learning — Previsão de Preços no Airbnb

Este projeto tem como objetivo **prever o preço da diária de acomodações do Airbnb** do Rio de Janeiro utilizando técnicas de **Ciência de Dados e Machine Learning**, passando por todas as etapas do pipeline: análise exploratória, tratamento dos dados, modelagem, avaliação e *deploy* do modelo em uma aplicação interativa.

O foco do projeto é demonstrar **aplicação prática de Machine Learning em um problema real**, considerando não apenas a acurácia do modelo, mas também **tempo de execução e viabilidade para uso em produção**.

---

## Objetivo do Projeto
Construir um modelo de regressão capaz de estimar o preço da diária de um imóvel do Airbnb com base em características como:
- Localização
- Número de quartos e camas
- Comodidades
- Tipo de imóvel e quarto
- Políticas de cancelamento
- Perfil do anfitrião

---

## Dataset Utilizado

O dataset utilizado neste projeto foi obtido no **Kaggle**:

**Airbnb Rio de Janeiro**  
https://www.kaggle.com/datasets/allanbruno/airbnb-rio-de-janeiro/data

O conjunto de dados contém informações reais de anúncios do Airbnb no Rio de Janeiro, incluindo variáveis numéricas, categóricas, booleanas, geográficas e campos textuais/listas, o que o torna adequado para problemas de regressão e análise exploratória de dados.

---

## Estrutura do Repositório

```text
├── solucao_airbnb.ipynb          # Análise exploratória, tratamento dos dados e modelagem
├── DeployProjetoAirbnb.ipynb     # Preparação do modelo para deploy
├── DeployProjetoAirbnb.py        # Aplicação Streamlit
├── Top1000.xlsx                  # Subconjunto do dataset utilizado
├── README.md                     # Documentação do projeto