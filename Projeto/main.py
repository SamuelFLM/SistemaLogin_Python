import Conexao
import pyodbc
import os
#Interface do sistema

#Função main aonde chamo toda estrutura:
def main():
    os.system('cls')
    Conexao.parametro_para_titulo("TELA PRINCIPAL")
    Conexao.switch_case(
    "\n 1 - Realizar Login"
    "\n 2 - Realizar Cadastro"
    "\n Digite"
)

main()




