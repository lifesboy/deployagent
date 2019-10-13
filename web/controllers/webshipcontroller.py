import os

from web.app import app


@app.route('/webship/deploy')
def data_list():
    os.system('cd /opt/shipweb-src/'
              '&& git pull'
              '&& rm -rf /opt/shipweb/*'
              '&& cp -R release/* /opt/shipweb/')
    return '1'
