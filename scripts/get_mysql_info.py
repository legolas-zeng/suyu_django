# -*-coding:utf-8 -*-import MySQLdbimport sysimport ossubordinate_1_ip = '172.17.0.2'Main_Log_File = ''subordinate_info = 'show subordinate status'main_info = 'show main status'Subordinate_heartbeat_period = "show status like 'Subordinate_heartbeat_period'"Subordinate_received_heartbeats = "show status like 'Subordinate_received_heartbeats'"que_sql = "SHOW GLOBAL STATUS LIKE 'Questions'"IoS = ''SqS = ''Sec = ''class get_subordinate_info():	def __init__(self):		#self.conn = MySQLdb.connect(host='192.168.28.132', user='ops', passwd='123456abc',port=3306, charset='utf8')		self.conn = MySQLdb.connect(host='172.17.0.2', user='ops',passwd='123456abc', port=3306, charset='utf8')		#self.conn = MySQLdb.connect(host='127.0.0.1', user='root', port=3306, charset='utf8')		self.cur = self.conn.cursor()	def judge_subordinate(self,command):		global IoS		global SqS		global Sec		try:			self.cur.execute(command)			for n in self.cur.fetchall():				print n				IoS = n[10]				SqS = n[11]				Sec = n[32]			if IoS == 'Yes' and SqS == 'Yes' :				print 'subordinate is running'			else:				print 'subordinate is stop'			# self.cur.close()			# self.conn.close()		except MySQLdb.Error, e:			print "MySQLdb Error", e	def question(self,command):		self.cur.execute(command)		for n in self.cur.fetchall():			print n[1]	def judge_main(self):		passif __name__ == '__main__':	a = get_subordinate_info()	a.judge_subordinate(subordinate_info)	a.question(que_sql)