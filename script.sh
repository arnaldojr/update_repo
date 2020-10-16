#!/bin/sh

echo "Atualizando start_turtle.sh"
rm -rf /usr/bin/start_turtle.sh
cp ~/update_repo/start_turtle.sh /usr/bin/start_turtle.sh

echo "Exclui repositorios bumper, servo_camera e servo_arm antigos"
rm -rf ~/catkin_ws/src/bumper
rm -rf ~/catkin_ws/src/servo_camera
rm -rf ~/catkin_ws/src/servo_arm

echo "Clona repositorios bumper, servo_camera e servo_arm"
cd ~/catkin_ws/src/
git clone https://github.com/arnaldojr/bumper.git
git clone https://github.com/arnaldojr/servo_camera.git
git clone https://github.com/arnaldojr/servo_arm.git

echo "compilando catkin..."
cd ~/catkin_ws/
catkin_make

echo "Repositorios atualizados"

echo "Restart dos serviços do robo"
sudo systemctl restart start_turtle.service

echo "Fim"