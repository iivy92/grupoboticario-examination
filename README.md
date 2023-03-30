
# Grupo Boticário - Teste Técnico 💻
Esta aplicação tem como objetivo informar ao revendedor informações sobre cashback de acordo com o volume de venda. 


## Rodando localmente ⚙️

Clone o projeto

```bash
  git clone https://github.com/iivy92/grupoboticario-examination
```

Entre no diretório do projeto

```bash
  cd grupoboticario-examination
```

Crie o ambiente virtual

```bash
  pythom -m venv .venv
  source .venv/bin/activate
```

Instale as dependências

```bash
  pip install -r requirements.txt
```

Execute o projeto

```bash
  uvicorn main:app --reload
```

Ou use docker para subir o projeto em um container

```bash
  docker-compose up --build 
```

## Executando os testes 📈

```bash
  make test
```


## Documentação 📝 
após subir aplição, documentação swagger disponível [aqui](http://0.0.0.0:8000/docs)


## Rotas 🌐
#### Realizar cadastro de revendedor 
```http
  POST /v1/users/signup
```
| Parâmetro   | Tipo       | Descrição                           |Exemplo      |
| :---------- | :--------- | :---------------------------------- |:----------- |
| `name` | `string` | **Obrigatório**. Nome do usuario | Pedro Ivo |
| `cpf` | `string` | **Obrigatório**. CPF | 0337410509 |
| `email` | `string` | **Obrigatório**. Email do usuario | email@example.com
| `password` | `string` | **Obrigatório**. Senha | Password#123

#### Realizar login revendedor 
```http
  POST /v1/users/signin
```
| Parâmetro   | Tipo       | Descrição                           |Exemplo      |
| :---------- | :--------- | :---------------------------------- |:----------- |
| `username` | `string` | **Obrigatório**. CPF | 03374110509 |
| `password` | `string` | **Obrigatório**. Senha |Password#123 |

#### informações revendedor 
```http
  GET /v1/users/me 
```

#### Cadastrar compra 

```http
  POST /v1/items/create
```

| Parâmetro   | Tipo       | Descrição                           |Exemplo      |
| :---------- | :--------- | :---------------------------------- |:----------- |
| `code` | `string` | **Obrigatório**. Código da compra| btc230492 |
 | `date` | `string date` | **Obrigatório**. Data da compra | 2023-03-24 |
| `price` | `string` | **Obrigatório**. Preço da compra | 59.90 |
| `status` | `string` | Status do pedido | (approved, in_validation) |

#### Listar compras com informações de cashback

```http
  GET /v1/items/search
```
| Parâmetro   | Tipo       | Descrição                           |Exemplo      |
| :---------- | :--------- | :---------------------------------- |:----------- |
| `date` | `string date` | Data da compra| 2023-03-24 |


#### Informar total de cashback acumulado

```http
  GET /v1/items/accumulated-credit
```


## Autores 🎯

- [@pedroivo](https://www.linkedin.com/in/pedroivo33/)

