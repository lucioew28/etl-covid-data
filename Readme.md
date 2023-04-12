# **ETL Project**
![alt text](https://github.com/lucioew28/etl-covid-data/blob/main/assets/star-schema.png?raw=true)
---

The objective of the project is to create a ETL (Extrac, Transform and Load) using the Codivi dataset : https://coronavirus.es.gov.br/painel-covid-19-es.

---

## **How to use it:**

1) Clone the repo `etl-covid-data`:

```bash
$ git clone git@github.com:lucioew28/etl-covid-data.git && cd etl-covid-data
```

2) Install the dependencies

```bash
$ pip install -r requirements.txt
```

3) This project uses Postgres as its database so you can download it from here : https://www.postgresql.org/download/ or if you prefer there is also the option of using docker compose command to launch a container with Postgres and a webviewer

```bash
$ docker-compose up -d
```

4) The last step is to run the main.py file that is going to do all the heavy work for you 👍

```bash
$ python3 main.py
```
