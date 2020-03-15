import os
import threading
from web.app import app

sem = threading.Semaphore()


@app.route('/deployagent/deploy', methods=["GET", "POST"])
def deployagent_deploy():
    sem.acquire()
    build = os.popen('cd /opt/deployagent/'
              # ' && mkdir /opt/deployagent/logs'
              ' && git pull'
              ' && systemctl restart deployagent.service'
              ' && systemctl status deployagent.service').read()
    sem.release()
    return "<br />".join(build.split("\n"))
