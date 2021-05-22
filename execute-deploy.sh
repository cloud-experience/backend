#!/bin/bash
sudo kill $(pgrep -f gunicorn)
cd /home/ec2-user/app/
systemctl restart nginx
gunicorn -w 1 --daemon app:app