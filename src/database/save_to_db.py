from src.database.connection import connect

def save_to_database(df, database):
    # Get a connection to the database
    conn = connect()
    
    # Drop the microdados_filtrados table if it already exists
    with conn.cursor() as cur:
        cur.execute('DROP TABLE IF EXISTS microdados_filtrados')

    # Create the microdados_filtrados table with columns based on the input DataFrame
    columns = ', '.join([f"{col} TEXT" for col in df.columns])
    with conn.cursor() as cur:
        cur.execute(f"CREATE TABLE microdados_filtrados ({columns})")

    # Insert the data from the DataFrame into the microdados_filtrados table
    values_placeholder = ', '.join(['%s' for _ in range(len(df.columns))])
    values = [tuple(row) for row in df.to_numpy()]
    with conn.cursor() as cur:
        cur.executemany(f"INSERT INTO microdados_filtrados VALUES ({values_placeholder})", values)

    # Create the fato table with fixed columns
    with conn.cursor() as cur:
        cur.execute('CREATE TABLE fato (dim_racacor TEXT, dim_sexo TEXT, dim_comorbidadetabagismo TEXT, dim_bairro TEXT, dim_dataobito TEXT)')

    # Insert data from microdados_filtrados table into fato table
    with conn.cursor() as cur:
        cur.execute('INSERT INTO fato (dim_racacor, dim_sexo, dim_comorbidadetabagismo, dim_bairro, dim_dataobito) SELECT racacor, sexo, comorbidadetabagismo, bairro, dataobito FROM microdados_filtrados')

    # Commit changes and close the connection
    conn.commit()
    conn.close()
