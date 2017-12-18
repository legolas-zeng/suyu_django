#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author : JasonChen
# Email  : 4487802902@qq.com
# Date   : 2016/11/14
# Readme : 变量定义

# 中心服、后台数据库信息
COUNTRY_LIST = {
    'china': {'name': u'国服', 'app': ['s1', 's2'], 'gm_url': 'http://tmldgm.suyutech.com', 'gm_key': 'AKJDF22308SJAL$#!Alj239', 'game': 'sgzs'},
    'vietnam': {'name': u'越南', 'app': ['s1'], 'gm_url': 'http://35.194.140.254', 'gm_key': 'AKJDF22308SJAL$#!Alj239', 'game': 'sgzs'},
    'tmldyn': {'name': u'越南唐门', 'app': ['s1'], 'gm_url': 'http://35.194.228.69','gm_key': 'AKJDF22308SJAL$#!Alj239', 'game': 'tmld_yuenan'},
    'golden': {'name': u'辉耀', 'app': ['s1'], 'gm_url': 'http://tmldgm.suyutech.com', 'gm_key': 'AKJDF22308SJAL$#!Alj239', 'game': 'tmld2'},
    # 'hongkong': {'name': u'港澳台', 'app': ['s1'], 'gm_url': 'http://128.1.63.13', 'gm_key': 'AKJDF22308SJAL$#!Alj239', 'game': 'zshh_hk'},
    'kuaiyou': {'name': u'快游', 'app': ['s1'], 'gm_url': 'http://tmldgm.suyutech.com', 'gm_key': 'AKJDF22308SJAL$#!Alj239', 'game': 'tmld_ky'},
    'miaole': {'name': u'秒乐', 'app': ['s1'], 'gm_url': 'http://tmldgm.suyutech.com', 'gm_key': 'AKJDF22308SJAL$#!Alj239', 'game': 'sgzs_ml'},
    'xxqy': {'name': u'仙侠情缘', 'app': ['s1'], 'gm_url': 'http://tmldgm.suyutech.com', 'gm_key': 'AKJDF22308SJAL$#!Alj239', 'game': 'tmld_xxqy'},
    '6kw': {'name': u'6kw', 'app': ['s1'], 'gm_url': 'http://tmldgm.suyutech.com', 'gm_key': 'AKJDF22308SJAL$#!Alj239', 'game': 'tmld_6k'},
    'chuangxing': {'name': u'创星', 'app': ['s1'], 'gm_url': 'http://tmldgm.suyutech.com', 'gm_key': 'AKJDF22308SJAL$#!Alj239', 'game': 'tmld_cx'},
}

# 正式数据库信息
DB_INFO = {
    'china_s1': {'host': '120.76.29.83', 'user': 'root', 'pwd': 's!*090_Db', 'dbname': 's1tool', 'port': 3306},
    'china_s2': {'host': '118.89.31.220', 'user': 'ops', 'pwd': 'sk21ikEklelisk12', 'dbname': 's1tool', 'port': 3306},
    'china_gmdb': {'host': '120.25.78.172', 'user': 'tmldgm', 'pwd': 'tmldgm_dbpwd_2016', 'dbname': 'tmldgm', 'port': 3306},

    'vietnam_s1': {'host': '35.194.140.254', 'user': 'ops', 'pwd': 'sk21ikEklelisk12', 'dbname': 's1tool', 'port': 3306},
    'vietnam_gmdb': {'host': '35.194.140.254', 'user': 'ops', 'pwd': 'sk21ikEklelisk12', 'dbname': 'tmldgm', 'port': 3306},

    'tmldyn_s1': {'host': '35.194.228.69', 'user': 'ops', 'pwd': 'sk21ikEklelisk12', 'dbname': 's1tool', 'port': 3306},
    'tmldyn_gmdb': {'host': '35.194.228.69', 'user': 'ops', 'pwd': 'sk21ikEklelisk12', 'dbname': 'tmldgm', 'port': 3306},

    'golden_s1': {'host': '139.199.155.17', 'user': 'ops', 'pwd': 'sk21ikEklelisk12', 'dbname': 's1tool', 'port': 3306},
    'golden_gmdb': {'host': '120.25.78.172', 'user': 'tmldgm', 'pwd': 'tmldgm_dbpwd_2016', 'dbname': 'tmldgm', 'port': 3306},

    # 'hongkong_s1': {'host': '128.1.63.13', 'user': 'ops', 'pwd': 'sk21ikEklelisk12', 'dbname': 's1tool', 'port': 3306},
    # 'hongkong_gmdb': {'host': '128.1.63.13', 'user': 'ops', 'pwd': 'sk21ikEklelisk12', 'dbname': 'tmldgm', 'port': 3306},

    'kuaiyou_s1': {'host': '123.207.228.208', 'user': 'ops', 'pwd': 'sk21ikEklelisk12', 'dbname': 's1tool', 'port': 3306},
    'kuaiyou_gmdb': {'host': '120.25.78.172', 'user': 'tmldgm', 'pwd': 'tmldgm_dbpwd_2016', 'dbname': 'tmldgm', 'port': 3306},

    'miaole_s1': {'host': '139.199.1.175', 'user': 'ops', 'pwd': 'sk21ikEklelisk12', 'dbname': 's1tool', 'port': 3306},
    'miaole_gmdb': {'host': '120.25.78.172', 'user': 'tmldgm', 'pwd': 'tmldgm_dbpwd_2016', 'dbname': 'tmldgm', 'port': 3306},

    'xxqy_s1': {'host': '106.75.156.219', 'user': 'ops', 'pwd': 'sk21ikEklelisk12', 'dbname': 's1tool', 'port': 3306},
    'xxqy_gmdb': {'host': '120.25.78.172', 'user': 'tmldgm', 'pwd': 'tmldgm_dbpwd_2016', 'dbname': 'tmldgm', 'port': 3306},

    '6kw_s1': {'host': '122.152.198.11', 'user': 'ops', 'pwd': 'sk21ikEklelisk12', 'dbname': 's1tool', 'port': 3306},
    '6kw_gmdb': {'host': '120.25.78.172', 'user': 'tmldgm', 'pwd': 'tmldgm_dbpwd_2016', 'dbname': 'tmldgm', 'port': 3306},

    'chuangxing_s1': {'host': '139.199.85.14', 'user': 'ops', 'pwd': 'sk21ikEklelisk12', 'dbname': 's1tool', 'port': 3306},
    'chuangxing_gmdb': {'host': '120.25.78.172', 'user': 'tmldgm', 'pwd': 'tmldgm_dbpwd_2016', 'dbname': 'tmldgm', 'port': 3306},
}

# 本地测试数据库信息
# DB_INFO = {
#     'china_s1': {'host': 'localhost', 'user': 'root', 'pwd': '', 'dbname': 's1tool', 'port': 3306},
#     'china_s2': {'host': 'localhost', 'user': 'root', 'pwd': '', 'dbname': 's2tool', 'port': 3306},
#     'china_gmdb': {'host': '120.25.78.172', 'user': 'tmldgm', 'pwd': 'tmldgm_dbpwd_2016', 'dbname': 'tmldgm', 'port': 3306},
#     'vietnam_s1': {'host': 'localhost', 'user': 'root', 'pwd': '', 'dbname': 'vietnam_s1tool', 'port': 3306},
#     'vietnam_gmdb': {'host': '35.185.157.56', 'user': 'ops', 'pwd': 'sk21ikEklelisk12', 'dbname': 'tmldgm', 'port': 3306}
# }

# 游戏服数据库信息
GAME_DB_INFO = {
    'user': 'ops',
    'pwd': 'sk21ikEklelisk12',
    'port': 3306
}

# API接口KEY
OMS_API_KEY = 'addserverkey#kfi789i1!'

# 加载活动接口KEy
LOAD_ACTIVITY_KEY = 'loadactivityKEjksk^j3k'

# SQL语句执行限制
SQL_LIMIT_LIST = ['DROP', 'DELETE', 'TRUNCATE', 'GRANT', 'FLUSH']

# 调用GM后台接口功能列表
GM_MODULE = [
    {'action': 'open_white', 'name': '开启白名单', 'ArgvCount': 0},
    {'action': 'close_white', 'name': '关闭白名单', 'ArgvCount': 0},
    {'action': 'run_gm_cmd', 'name': '踢全部玩家下线', 'cmd': 'kick', 'ArgvCount': 0},
    {'action': 'stop_server', 'name': '停止游戏区服', 'ArgvCount': 0},
    {'action': 'start_server', 'name': '启动游戏区服', 'ArgvCount': 0},
    {'action': 'run_gm_cmd', 'name': '热加载：rsf', 'cmd': 'rsf', 'ArgvCount': 0},
]



