#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author : JasonChen
# Email  : 4487802902@qq.com
# Date   : 2017/1/6
# Readme : GM后台数据库操作


from database import CDataBase
import time
from tmsy.constant import DB_INFO, COUNTRY_LIST
from tmsy.db import get_host_list
import json



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

    def get_server_list(self):
        sql = "select app, app_id, platform, area, server, merge, `show`, prefix, name, status, DATE_FORMAT(sertime,'%%Y-%%m-%%d %%H:%%i:%%S') as sertime, ip, white, is_open "
        sql += "from game_servers where game=%s order by app, platform, `area`+0, `show`+0"

        # print sql
        ret = self._conn.select_sql(sql, (self._game, ))
        server_list = {}
        platform_list = {}
        ip_list = {}
        area_dict = self.get_area_list()
        host_list = get_host_list()
        for line in ret:
            platform = line['platform']
            show = int(line['show'])
            app = line['app']
            area_id = line['area']
            if area_id in area_dict.keys():
                line['area'] = area_dict.get(area_id).get('name')
            else:
                line['area'] = 'N/A'
            ip_port = line['ip'].split(':')
            if len(ip_port) == 2:
                ip, port = ip_port
            else:
                ip = ip_port[0]
                port = 'N/A'
            line['ip'] = ip
            line['port'] = port
            line['lanip'] = ip
            host_info = host_list.get(ip, None)
            if host_info:
                line['lanip'] = host_info.hostLanIp

            if app not in ip_list.keys():
                ip_list[app] = []
            if ip and ip not in ip_list[app]:
                ip_list[app].append(ip)
            if app not in platform_list.keys():
                platform_list[app] = []
            if platform and platform not in platform_list[app]:
                platform_list[app].append(platform)
            if app not in server_list.keys():
                server_list[app] = {}
            if platform and platform not in server_list[app].keys():
                server_list[app][platform] = []
            server_list[app][platform].append(line)
        return platform_list, server_list, ip_list

    def get_open_server_list(self, state, sDate, eDate):
        open_sDate = sDate + ' 00:00:00'
        open_eDate = eDate + ' 23:59:59'
        sql = "select id, platform, server, server_id, prefix, name, open_date, apply_date, state from server_apply"
        sql += " where game='%s' and ((open_date>='%s' and open_date<='%s') or (apply_date>='%s' and apply_date<='%s'))" % (self._game, open_sDate, open_eDate, open_sDate, open_eDate)
        if state > 0:
            sql += " and state=%s" % state
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



