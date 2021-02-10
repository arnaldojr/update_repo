#!/bin/bash
cd /home/ubuntu/catkin_ws/src/update_repo/
git pull
sleep 3
screen -dmS ROBO bash
screen -S ROBO -X screen -t UPDATE_REPO bash -ic "bash /home/ubuntu/update_repo/update_repo.sh"
sleep 3
screen -S ROBO -X screen -t CORE  bash -ic "roslaunch turtlebot3_bringup turtlebot3_core.launch"
sleep  10
screen -S ROBO -X screen -t LIDAR bash -ic "roslaunch turtlebot3_bringup turtlebot3_robot.launch"
sleep 5
screen -S ROBO -X screen -t SERVOCAM bash -ic "rosrun servo_camera driver_node"
sleep 3
screen -S ROBO -X screen -t SERVOARM bash -ic "rosrun servo_arm arm_node"
sleep 3
screen -S ROBO -X screen -t BUMPER bash -ic "rosrun bumper bumper"
sleep 3
screen -S ROBO -X screen -t CAMERA bash -ic "bash /home/ubuntu/camera.sh"
sleep 3
#screen -S ROBO -X screen -t TELINHA bash -ic "/home/ubuntu/net/control.py"
#sleep 2
screen -S ROBO -X screen -t BEEP bash -ic "rostopic pub -1 /sound turtlebot3_msgs/Sound 'value: 1'"


echo 0
