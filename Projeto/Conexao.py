import os
import pyodbc
import time

# Função para limpar tela terminal
def limpar_tela_terminal():
    os.system('cls')


# Função para aplicar titulo para qualquer estrutura
def parametro_para_titulo(nome_titulo):
    print(20 * "*")
    print(f"    {nome_titulo}   ")
    print(20 * "*")


# Função para direcionar opcao usuario
# Parametro: Passo str para modular a pergunta para o usuario e recebo int para aplicar nas opção;
def switch_case(pergunta):
    opcao_usuario = int(input(f"{pergunta}:"))
    match opcao_usuario:
        case 1:
            tela_login()
        case 2:
            tela_cadastro()


# Função para direcionar o cadastro do usuario
def tela_cadastro():
    limpar_tela_terminal()
    parametro_para_titulo("CADASTRO")
    inserindo_dados_usuario()
    print("\nCADASTRO REALIZADO COM SUCESSO!")
    print("Você será direcionado para pagina de login")
    time.sleep(3.0)
    tela_login()


# Função para direcionar o login do usuario
def tela_login():
    limite_tentativas_login = 0
    while(limite_tentativas_login <= 3):
        limpar_tela_terminal()
        parametro_para_titulo("LOGIN")

        limite_tentativas_login += 1
        login_email = input("\nINFORME SEU E-MAIL: ")
        login_senha = input("\nINFORME SUA SENHA: ")
        if(validacao_login(login_email, login_senha)):
            print("LOGIN EFETUADO COM SUCESSO")
            break;
        else:
            print("E-MAIL OU SENHA INVALIDOS")
            time.sleep(1.5)

# ********Conexao com Banco de dados***************
# Passando as informação referente ao meu banco de dados
dados_conexao = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=coloque seu host;"
    "Database=coloque banco de dados;"
    "UID=sa;"
    "PWD=coloque sua senha;"
)
# Faz a conexao com o Banco
conectar_DB = pyodbc.connect(dados_conexao)
# Executa a consulta
cursor = conectar_DB.cursor()

# Função responsavel por receber inputs do usuario
def inserindo_dados_usuario():
    nome = input("\nINFORME SEU NOME: ")
    email = input("\nINFORME SEU EMAIL: ")
    senha = input('\nINFORME SUA SENHA: ')
    sexo = input("\n INFORME SEU SEXO[M | F]: ")

    # Query SQL Server
    sql_inclusao_dados = f"""
        INSERT INTO coloque_tabela(NOME, EMAIL, SENHA, SEXO)
        VALUES('{nome}', '{email}','{senha}', '{sexo}')"""
    # Manda os dados para o Banco
    cursor.execute(sql_inclusao_dados)
    # Sempre que tiver fazendo algo no banco[Inserindo,deletando, alterando] , tem que inserir o commit
    cursor.commit()

def validacao_login(email, senha):
    # Faz a leitura no banco de dados
    cursor.execute(f"""
    select * from coloque_banco_de_dados where EMAIL='{email}' and SENHA='{senha}'
    """)
    rows = cursor.fetchall()
    return rows

