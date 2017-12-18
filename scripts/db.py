#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author : JasonChen
# Email  : 4487802902@qq.com
# Date   : 2017/3/1
# Readme :

from models import JsonInfo, Hosts
import json


# 获取主机信息
def get_host_list():
    try:
        host_list = Hosts.objects.all()
    except:
        host_list = None
    host_new_dict = {}
    if host_list:
        for host in host_list:
            wanip = host.hostWanIp
            host_new_dict[wanip] = host
    return host_new_dict


def get_json_info(country):
    try:
        json_info = JsonInfo.objects.get(country=country)
    except:
        json_info = None
    return json_info

def save_json_info(country, channel_list, server_list, ip_list):
    json_info = get_json_info(country)
    if json_info:
        json_info.jsonChannelList = channel_list
        json_info.jsonServerList = server_list
        json_info.jsonIpList = ip_list
        json_info.save()
    else:
        json_info = JsonInfo(
            country=country,
            jsonChannelList=channel_list,
            jsonServerList=server_list,
            jsonIpList=ip_list
        )
        json_info.save()
    return json_info


def get_server_list_json(country, app, channel=None, isprefix=False, ip=None):
    list_json = {}
    json_info = get_json_info(country)
    if not json_info:
        return list_json
    server_dict = json.loads(json_info.jsonServerList)
    server_list = []
    if not app:
        return {}
    server_dict = server_dict.get(app, {})
    if not server_dict:
        return {}
    if channel:
        server_list = server_dict.get(channel, [])
    else:
        for k in server_dict.values():
            server_list.extend(k)

    for server in server_list:
        serverid = server['server']
        merge = server['merge']
        serverip = server['ip']
        if serverid != merge:
            continue
        if ip and ip != serverip:
            continue
        servershow = int(server['show'])
        serverprefix = server['prefix']
        area = server['area']
        servername = server['name']
        serverlanip = server['lanip']
        serverport = server['port']
        game_channel = server['platform']
        white = server['white']
        is_open = server['is_open']

        # if game_channel in ['inside'] or serverip in ['120.76.29.83', '192.168.1.45']:
        #     continue
        if serverprefix and isprefix:
            showname = "%s%s" % (serverprefix, servershow)
        else:
            showname = servershow
        if game_channel not in list_json.keys():
            list_json[game_channel] = {}
        if area not in list_json[game_channel].keys():
            list_json[game_channel][area] = []

        list_json[game_channel][area].append({'serverid': str(serverid), 'ip': serverip, 'port': serverport,
                                             'name': servername,
                                             'channel': game_channel, 'prefix': serverprefix, 'show': servershow,
                                             'white': white,
                                             'is_open': is_open, 'serverlanip': serverlanip})
    return list_json


# 获取区服列表详细信息，返回以serverid为key的字典
def get_serverid_info_list_json(country, app, return_serverid=None, show_hefu=False):
    list_json = {}
    json_info = get_json_info(country)
    if not json_info:
        return list_json
    server_dict = json.loads(json_info.jsonServerList)
    server_list = []
    if not app:
        return {}
    server_dict = server_dict.get(app, {})
    if not server_dict:
        return {}

    for k in server_dict.values():
        server_list.extend(k)

    for server in server_list:
        serverid = server['server']
        merge = server['merge']
        if not show_hefu and serverid != merge:
            continue
        if return_serverid and str(serverid) != return_serverid:
            continue
        servershow = int(server['show'])
        serverprefix = server['prefix']
        area = server['area']
        servername = server['name']
        serverip = server['ip']
        serverlanip = server['lanip']
        serverport = server['port']
        game_channel = server['platform']
        white = server['white']
        is_open = server['is_open']
        status = server['status']

        list_json[str(serverid)] = {'serverid': str(serverid), 'ip': serverip, 'port': serverport,
                                             'name': servername, 'area': area, 'merge': merge,
                                             'channel': game_channel, 'prefix': serverprefix, 'show': servershow,
                                             'white': white, 'status': status,
                                             'is_open': is_open, 'serverlanip': serverlanip}
    return list_json

# 返回serverid对应区服名字
def get_serverId_list_json(country, app):
    list_dict = {}
    json_info = get_json_info(country)
    if not json_info:
        return list_dict
    server_dict = json.loads(json_info.jsonServerList)
    if not app:
        return {}
    server_dict = server_dict.get(app, {})
    server_list = []
    for k in server_dict.values():
        server_list.extend(k)
    for server in server_list:
        serverid = server['server']
        merge = server['merge']
        if serverid != merge:
            continue
        servershow = int(server['show'])
        serverprefix = server['prefix']
        game_channel = server['platform']
        servername = server['name']

        if serverid not in list_dict.keys():
            list_dict[serverid] = "%s___%s%s___%s" % (game_channel, serverprefix, servershow, servername)
    return list_dict

def get_ip_serverlist(server_dict):
    ip_dict = {}
    zone_count = 0
    for key, value in server_dict.items():
        for server in value:
            serverid = server['server']
            merge = server['merge']
            if serverid != merge:
                continue
            servername = server['name']
            servershow = int(server['show'])
            serverprefix = server['prefix']
            channel = key
            ip = server['ip']
            if ip not in ip_dict.keys():
                ip_dict[ip] = []
            show_str = u"%s[%s%s_%s](%s)" % (channel, serverprefix, servershow, servername, serverid)
            data = {'serverid': serverid, 'name': servername, 'show': servershow, 'prefix': serverprefix, 'channel': channel}
            ip_dict[ip].append(data)
            zone_count += 1
    return zone_count, ip_dict