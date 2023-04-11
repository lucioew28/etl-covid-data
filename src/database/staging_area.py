import psycopg2
from src.database.connection import connect

def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS staging (
            DataNotificacao DATE,
            DataCadastro DATE,
            DataDiagnostico DATE,
            DataColeta_RT_PCR DATE,
            DataColetaTesteRapido DATE,
            DataColetaSorologia DATE,
            DataColetaSorologiaIGG DATE,
            DataEncerramento DATE,
            DataObito DATE,
            Classificacao TEXT,
            Evolucao TEXT,
            CriterioConfirmacao TEXT,
            StatusNotificacao TEXT,
            Municipio TEXT,
            Bairro TEXT,
            FaixaEtaria TEXT,
            IdadeNaDataNotificacao INTEGER,
            Sexo TEXT,
            RacaCor TEXT,
            Escolaridade TEXT,
            Gestante TEXT,
            Febre BOOLEAN,
            DificuldadeRespiratoria BOOLEAN,
            Tosse BOOLEAN,
            Coriza BOOLEAN,
            DorGarganta BOOLEAN,
            Diarreia BOOLEAN,
            Cefaleia BOOLEAN,
            ComorbidadePulmao BOOLEAN,
            ComorbidadeCardio BOOLEAN,
            ComorbidadeRenal BOOLEAN,
            ComorbidadeDiabetes BOOLEAN,
            ComorbidadeTabagismo BOOLEAN,
            ComorbidadeObesidade BOOLEAN,
            FicouInternado BOOLEAN,
            ViagemBrasil BOOLEAN,
            ViagemInternacional BOOLEAN,
            ProfissionalSaude BOOLEAN,
            PossuiDeficiencia BOOLEAN,
            MoradorDeRua BOOLEAN,
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