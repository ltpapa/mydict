#!/usr/bin/evn python
#coding:utf-8

import dbapi

class Module:
    '''MVC mode module'''
    def __init__(self,dbfile):
        self.init(dbfile)

    def init(self,dbfile):
        create_table_sql = '''CREATE TABLE `known` (
                            `word` varchar(20) NOT NULL,
                            `chinese` varchar(2048) DEFAULT NULL,
                            `english` varchar(2048) DEFAULT NULL,
                            `category` int(11) DEFAULT NULL,
                            PRIMARY KEY (`word`)
                            )'''
        self.conn = dbapi.get_conn(dbfile)
        dbapi.create_table(conn, create_table_sql)

    def insert_a_new_word(self,word):
        sql = '''INSERT INTO known values (?, ?, ?, ?)'''
        data = [(word['name'],word['chinese'],word['englist'],word['category'])]
        dbapi.save(self.conn,save_sql,data)

    def insert_words(self,words):
        sql = '''INSERT INTO known values (?, ?, ?, ?)'''
        dbapi.save(self.conn,save_sql,words)

    def is_a_word_indb(self,word):
        sql = 'SELECT * FROM student WHERE word = ? '
        if None == fetchone(self.conn, sql, word):
            return False
        else:
            return True

