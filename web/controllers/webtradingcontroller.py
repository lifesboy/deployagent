import os
import threading
from web.app import app

sem = threading.Semaphore()

@app.route('/web-trading/deploy', methods=["GET", "POST"])
def webtrading_deploy():
    sem.acquire()
    build = os.popen('cd /opt/web-trading/'
              # ' && mkdir /opt/deployagent/logs'
              ' && git pull && git status'
              ' && npm install'
              ' && npm run build_sharectv'
              #' && mkdir /var/www/html/web-trading'
              ' && rm -rfv /var/www/html/web-trading/*'
              ' && cp -Rv /opt/web-trading/dist/web-trading/* /var/www/html/web-trading/').read()
    sem.release()
    return "<br />".join(build.split("\n"))
