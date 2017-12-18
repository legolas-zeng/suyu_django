from django.conf.urls import include, url
from . import views,function
from suyusys import views as sviews
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
 
 # about run command urls
 url(r'^command\_page$',command_page, name='command_page'),
 url(r'^command\_run$',command_run, name='command_run'),
 url(r'^saltmodule_deploy\.html',saltmodule),
 url(r'minion/softinstall/',SoftInstall,name='SoftInstall'),
 
 # about redis
 url(r'^redisreport',views.redisreport, name='redisreport'),
 url(r'^newindex',sviews.newindex),
 url(r'^redis-info',sviews.redis_info),
 url(r'^echart_redis/$',sviews.echart_redis),
 url(r'^api/apichartredis/$',sviews.Api_echart_redis),
 
 # about sususys
 url(r'^globa_setting', sviews.globa_setting),
 url(r'^Notifications', sviews.Notifications),
 url(r'^hefu_game_plan', sviews.hefu_game),
 url(r'^File_upload', sviews.file_upload),
 url(r'^hefu_input', sviews.hefu_input),
 url(r'^hefu_progress', sviews.hefu_progress),
 url(r'^hefu_progress_api', sviews.hefu_progress_api),
]
urlpatterns += staticfiles_urlpatterns()
