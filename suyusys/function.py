# -*-coding:utf-8 -*-import MySQLdbimport jsonfrom scripts.constant import DB_INFOfrom scripts.database import CDataBaseimport sysfrom suyusys.models import *from NewGames.models import *import os,djangoos.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_test.settings")# project_name 项目名称django.setup()def db_conn():	try:		db_key = 'china_gmdb'		db_info = DB_INFO.get(db_key)		conn = MySQLdb.connect(host=db_info['host'], user=db_info['user'], passwd=db_info['pwd'], db=db_info['dbname'],		                     port=db_info['port'],charset='utf8')		return conn	except MySQLdb.Error, e:		print "Mysqldb Error:%s" % eclass hefu(object):	def __init__(self,id):		self.id = id		self.game = self.hefu_info(1)		self.server_id = self.hefu_info(4)			def hefu_info(self,d):		con = db_conn()		cursor = con.cursor()		cursor.execute('select * from server_combine where id = %s',self.id)		data = cursor.fetchall()		cursor.close()		con.close()		for a in data:			b = list(a)			return b[d]		def hefu_id_info(self,*args):		con = db_conn()		cursor = con.cursor()		print self.game		print self.server_id		sql = "select * from game_servers where game='%s' and server = %s"%(self.game,self.server_id)		cursor.execute(sql)		data = cursor.fetchall()		cursor.close()		con.close()		for a in data:			if not args:				return list(a)			if list(args)[0] == 24:				return a[24][0:-5]			else:				return a[list(args)[0]]def game_info(game,app_id):	con = db_conn()	cursor = con.cursor()	sql = "select * from game_servers where game='%s' and app_id = %s"%(game,app_id)	cursor.execute(sql)	data = cursor.fetchall()	cursor.close()	con.close()	for a in data:		b = list(a)		return bdef server_apply(id):	con = db_conn()	cursor = con.cursor()	cursor.execute('select * from server_apply where gid = %s',id)	data = cursor.fetchall()	print data	cursor.close()	con.close()	for a in data:		b = list(a)		return b	# 更新游戏列表def updata_game_api():	a = game_list('tmld_ky')	req = a.game_info()	for datas in req:		game_infos = list()		game = datas[1]		app = datas[2]		app_id = datas[3]		platform = datas[4]		area = datas[5]		servers = datas[6]		show = datas[8]		merge = datas[9]		name = datas[14]		status = datas[19]		offtime = datas[20]		pretip = datas[21]		sertime = datas[22]		ip = datas[24][:-5]		white = datas[26]		is_open = datas[27]		add_time = datas[28]		game_infos.append(server(game=game,area=area,app=app,app_id=app_id,platform=platform,server=servers,show=show,merge=merge,name=name,status=status,offtime=offtime,sertime=sertime,ip=ip,white=white,is_open=is_open,add_time=add_time))		server.objects.bulk_create(game_infos)			print u"游戏更新完成"# 更新新服计划列表def updata_new_game_api():	a = new_game('84')	c = a.new_game_info()	for b in c:		game_infoss = list()		id = b[0]		game = b[1]		platform = b[2]		area = b[3]		server = b[5]		name = b[7]		open_date = b[8]		apply_date = b[9]		state = b[10]		print name, server		game_infoss.append(new_game_plan(game=game, platform=platform, areas=area, name=name, open_date=open_date, state=state,apply_date=apply_date,game_id=server,ids=id))		new_game_plan.objects.bulk_create(game_infoss)		print u'成功导入新服任务'def updata_new_platform_api():	a = new_game('84')	c = a.new_platform()	for b in c:		game_infoss = list()		id = b[0]		game = b[1]		platform = b[2]		area = b[3]		server = b[5]		name = b[7]		open_date = b[8]		apply_date = b[9]		state = b[10]		print name, server		game_infoss.append(			new_game_plan(game=game, platform=platform, areas=area, name=name, open_date=open_date, state=state,			              apply_date=apply_date, game_id=server, ids=id))		new_game_plan.objects.bulk_create(game_infoss)		print u'成功导入新服任务'		class game_list(object):	def __init__(self,game):		self.game = game	def game_info(self):		con = db_conn()		cursor = con.cursor()		data = cursor.execute('select * from game_servers where game=%s',self.game)		data = cursor.fetchall()		# info = cursor.fetchmany(data)		cursor.close()		con.close()		for a in data:			# b = list(a)			print a			print a[14]		return dataclass new_game(object):	def __init__(self,id):		self.id = id	def new_game_info(self):		con = db_conn()		cursor = con.cursor()		data = cursor.execute('select * from server_apply where area=%s', self.id)		data = cursor.fetchall()		cursor.close()		con.close()		# for info in data:		# 	print info		return data	def new_platform(self):		con = db_conn()		cursor = con.cursor()		data = cursor.execute('select * from platform_map')		data = cursor.fetchall()		cursor.close()		con.close()		return data#TODO ansible数据处理def ansible_handle(data):	req = data	data_list = {}	for k, v in req.items():		info_list = v.get('ansible_facts')		network_info = info_list.get('ansible_eth0')		disk_info = info_list.get('ansible_mounts')		men_info = info_list.get('ansible_memory_mb')		HDD_info = info_list.get('ansible_devices')				print disk_info				network = network_info.get('ipv4')		data_list['netmask'] = network.get('netmask')		data_list['network'] = network.get('network')				data_list['ipv4'] = info_list.get('ansible_all_ipv4_addresses')     # ipv4		data_list['system_version'] = info_list.get('ansible_distribution_version')  # 系统版本		data_list['hostname'] = info_list.get('ansible_hostname')           # 主机名		data_list['system'] = info_list.get('ansible_distribution')         # 系统发行版		data_list['men'] = info_list.get('ansible_memtotal_mb')             # 物理内存容量		data_list['cpu'] = info_list.get('ansible_processor')               # cpu		data_list['kernel'] = info_list.get('ansible_kernel')               # 内核		data_list['cpu_total'] = info_list.get('ansible_processor_vcpus')   # CPU核心数		print data_list	return data_list