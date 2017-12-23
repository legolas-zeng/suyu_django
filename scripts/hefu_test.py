# -*-coding:utf-8 -*-
import os
import codecs
import sys
import time
import requests
import json

HEFU_BASE_PATH = "F:\django_test\media"
log_file_name = "hefu_log_%s.txt" % time.strftime('%Y%m%d-%H', time.localtime(time.time()))

def save_hefu_log(log_str, is_show=True):
    log_file_path = os.path.join(HEFU_BASE_PATH, log_file_name)
    with codecs.open(log_file_path, 'a', 'utf-8') as f:
        f.write("%s\t%s\r\n" % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), log_str))

def check_host_port_is_open():
    time.sleep(2)
    save_hefu_log(u"success")
    post_info(pro=1,status='success')
    print 1

def check_hefu(pro=2):
    time.sleep(2)
    save_hefu_log(u"success")
    post_info(pro=2, status='success')
    print 2

def _backup_db():
    time.sleep(2)
    save_hefu_log(u"success")
    post_info(pro=3, status='success')
    print 3
    
def backup_databases():
    time.sleep(2)
    save_hefu_log(u"success")
    post_info(pro=4, status='success')
    print 4
    
def run_hefu():
    save_hefu_log(u"执行合服脚本成功")
    # save_hefu_log(u"执行合服脚本失败")
def post_info(pro,status):
    hefu_id = '539' #
    info = {
        'pro':pro,
        'status':status,
        'hefu_id':hefu_id
    }
    data = json.dumps(info)
    print data
    r = requests.post('http://192.168.2.120/Hefu_Progress_Api', data=data)
    print r.status_code

if __name__ == '__main__':
    check_host_port_is_open()
    check_hefu()
    _backup_db()
    backup_databases()
    save_hefu_log(u"合服成功")
    save_hefu_log(u"========运行脚本 结束=============", is_show=False)

