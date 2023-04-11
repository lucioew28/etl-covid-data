import csv
import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="exampledb",
    user="docker",
    password="docker"
)

# Open the CSV file and read its contents into a list of dictionaries
with open('MICRODADOS_TREATED.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

# Define the table name and column names for the database table
table_name = 'staging'
column_names = [
    'DataNotificacao',
    'DataCadastro',
    'DataDiagnostico',
    'DataColeta_RT_PCR',
    'DataColetaTesteRapido',
    'DataColetaSorologia',
    'DataColetaSorologiaIGG',
    'DataEncerramento',
    'DataObito',
    'Classificacao',
    'Evolucao',
    'CriterioConfirmacao',
    'StatusNotificacao',
    'Municipio',
    'Bairro',
    'FaixaEtaria',
    'IdadeNaDataNotificacao',
    'Sexo',
    'RacaCor',
    'Escolaridade',
    'Gestante',
    'Febre',
    'DificuldadeRespiratoria',
    'Tosse',
    'Coriza',
    'DorGarganta',
    'Diarreia',
    'Cefaleia',
    'ComorbidadePulmao',
    'ComorbidadeCardio',
    'ComorbidadeRenal',
    'ComorbidadeDiabetes',
    'ComorbidadeTabagismo',
    'ComorbidadeObesidade',
    'FicouInternado',
    'ViagemBrasil',
    'ViagemInternacional',
    'ProfissionalSaude',
    'PossuiDeficiencia',
    'MoradorDeRua',
    'ResultadoRT_PCR',
    'ResultadoTesteRapido',
    'ResultadoSorologia',
    'ResultadoSorologia_IGG',
    'TipoTesteRapido'
]

# Construct the SQL INSERT statement using placeholders for the column values
sql = 'INSERT INTO {} ({}) VALUES ({})'.format(
    table_name,
    ', '.join(column_names),
    ', '.join(['%({})s'.format(column) for column in column_names])
)

# Insert the data into the database table
with conn.cursor() as cur:
    for row in data:
        cur.execute(sql, row)
    conn.commit()

# Close the database connection
conn.close()
