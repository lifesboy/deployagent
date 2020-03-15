import os
import threading
from web.app import app

sem = threading.Semaphore()

@app.route('/webforexweb/deploy', methods=["GET", "POST"])
def webforexweb_deploy():
    sem.acquire()
    build = os.popen('cd /opt/web/'
              # ' && mkdir /opt/deployagent/logs'
              ' && git pull && git status'
              ' && npm install'
              ' && nnpm run build_sharectv'
              #' && mkdir /var/www/html/web'
              ' && rm -rfv /var/www/html/web/*'
              ' && cp -Rv /opt/web/dist/web/* /var/www/html/web/').read()
    sem.release()
    return "<br />".join(build.split("\n"))
