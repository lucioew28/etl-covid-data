# **Exploratory analysis of data in the Covid-19**
Análise exploratória dos dados do banco de dados Covid-19 disponibilizado pelo Governo do Estado do Espírito Santo, disponível em: https://coronavirus.es.gov.br/painel-covid-19-es.

Baixe o arquivo CSV disponível no site e utilize a tecnologia que melhor lhe convier para filtrar as pessoas residentes no município de Cariacica que fumam e faleceram entre 2020 e 2023.

---

## 🐛 **Como executar a aplicação:**

Clone o repositório e acesse a pasta `initial-diagnosis-business-intelligence`:

```bash
$ git clone git@github.com:jhonyrdesouza/initial-diagnosis-business-intelligence.git && cd initial-diagnosis-business-intelligence
```

Acesse [o painel Covid-19](https://coronavirus.es.gov.br/painel-covid-19-es) e clique em `baixar dados CSV`, feito isso adicione o arquivo baixado no diretório principal do projeto.

Instale as dependencias necessárias para a execução do projeto:

```bash
$ pip install -r requirements.txt
```

```py
# Libraries used:
pandas==1.4.4
psycopg2==2.9.5

```

Para iniciar a aplicação localmente, será necessário a utilização de um banco de dados Postgres, que pode ser baixado localmente ou utilizado a partir de um container Docker (recomendado), para o segundo caso, leia na sessão Docker abaixo.

E para inicializar a aplicação, execute os comandos abaixo:

```bash
$ python3 main.py
```

---

## 🐳 **Docker:**

Para desenvolvimento local, com reload na aplicação, é possível utilizar o docker-compose.db.yml para subir um container com o banco de dados Postgres. Para isso, execute o seguinte comando:

```bash
$ docker-compose -f ./docker/development/docker-compose.dev.yml up -d
```