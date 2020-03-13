# deployagent

Simple deploy agent to setup auto CI/CD.

  - Installation
  - Setup git webhook
  - Setup deploy environment

### Installation

Requires [Python](https://python.org/) to run.

Install webservice:
```sh
$ apt-get install uwsgi -y
$ apt-get install uwsgi-plugin-python -y
```

Clone source to: /opt/deployagent.
```sh
$ git clone -b release https://github.com/lifesboy/deployagent.git /opt/deployagent
```

Install deployagent service
```sh
$ sudo cp /opt/deployagent/deployagent.service /etc/systemd/system/deployagent.service
$ sudo chmod 644 /etc/systemd/system/deployagent.service
$ sudo systemctl start deployagent
$ sudo systemctl status deployagent
```

Intergrate deployagent service if server is running nginx
```sh
$ sudo cp /opt/deployagent/nginx/sites-available/deployagent /etc/nginx/sites-available/
$ sudo ln -s /etc/nginx/sites-available/deployagent /etc/nginx/sites-enabled/deployagent
$ sudo systemctl restart nginx.service
```

If you use HTTPS git repos, try manually pull for first time, and enable long cache to by pass inputing password
```sh
$ git config --global credential.helper cache
$ git config --global credential.helper 'cache --timeout=2592000'
```