from src.database.connection import connect 

def create_fact_table():
    conn = connect()
    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS localidade CASCADE')
    cur.execute('''
        CREATE TABLE localidade (
            id SERIAL PRIMARY KEY,
            municipio TEXT,
            bairro TEXT
        )
    ''')
    
    cur.execute('DROP TABLE IF EXISTS idade CASCADE')
    cur.execute('''
        CREATE TABLE idade (
            id SERIAL PRIMARY KEY,
            faixa_etaria TEXT,
            idade_na_data_notificacao TEXT
        )
    ''')

    cur.execute('DROP TABLE IF EXISTS sexo CASCADE')
    cur.execute('''
        CREATE TABLE sexo (
            id SERIAL PRIMARY KEY,
            genero TEXT
        )
    ''')

    cur.execute('DROP TABLE IF EXISTS raca_cor CASCADE')
    cur.execute('''
        CREATE TABLE raca_cor (
            id SERIAL PRIMARY KEY,
            descricao TEXT
        )
    ''')

    cur.execute('DROP TABLE IF EXISTS escolaridade CASCADE')
    cur.execute('''
        CREATE TABLE escolaridade (
            id SERIAL PRIMARY KEY,
            nivel TEXT
        )
    ''')

    cur.execute('DROP TABLE IF EXISTS morte')
    cur.execute('''
        CREATE TABLE morte (
            id SERIAL PRIMARY KEY,
            data_obito TEXT,
            localidade_id INTEGER REFERENCES localidade(id),
            idade_id INTEGER REFERENCES idade(id),
            sexo_id INTEGER REFERENCES sexo(id),
            raca_cor_id INTEGER REFERENCES raca_cor(id),
            escolaridade_id INTEGER REFERENCES escolaridade(id)
        )
    ''')

    conn.commit()
    cur.close()
    conn.close()
