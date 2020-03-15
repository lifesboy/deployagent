import os
import threading
from web.app import app

sem = threading.Semaphore()

@app.route('/api-interface/deploy', methods=["GET", "POST"])
def apiinterface_deploy():
    sem.acquire()
    build = os.popen('cd /opt/api-interface/'
              #' && mkdir /opt/deployagent/logs'
              ' && git pull'
              ' && npm install'
              ' && pm2 start ecosystem.config.js --env development-4100').read()
    sem.release()
    return "<br />".join(build.split("\n"))
