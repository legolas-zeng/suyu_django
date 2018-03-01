# -*-coding:utf-8 -*-
import xmlrpclib

class super_api(object):
    __slots__ = ['user', 'password', 'ip', 'port']
    def __init__(self,user,password,ip,port):
        self.user = user
        self.password = password
        self.ip = ip
        self.port = port
    def ser_conn(self):
        url = 'http://' + self.user + ':' + self.password + '@' + self.ip + ':' + self.port + '/RPC2'
        conn = xmlrpclib.Server(url)
        return conn

    def conf_reload(self):
        pass

    def start_process(self,process):
        status = self.ser_conn().supervisor.startProcess(process)
        return status
    def start_process_all(self):
        pass

    def stop_process(self,process):
        status = self.ser_conn().supervisor.stopProcess(process)
        return status

    def stop_process_all(self):
        pass

    def get_info(self,process):
        info = self.ser_conn().supervisor.getProcessInfo(process)
        return info
    def get_info_all(self):
        info = self.ser_conn().supervisor.getAllProcessInfo()
        return info

    def handle_get_info_all(self):
        info = self.get_info_all()


class handle_super_api():
    def __init__(self,user, password, ip, port):
        self.a = super_api(user, password, ip, port)

    def handle_get_info_all(self,*args):
        data = self.a.get_info_all()
        send_data = []
        for info in data:
            name = info.get('name')
            state = info.get('state')
            pid = info.get('pid')
            datas = {
                'name' : name,
                'state' : state,
                'pid' : pid
            }
            send_data.append(datas)
        return send_data







