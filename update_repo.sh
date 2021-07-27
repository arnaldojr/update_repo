#!/bin/bash
echo "Atualizando repositorios..." >> ~/update_repo.txt
cd /home/ubuntu/update_repo
git pull
echo "atualizando repositorio git bumper." >> ~/update_repo.txt
cd /home/ubuntu/catkin_ws/src/bumper
git pull
echo "atualizando repositorio git servo_arm." >> ~/update_repo.txt
cd /home/ubuntu/catkin_ws/src/servo_arm
git pull
echo "atualizando repositorio git servo_camera." >> ~/update_repo.txt
cd /home/ubuntu/catkin_ws/src/servo_camera
git pull
echo "Repositórios atualizados." >> ~/update_repo.txt
date >> ~/update_repo.txt
