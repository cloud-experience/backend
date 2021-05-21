#!/bin/bash
cd /home/ec2-user/app/
systemctl restart nginx
gunicorn -w 1 app:app &