# update_repo

Instruções para atualização automatica dos repostitorios do robo fisico turtlebot3.

acessar via SSH o robô e rodar os comandos abaixo:

    cd ~
    git clone https://github.com/arnaldojr/update_repo.git
    cd ~/update_repo
    ./script.sh


## O que esta sendo feito:

    repositorios para atualização automatica bumper, servo_camera, servo_arm
    restart do serviços 

# Para restart apenas dos serviços do robô

    sudo systemctl restart start_turtle.service
    
  
