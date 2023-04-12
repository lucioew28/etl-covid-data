from src.database.connection import connect 

def populate_star_schema():
    conn = connect()
    cur = conn.cursor()

    cur.execute('''
        INSERT INTO localidade (municipio, bairro)
            SELECT 
                Municipio,
                Bairro
            FROM staging
    ''')

    cur.execute('''
        INSERT INTO idade (faixa_etaria, idade_na_data_notificacao)
            SELECT 
                FaixaEtaria,
                IdadeNaDataNotificacao
            FROM staging
    ''')

    cur.execute('''
        INSERT INTO sexo (genero)
            SELECT 
                Sexo
            FROM staging
    ''')

    cur.execute('''
        INSERT INTO raca_cor (descricao)
            SELECT 
                RacaCor
            FROM staging
    ''')
   

    cur.execute('''
        INSERT INTO escolaridade (nivel)
            SELECT 
                Escolaridade
            FROM staging
    ''')

    
    cur.execute('''
        INSERT INTO morte (data_obito)
            SELECT 
                dataobito
            FROM staging
                WHERE dataobito IS NOT NULL  AND dataobito <> ''
    ''')
   
    conn.commit()
    cur.close()
    conn.close()
