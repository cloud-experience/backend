#!/bin/bash
sudo kill $(pgrep -f python3)
# python3 /home/ec2-user/app/app.py &
# cd home/ec2-user/app/
# gunicorn -w 1 app:app
# systemctl restart nginx