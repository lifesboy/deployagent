import os

from web.app import app


@app.route('/shipweb/deploy', methods=["GET", "POST"])
def shipweb_deploy():
    os.system('cd /opt/shipweb-src/'
              # ' && mkdir /opt/deployagent/logs'
              ' && git pull >> /opt/deployagent/logs/shipweb.txt'
              ' && rm -rfv /opt/shipweb/* >> /opt/deployagent/logs/shipweb.txt'
              ' && cp -Rv /opt/shipweb-src/release/* /opt/shipweb/ >> /opt/deployagent/logs/shipweb.txt')
    return '1'
