import os

bind = '127.0.0.1:8000'
workers = 5
worker_class = 'sync'
worker_connections = 1000
timeout = 1800
keepalive = 2

proc_name = 'epsilon-backend-gunicorn'
daemon = False