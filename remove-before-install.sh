#!/bin/bash
kill $(pgrep -f flask)
rm -rf /home/ec2-user/app