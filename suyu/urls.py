from django.conf.urls import include, url
from . import views,function
from suyusys import views as sviews
from NewGames import views as ssviews
from search import views as sv
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
from saltstack.views import *

# import silver_fox
# from silver_fox import views as sviews
urlpatterns = [
 #url(r'^test$',views.base,name='test'),
 url(r'^$',views.index,name='index'),
 url(r'^login$', views.login, name='login'),
 url(r'^apireport$',views.apireport,name='apireport'),
 url(r'^hostlistinfo$',views.hostlistinfo,name='hostlistinfo'),
 url(r'^api/chart$',views.apichart,name='apichart'),
 url(r'^api/men$',views.apimen,name='apimen'),
 url(r'^chart$',views.chart,name='chart'),
 url(r'^bad$',views.bad,name='bad'),
 url(r'^test$',views.test,name='test'),
 url(r'^test\_6\.html$',views.test_6,name='test_6'),
 url(r'^test\_5\.html$',views.test_5,name='test_5'),
 url(r'^test\_4\.html$',views.test_4,name='test_4'),
 url(r'^test\_3$',views.test_3,name='test_3'),
 url(r'^test\_2$',views.test_2,name='test_2'),
 url(r'^test\_2\_api$',views.test_2_api,name='test_2_api'),
 url(r'^server\_upload$',views.server_upload,name='server_upload'),
 url(r'^uploadsave$', views.uploadsave, name='uploadsave'),
 url(r'^upload\_list$', views.upload_list, name='upload_list'),
 url(r'^upload\_del$', views.upload_del, name='upload_del'),
 
 # about salt
 url(r'^command\_page$',command_page, name='command_page'),
 url(r'^command\_run$',command_run, name='command_run'),
 url(r'^saltmodule_deploy\.html',saltmodule),
 url(r'^minion/softinstall/',SoftInstall,name='SoftInstall'),
 url(r'^salt_tem_api$',sviews.salt_tem_api,name='salt_tem_api'),
 
 # about redis
 url(r'^redisreport',views.redisreport, name='redisreport'),
 url(r'^redis-info',sviews.redis_info, name='redis-info'),
 url(r'^echart_redis/$',sviews.echart_redis),
 url(r'^api/apichartredis/$',sviews.Api_echart_redis),
 
 # about suyusys
 url(r'^newindex',sviews.newindex,name='newindex'),
 url(r'^reindex',sviews.reindex,name='reindex'),
 url(r'^globa_setting', sviews.globa_setting),
 url(r'^Notifications', sviews.Notifications),
 url(r'^File_upload', sviews.file_upload),
 url(r'^file_preview', sviews.file_preview,name='file_preview'),
 url(r'^ip_search$', sv.ip_search, name='ip_search'),
 #url(r'^action_search/(\d+)',include('suyusys.urls',namespace='suyusys')),
 url(r'^action_search',include('suyusys.urls')),
 #url(r'^action_search/(?P<key_word>\S+)', sv.action_search, name='action_search'),
 url(r'^Host_list', sviews.Host_list, name='Host_list'),
 url(r'^alter_host_status_api', sviews.alter_host_status_api, name='alter_host_status_api'),
 url(r'Host_info',sviews.Host_info,name='Host_info'),
 url(r'^new_login$', sviews.new_login, name='new_login'),
 url(r'^login_out', sviews.login_out, name='login_out'),
 
 # about hefu
 url(r'^HefuInput', sviews.HefuInput),
 url(r'^HefuProgress', sviews.HefuProgress),
 url(r'^Hefu_Progress_Api', sviews.HefuProgressApi),
 url(r'^Hefu_Progress_Search', sviews.HefuProgressSearch,name='HefuProgressSearch'),
 url(r'^hefu_log_api', sviews.hefu_log_api,name='hefu_log_api'),
 url(r'^hefu_game_plan\.jsp', sviews.hefu_game, name='hefu_game_plan'),
 url(r'^HefuServerPlanView', sviews.HefuServerPlanView, name='HefuServerPlanView'),
 
 # about server_list
 url(r'^server_list', sviews.server_list, name='server_list'),
 

 # about game
 url(r'^game_action', sviews.game_action, name='game_action'),
 
 # about install
 url(r'^new_game_plan', ssviews.newgameplan, name='new_game_plan'),
 url(r'^new_game_progress', ssviews.new_game_progress, name='new_game_progress'),
 url(r'^new_game_api', ssviews.new_game_api, name='new_game_api'),
 
 
 
]
urlpatterns += staticfiles_urlpatterns()
