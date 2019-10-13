import os

from web.app import app


@app.route('/deployagent/deploy')
def data_list():
    os.system('cd /opt/deployagent/'
              # ' && mkdir /opt/deployagent/logs'
              ' && git pull >> /opt/deployagent/logs/deployagent.txt'
              ' && systemctl restart deployagent.service >> /opt/deployagent/logs/deployagent.txt'
              ' && systemctl status deployagent.service >> /opt/deployagent/logs/deployagent.txt')
    return '1'
