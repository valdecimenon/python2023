import sqlite3

from produto import Produto

#dao = data access object = objeto de acesso a dados

SQL_PREPARA_BANCO =   'CREATE TABLE IF NOT EXISTS PRODUTO (' \
                      'descricao varchar(60) not null,' \
                      'preco double not null,' \
                      'quantidade integer not null' \
                      ');'

# create for me a code to insert a table with 3 columns
SQL_SALVA_PRODUTO = 'INSERT INTO PRODUTO VALUES (?, ?, ?)'
SQL_LISTA_PRODUTOS = 'SELECT descricao, preco, quantidade, rowid from produto'

class ProdutoDAO:
    #construtor
    def __init__(self, nome_banco):
        self.__nome_banco = nome_banco
        self.prepara_banco()

    def prepara_banco(self):
        print('Conectando com o banco de dados...', end='')
        conexao = sqlite3.connect(self.__nome_banco)
        conexao.cursor().execute(SQL_PREPARA_BANCO)
        #no final, precisamos fazer um commit para confirmar
        conexao.commit()
        print('OK')


    def salvar(self, produto):
        print('Salvando produto...', end='')
        conexao = sqlite3.connect(self.__nome_banco)
        cursor = conexao.cursor()

        cursor.execute(SQL_SALVA_PRODUTO, (produto.descricao, produto.preco, produto.quantidade))
        produto.id = cursor.lastrowid
        #confirma a operação
        conexao.commit()
        print('OK')

    def listar(self):
        conexao = sqlite3.connect(self.__nome_banco)
        cursor = conexao.cursor()
        cursor.execute(SQL_LISTA_PRODUTOS)
        #converte a lista de tuplas em lista de produtos
        produtos = traduz_produtos(cursor.fetchall())
        return produtos

#              0                               1
#('TV SAMSUNG', 2999.99, 10, 1), ('TV SAMSUNG', 2999.99, 10, 2)]
def traduz_produtos(lista):
    produtos = []
    for tupla in lista:
        # tupla = ('TV SAMSUNG', 2999.99, 10, 1)
        p = Produto(tupla[0], tupla[1], tupla[2], tupla[3])
        produtos.append(p)
    return produtos

