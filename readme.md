## Como executar 


Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

```
pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
flask run --host 0.0.0.0 --port 5000
```

Para testar o modelo, basta executar:

```
pytest -v test_modelos.py
```

## Frontend

Para abrir o frontend, basta abrir o arquivo [index.html](./front/index.html) no seu navegador.

## Notebook

Para acessar o notebook feito no Google Colab, basta clicar [aqui](https://colab.research.google.com/drive/1MPBBGNpXM3T4bnK7M7lDNRor-mUZtUo6?usp=sharing).
Ele também está versionado no diretório [Modelo_Alzheimer.ipynb](./MachineLearning/notebooks/Modelo_Alzheimer.ipynb).

## Dataset

O Dataset está em [alzheimers_disease_data.csv](./MachineLearning/data/alzheimers_disease_data.csv), mas você também pode ver o original aqui: [Alzheimer's Disease Dataset](https://www.kaggle.com/jboysen/mri-and-alzheimers), ou no meu github [aqui](https://raw.githubusercontent.com/tostavio/datasets/refs/heads/main/alzheimers_disease_data.csv)