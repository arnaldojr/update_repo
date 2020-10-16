#!/bin/bash
echo "Atualizando o hostname..." >> ~/update_repo.txt
echo "atualizando repositorio git bumper."
cd /home/ubuntu/catkin_ws/src/bumper
git pull
echo "atualizando repositorio git servo_arm."
cd /home/ubuntu/catkin_ws/src/servo_arm
git pull
echo "atualizando repositorio git servo_camera."
cd /home/ubuntu/catkin_ws/src/servo_camera
git pull
echo "Repositórios atualizados."
date >> ~/update_repo.txt

echo 0