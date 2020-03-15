import os
import threading
from web.app import app

sem = threading.Semaphore()


@app.route('/deployagent/deploy', methods=["GET", "POST"])
def deployagent_deploy():
    sem.acquire()
    os.system('cd /opt/deployagent/'
              # ' && mkdir /opt/deployagent/logs'
              ' && git pull >> /opt/deployagent/logs/deployagent.txt'
              ' && systemctl restart deployagent.service >> /opt/deployagent/logs/deployagent.txt'
              ' && systemctl status deployagent.service >> /opt/deployagent/logs/deployagent.txt')
    sem.release()
    return '1'
