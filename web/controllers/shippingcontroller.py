import os
import threading
from web.app import app

sem = threading.Semaphore()

@app.route('/shipping/deploy', methods=["GET", "POST"])
def shipping_deploy():
    sem.acquire()
    os.system('cd /opt/shipping/'
              # ' && mkdir /opt/deployagent/logs'
              ' && git pull >> /opt/deployagent/logs/shipping.txt'
              ' && systemctl restart shipping.service >> /opt/deployagent/logs/shipping.txt'
              ' && systemctl status shipping.service >> /opt/deployagent/logs/shipping.txt')
    sem.release()
    return '1'
