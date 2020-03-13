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
