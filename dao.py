#dao = Data Access Object ou Objeto de Acesso a Dados
#módulo responsável pelo acesso ao banco de dados
import sqlite3

SQL_PREPARA_BANCO = 'CREATE TABLE IF NOT EXISTS produto (' \
                         'descricao VARCHAR(60) NOT NULL,' \
                         'preco DOUBLE NOT NULL,' \
                         'quantidade INTEGER NOT NULL' \
                    ');'

SQL_SALVA_PRODUTO = 'INSERT INTO produto VALUES (?, ?, ?)'
SQL_LISTA_PRODUTOS = 'SELECT descricao, preco, quantidade, rowid FROM produto'
SQL_PRODUTO_POR_ID = 'SELECT descricao, preco, quantidade, rowid FROM produto WHERE rowid=?'
SQL_ATUALIZA_PRODUTO = 'UPDATE produto SET descricao=?, preco=?, quantidade=? WHERE rowid=?'
SQL_DELETA_PRODUTO = 'DELETE FROM produto WHERE rowid=?'


class ProdutoDao:

    def __init__(self, nome_banco):
        self.__nome_banco = nome_banco
        self.prepara_banco()

    def prepara_banco(self):
        print('Conectando com o banco de dados...', end='')
        conexao = sqlite3.connect(self.__nome_banco)
        cursor = conexao.cursor()
        cursor.execute(SQL_PREPARA_BANCO)
        #comitando senão nada terá efeito
        conexao.commit()
        print('OK')

    def salvar(self, produto):
        print('Salvando produto...', end='')
        conexao = sqlite3.connect(self.__nome_banco)
        cursor = conexao.cursor()
        cursor.execute(SQL_SALVA_PRODUTO, (produto.descricao, produto.preco, produto.quantidade))
        produto.id = cursor.lastrowid
        conexao.commit()
        print('OK')
        return produto #devolve o mesmo produto, porém agora com o id

    def listar(self):
        conexao = sqlite3.connect(self.__nome_banco)
        cursor = conexao.cursor()
        cursor.execute(SQL_LISTA_PRODUTOS)
        #converte a lista de dados em lista de objetos tipo Produto
        produtos = traduz_produtos(cursor.fetchall())
        return produtos

def traduz_produtos(self, produtos):
   pass


