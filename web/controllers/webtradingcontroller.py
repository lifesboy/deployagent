import os
import threading
from web.app import app

sem = threading.Semaphore()

@app.route('/web-trading/deploy', methods=["GET", "POST"])
def webtrading_deploy():
    sem.acquire()
    os.system('cd /opt/web-trading/'
              # ' && mkdir /opt/deployagent/logs'
              #' && git pull >> /opt/deployagent/logs/web-trading.txt'
              ' && npm install >> /opt/deployagent/logs/web-trading.txt'
              ' && npm run build_sharectv >> /opt/deployagent/logs/web-trading.txt'
              ' && mkdir /var/www/html/web-trading >> /opt/deployagent/logs/web-trading.txt'
              ' && rm -rfv /var/www/html/web-trading/* >> /opt/deployagent/logs/web-trading.txt'
              ' && cp -Rv /opt/web-trading/dist/web-trading/* /var/www/html/web-trading/ >> /opt/deployagent/logs/web-trading.txt')
    sem.release()
    return '1'
