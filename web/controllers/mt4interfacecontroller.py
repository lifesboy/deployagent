import os
import threading
from web.app import app

sem = threading.Semaphore()

@app.route('/mt4-interface/deploy', methods=["GET", "POST"])
def mt4interface_deploy():
    sem.acquire()
    os.system('cd /opt/mt4-interface/'
              #' && mkdir /opt/deployagent/logs'
              #' && git pull >> /opt/deployagent/logs/mt4-interface.txt'
              ' && npm install >> /opt/deployagent/logs/mt4-interface.txt'
              ' && npm run build >> /opt/deployagent/logs/mt4-interface.txt'
              ' && mkdir /var/www/html/mt4-interface >> /opt/deployagent/logs/mt4-interface.txt'
              ' && rm -rfv /var/www/html/mt4-interface/* >> /opt/deployagent/logs/mt4-interface.txt'
              ' && cp -Rv /opt/mt4-interface/dist/mt4-interface/* /var/www/html/mt4-interface/ >> /opt/deployagent/logs/mt4-interface.txt')
    sem.release()
    return '1'
