# -*-coding:utf-8 -*-
from celery import task,shared_task
import time

@task
def celery_task():
	time.sleep(5)
	print("success test tasks......")
