# from gevent import monkey
#
# monkey.patch_all()

import multiprocessing

bind = "0.0.0.0:5000"

#超时
timeout = 30

#指定每个进程开启的线程数
thread = 2

# 启动的进程数
# workers = multiprocessing.cpu_count()
workers = 5
# worker_class = 'gevent'

#