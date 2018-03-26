#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author : JasonChen
# Email  : 4487802902@qq.com
# Date   : 2017/1/6
# Readme : GM后台数据库操作


from database import CDataBase
import time,json
from scripts.constant import DB_INFO,COUNTRY_LIST
from django.db.models import Aggregate, CharField


# TODO 聚合查询功能
class GroupConcat(Aggregate):          # Aggregate的子类
    # supports COUNT(distinct field)
    function = 'GROUP_CONCAT'
    template = '%(function)s(%(distinct)s%(expressions)s)'
    def __init__(self, expression, distinct=False,ordering=None,separator=',', **extra):
        super(GroupConcat, self).__init__(
            expression,
            distinct='DISTINCT ' if distinct else '',
            ordering=' ORDER BY %s' %ordering if ordering is not None else '',
            separator=' SEPARATOR "%s"' % separator,
            output_field=CharField(),
            **extra)

class GmDB(object):
    def __init__(self, db_key):
        self._db_info = DB_INFO.get(db_key)
        self._country, self.app = db_key.split('_')
        self._country_info = COUNTRY_LIST.get(self._country)
        self._game = self._country_info.get('game')
        self._conn = self.db_conn()
        if self._country in ['china', 'golden', 'kuaiyou', 'miaole', 'xxqy', '6kw', 'chuangxing']:
            self._conn._cursor.execute('SET NAMES utf8')
    def db_conn(self):
        conn = CDataBase(self._db_info['host'], self._db_info['user'], self._db_info['pwd'],
                         self._db_info['dbname'], self._db_info['port'])
        return conn

    def get_platform_list(self, app):
        sql = "select platform from game_servers where game=%s and app=%s group by platform "
        ret = self._conn.select_sql(sql, (self._game, app))
        return ret


    def get_area_list(self):
        sql = "select id, name, game, platform from area where game = %s"
        ret = self._conn.select_sql(sql, (self._game,))
        area_dict = {}
        for line in ret:
            area_id = line['id']
            area_dict[area_id] = line
        return area_dict


    def get_open_server_list(self, state, sDate, eDate):
        open_sDate = sDate + ' 00:00:00'
        open_eDate = eDate + ' 23:59:59'
        sql = "select id, platform, server, server_id, prefix, name, open_date, apply_date, state from server_apply"
        sql += " where game='%s' and ((open_date>='%s' and open_date<='%s') or (apply_date>='%s' and apply_date<='%s'))" % (self._game, open_sDate, open_eDate, open_sDate, open_eDate)
        if state > 0:
            sql += " and state=%s" % state
        ret = self._conn.select_sql(sql, ())
        return ret
    
    # TODO 工单查询
    def get_open_server_count(self):
        sql = "select count(0) from server_apply where game='%s' and state=1"%self._game
        ret = self._conn.select_sql(sql,())
        return ret
    def get_hefu_server_count(self):
        sql = "select count(0) from server_combine where game='%s' and status=1"%self._game
        ret =self._conn.select_sql(sql,())
        return ret
    def get_open_server_notify(self):
        sql = "select game,count(1) count from server_apply where state=1 GROUP BY game"
        ret = self._conn.select_sql(sql,())
        return ret
    def get_hefu_notify(self):
        sql = "select game,count(1) count from server_combine where status=1 GROUP BY game"
        ret = self._conn.select_sql(sql,())
        return ret
    # TODO 区服列表查询
    def get_game_server(self):
        sql = "select area,count(1),concat(GROUP_CONCAT(name order by id separator '\"\,\"')) as 'result' from game_servers where game='%s' GROUP BY area"%self._game
        ret = self._conn.select_sql(sql, ())
        return ret

    # TODO area 名字
    def ger_platfrom(self,area_id):
        sql = "select name from area where id = '%s'"%area_id
        ret = self._conn.select_sql(sql, ())
        return ret
    
    
    
    def get_hefu_server_list(self, status, sDate, eDate):
        open_sDate = sDate + ' 00:00:00'
        open_eDate = eDate + ' 23:59:59'
        sql = "select id, platform, area, server_id, server_ids, apply_time, status, combine_time from server_combine"
        sql += " where game='%s' and ((apply_time>='%s' and apply_time<='%s') or (combine_time>='%s' and combine_time<='%s'))" % (self._game, open_sDate, open_eDate, open_sDate, open_eDate)
        if status > 0:
            sql += " and status=%s" % status
        ret = self._conn.select_sql(sql, ())
        return ret


if __name__ == '__main__':
    db = GmDB('china_gmdb')
    print db.get_open_server_list(2, '2017-06-22', '2017-06-23')



