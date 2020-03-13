import os
import threading
from web.app import app

sem = threading.Semaphore()

@app.route('/web-trading/deploy', methods=["GET", "POST"])
def webtrading_deploy():
    sem.acquire()
    build = os.popen('cd /opt/web-trading/'
              # ' && mkdir /opt/deployagent/logs'
              ' && git pull'
              ' && npm installt'
              ' && npm run build_sharectv'
              ' && mkdir /var/www/html/web-trading'
              ' && rm -rfv /var/www/html/web-trading/*'
              ' && cp -Rv /opt/web-trading/dist/web-trading/* /var/www/html/web-trading/').read()
    sem.release()
    return build
