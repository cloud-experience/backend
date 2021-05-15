#!/bin/bash
kill $(pgrep -f flask)
python3 /home/ec2-user/app/checkPageAPI.py
