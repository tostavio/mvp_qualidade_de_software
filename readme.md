## Como executar 


Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Para testar o modelo, basta executar:

```
pytest -v test_modelos.py
```

## Frontend

Para abrir o frontend, basta abrir o arquivo `index.html` que está em `frontend/index.html` no seu navegador.