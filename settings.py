wsgi_app = 'hogeapp.wsgi:application'
chdir = '/usr/local/Gunicorn'

daemon = False

raw_env = [
    'ENV_TYPE=dev',
    'HOGEHOGE_KEY=xxxxxxxxxxxxxxxxxxxxxxxxx'
]

bind = '0.0.0.0:8001'

workers = 2

accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

errorlog = '-'
loglevel = 'info'
