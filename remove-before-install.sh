#!/bin/bash
if pgrep -x python3 >/dev/null
then
  sudo kill $(pgrep -f python3)
else
  exit 0
fi
