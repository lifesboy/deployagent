import os
import threading
from web.app import app

sem = threading.Semaphore()

@app.route('/mt4-interface/deploy', methods=["GET", "POST"])
def mt4interface_deploy():
    sem.acquire()
    build = os.popen('cd /opt/mt4-interface/'
              #' && mkdir /opt/deployagent/logs'
              ' && git pull'
              ' && npm install'
              ' && pm2 start ecosystem.config.js --env development-3100').read()
    sem.release()
    return build
