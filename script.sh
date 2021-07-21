#!/bin/sh

echo "Atualizando start_turtle.sh"
sudo rm -rf /usr/bin/start_turtle.sh
sudo cp ~/catkin_ws/src/update_repo/start_turtle.sh /usr/bin/start_turtle.sh
sudo rm -rf /lib/systemd/system/start_turtle.service
sudo rm -rf /lib/systemd/system/telinha.service
sudo cp ~/catkin_ws/src/update_repo/start_turtle.service /lib/systemd/system/
sudo cp ~/catkin_ws/src/update_repo/telinha.service /lib/systemd/system/

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
sudo systemctl stop start_turtle.service
sudo systemctl stop telinha.service
sudo systemctl start start_turtle.service
sudo systemctl start telinha.service
sudo systemctl enable start_turtle.service
sudo systemctl enable telinha.service
echo "Fim"
