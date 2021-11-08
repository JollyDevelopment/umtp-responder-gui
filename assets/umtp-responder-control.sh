#!/usr/bin/env bash

# This file is used by polkit to start/stop/restart/enable/disable the
# umpt-responder.service

# case/esac for saving the new settings and start/stop/restart/enable/disable the 
# service
case $1 in
    update)
      # save the ~/.config/umtp-responder/umtprd.conf file to /etc/umtprd/umtprd.conf
      mv /home/"$2"/.config/umtp-responder-gui/umtprd.conf /etc/umtprd/umtprd.conf
      ;;
    start)
      systemctl start umtp-responder.service
      ;;
    stop)
      systemctl stop umtp-responder.service
      ;;
    restart)
      systemctl restart umtp-responder.service
      ;;
    enable)
      systemctl enable --now umtp-responder.service
      ;;
    disable)
      systemctl stop umtp-responder.service
      ;;
esac