import os
import threading
from web.app import app

sem = threading.Semaphore()

@app.route('/web-trading/deploy', methods=["GET", "POST"])
def shipweb_deploy():
    sem.acquire()
    os.system('cd /opt/web-trading/'
              # ' && mkdir /opt/deployagent/logs'
              ' && git pull >> /opt/deployagent/logs/holding.txt'
              ' && rm -rfv /var/www/html/web-trading/* >> /opt/deployagent/logs/holding.txt'
              ' && cp -Rv /opt/web-trading/release/* /var/www/html/web-trading/ >> /opt/deployagent/logs/holding.txt')
    sem.release()
    return '1'
