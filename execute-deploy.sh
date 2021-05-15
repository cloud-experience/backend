#!/bin/bash
sudo kill $(pgrep -f python3)
python3 /home/ec2-user/app/checkPageAPI.py &
