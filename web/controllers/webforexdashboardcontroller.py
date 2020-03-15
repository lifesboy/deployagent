import os
import threading
from web.app import app

sem = threading.Semaphore()

@app.route('/webforexdashboard/deploy', methods=["GET", "POST"])
def webforexdashboard_deploy():
    sem.acquire()
    build = os.popen('cd /opt/dashboard/'
              # ' && mkdir /opt/deployagent/logs'
              ' && git pull && git status'
              ' && npm install'
              ' && npm run build_sharectv'
              #' && mkdir /var/www/html/web'
              ' && rm -rfv /var/www/html/dashboard/*'
              ' && cp -Rv /opt/web/dist/dashboard/* /var/www/html/dashboard/').read()
    sem.release()
    return "<br />".join(build.split("\n"))
