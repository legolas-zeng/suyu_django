#!/usr/bin/env python
# -*- coding=utf-8 -*-

import MySQLdb
from MySQLdb import*


class CDataBase(object):
    def __init__(self, host, user, passwd, database, port=3306):
        self._host = host
        self._user = user
        self._pwd = passwd
        self._database = database
        self._port = port
        self._connect_db()


    def _connect_db(self):
        try:
            self._conn = Connection(self._host, self._user, self._pwd, self._database, self._port,
                                    cursorclass=cursors.DictCursor)
        except MySQLdb.Error, e:
            print '[connect_db]failed.error:%s' % str(e)
            self._conn = None
            return
        self._cursor = self._conn.cursor()
        #self._cursor.execute('set autocommit=1')
        #self._cursor.execute('SET NAMES utf8')
        self._cursor.execute('SET NAMES latin1')
        #self._cursor.execute('set character_set_results = latin1')


    def __del__(self):
        if self._conn:
            self._cursor.close()
            self._conn.close()

    def update_sql(self, sql, param):
        '''执行insert、update、delete语句'''
        ret = self._cursor.execute(sql, param)
        return ret

    def exec_many_sql(self, sql, param):
        self._cursor.executemany(sql, param)
        return self._cursor.fetchall()

    def select_sql(self, sql, param):
        '''执行select语句'''
        self._cursor.execute(sql, param)
        if self._cursor.rowcount == 0:
            return ()

        return self._cursor.fetchall()
        #return self._convert_to_name()

    def _convert_to_name(self):
        records = self._cursor.fetchall()
        fields = self._get_fields()

        results = []
        for record in records:
            rec = {}
            for i in xrange(len(fields)):
                rec[fields[i]]=record[i]

            results.append(rec)

        return tuple(results)

    def _get_fields(self):
        """map indices to fieldnames"""
        if not self._cursor.description:
            return {}

        results = {}
        column = 0

        for des in self._cursor.description:
            fieldname = des[0]
            results[column] = fieldname
            column = column + 1

        return results

    def ping(self):
        try:
            _ret = self._conn.ping()
        except Exception, e:
            _ret = e

        if _ret is None:
            return True

        ## reconnect
        self.close()
        return self._connect_db()

    def close(self):
        if self._conn != None:
            self._conn.close()

        self._conn = None
        self._cursor = None


if __name__ == '__main__':
    CENTERDB_INFO = {
        'host': 'localhost',
        'user': 'root',
        'pwd': '',
        'dbname': 's1tool',
        'port': 3306
    }

    db_conn = CDataBase(CENTERDB_INFO['host'], CENTERDB_INFO['user'], CENTERDB_INFO['pwd'],
                        CENTERDB_INFO['dbname'], CENTERDB_INFO['port'])
    if db_conn._conn:
        a = db_conn.select_sql("SHOW VARIABLES LIKE '%%char%%';", ())
        for i in a:
            print i
