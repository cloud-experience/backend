#!/bin/bash
sudo kill $(pgrep -f python3)
rm -rf /home/ec2-user/app
