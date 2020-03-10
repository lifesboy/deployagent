# deployagent
deployagent

#setup:
1. clone source to: /opt/deployagent
git clone -b release git@github.com:lifesboy/deployagent.git /opt/deployagent
2. Run:
sudo cp /opt/deployagent/deployagent.service /etc/systemd/system/deployagent.service
sudo chmod 644 /etc/systemd/system/deployagent.service
sudo systemctl start deployagent
sudo systemctl status deployagent