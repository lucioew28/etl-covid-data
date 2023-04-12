import psycopg2
from src.database.connection import connect

def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS staging (
            ID SERIAL PRIMARY KEY,
            DataNotificacao TEXT,
            DataCadastro TEXT,
            DataDiagnostico TEXT,
            DataColeta_RT_PCR TEXT,
            DataColetaTesteRapido TEXT,
            DataColetaSorologia TEXT,
            DataColetaSorologiaIGG TEXT,
            DataEncerramento TEXT,
            DataObito TEXT,
            Classificacao TEXT,
            Evolucao TEXT,
            CriterioConfirmacao TEXT,
            StatusNotificacao TEXT,
            Municipio TEXT,
            Bairro TEXT,
            FaixaEtaria TEXT,
            IdadeNaDataNotificacao TEXT,
            Sexo TEXT,
            RacaCor TEXT,
            Escolaridade TEXT,
            Gestante TEXT,
            Febre TEXT,
            DificuldadeRespiratoria TEXT,
            Tosse TEXT,
            Coriza TEXT,
            DorGarganta TEXT,
            Diarreia TEXT,
            Cefaleia TEXT,
            ComorbidadePulmao TEXT,
            ComorbidadeCardio TEXT,
            ComorbidadeRenal TEXT,
            ComorbidadeDiabetes TEXT,
            ComorbidadeTabagismo TEXT,
            ComorbidadeObesidade TEXT,
            FicouInternado TEXT,
            ViagemBrasil TEXT,
            ViagemInternacional TEXT,
            ProfissionalSaude TEXT,
            PossuiDeficiencia TEXT,
            MoradorDeRua TEXT,
            ResultadoRT_PCR TEXT,
            ResultadoTesteRapido TEXT,
            ResultadoSorologia TEXT,
            ResultadoSorologia_IGG TEXT,
            TipoTesteRapido TEXT
        );
    """)
    conn.commit()
    cur.close()
    conn.close()
    print('Table created successfully')