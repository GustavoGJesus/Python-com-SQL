from mysql.connector import connect, Error 


def criando_conexao():
    try:
        conexao = connect(user ='root', password='', host='127.0.0.1', database='db_motors')
        print("conexão:", conexao)
    except Error as erro: 
        print("Erro de conexão:\n", erro)
    else:
        return conexao

def fechando_conexao(con):
    con.close()
    print("\n Conexão fechada")

if __name__ == '__main__':
    conexao=criando_conexao()
    cursor=conexao.cursor()
    #conexao1 = connect(user ='root', password='', host='127.0.0.1', database='')
    sql="CREATE DATABASE if not exists db_motors"
    cursor.execute(sql)
    sql_tabela="""CREATE TABLE IF NOT EXISTS tb_carros(
        placa VARCHAR(7) UNIQUE NOT NULL,
        preco INT NOT NULL,
        km INT NOT NULL,
        data_de_aq date NULL,
        PRIMARY KEY (placa)
    )"""
    cursor.execute(sql_tabela)
    sql_ins="""
    insert into tb_carros (placa, preco, km, data_de_aq)
    values(%s, %s, %s, %s)
    """
    i_placa=input('Placa do carro: ')
    i_preco=input('Preco do carro: ')
    i_km=input('Quilometragem do carro: ')
    i_data_de_aq=input('Data de compra do carro (aaaa-mm-dd): ')
    tupla = (i_placa, i_preco, i_km, i_data_de_aq)
    cursor.execute(sql_ins, tupla)
    conexao.commit()
    
    sql = ''' select * from tb_carros'''
    cursor.execute(sql)
    registros = cursor.fetchall()

    for row in registros:
        
        print('Placa: ',row[0])
        print('Preco: ',row[1])
        print('Quilometragem: ',row[2])
        print('Data da Aquisicao: ',row[3])
        print('\n')

    new_sql="""
    UPDATE tb_carros
    SET preco = %s, 
    km=%s, 
    data_de_aq=%s
    WHERE placa = 'gust188'
    """

    new_preco=input("Preco do carro: ")
    new_km=input("Quilometragem do carro: ")
    new_data_de_aq=input("Data de compra do veiculo (aaaa-mm-dd): ")
    new_tupla=(new_preco, new_km, new_data_de_aq)
    cursor.execute(new_sql, new_tupla)
    conexao.commit()
    sql_deletando="""
    delete
    from tb_carros
    where placa = 'gust188' """

    cursor.execute(sql_deletando)
    conexao.commit()
    cursor.close()
    fechando_conexao(conexao)


    
    
    
    