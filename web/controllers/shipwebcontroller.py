import os
import threading
from web.app import app

sem = threading.Semaphore()

@app.route('/shipweb/deploy', methods=["GET", "POST"])
def shipweb_deploy():
    sem.acquire()
    os.system('cd /opt/shipweb-src/'
              # ' && mkdir /opt/deployagent/logs'
              ' && git pull >> /opt/deployagent/logs/shipweb.txt'
              ' && rm -rfv /opt/shipweb/* >> /opt/deployagent/logs/shipweb.txt'
              ' && cp -Rv /opt/shipweb-src/release/* /opt/shipweb/ >> /opt/deployagent/logs/shipweb.txt')
    sem.release()
    return '1'
