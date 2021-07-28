#!/usr/bin/python3
# -*- coding: latin-1 -*-
#Author: Lícia Sales
#Date: 06-28-2021

#imports
import socket
import os
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Image
import ImageDraw
import ImageFont
from sensor_msgs import BatteryState
# Raspberry Pi pin configuration:
RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# 128x64 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

# Initialize library.
disp.begin()

# Get display width and height.
width = disp.width
height = disp.height

# Clear display.
disp.clear()
disp.display()

# Create image buffer.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new('1', (width, height))

# Create drawing object.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# First define some constants to allow easy resizing of shapes.
padding = 2
shape_width = 20
top = padding
emy=top
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = padding
# Load default font.
font = ImageFont.load_default()

#Setup I/O
gpio_pin_down = 27
gpio_pin_up = 17
gpio_pin_left = 22
gpio_pin_right = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_pin_down, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(gpio_pin_up, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(gpio_pin_left, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(gpio_pin_right, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# Write two lines of text.
draw.text((x, top),    'Hello',  font=font, fill=255)
draw.text((x, top+20), 'World!', font=font, fill=255)

# Display image.
disp.image(image)
disp.display()

menu=0
GPIO.add_event_detect(gpio_pin_up, GPIO.FALLING, callback = limpa_tela(menu),bouncetime=300)
GPIO.add_event_detect(gpio_pin_down, GPIO.FALLING, callback = stop_robot(menu),bouncetime=300)
GPIO.add_event_detect(gpio_pin_left, GPIO.FALLING, callback = shutdown_robot(menu),bouncetime=300)
GPIO.add_event_detect(gpio_pin_right, GPIO.FALLING, callback = reboot_nodes(menu),bouncetime=300)        

while True:
    limpa_tela()
    if menu == 0:
        hostname = socket.gethostname() 
        ip_address = socket.gethostbyname(hostname)
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        draw.text((x, 0),"    {}            ".format(hostname),font=font,fill=255)
        draw.text((x,20),"    {}            ".format(ip_address),font=font,fill=255)
        draw.text((x, 40),"                 ",font=font,fill=255)

    


def stop_robot(menu):

    os.system("rostopic pub -1 /cmd_vel geometry_msgs/Twist -- '[0.0, 0.0, 0.0]' '[0.0, 0.0, 0.0]'")        
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    draw.text((x, 0),"     STOPING          ",font=font,fill=255)
    draw.text((x,20),"     INSPERBOT         ",font=font,fill=255)
    draw.text((x, 40),"                     ",font=font,fill=255)
    time.sleep(5)
    menu=0
    return (menu)

def shutdown_robot(menu):
    menu=menu-30
    if menu==-30:
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        draw.text((x, 0),"     SHUTDOWN          ",font=font,fill=255)
        draw.text((x,20),"     INSPERBOT         ",font=font,fill=255)
        draw.text((x, 40),"  Press \/ to confirm ",font=font,fill=255)
    
    if menu==-60:
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        draw.text((x, 0),"                               ",font=font,fill=255)
        draw.text((x,20),"                               ",font=font,fill=255)
        draw.text((x, 40),"                              ",font=font,fill=255)
        time.sleep(1)
        os.system("sudo shutdown now") 
        menu=0               
    return (menu)


def reboot_nodes(menu):
    menu=menu+30

    if menu==30:
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        draw.text((x, 0),"     REBOOT          ",font=font,fill=255)
        draw.text((x,20),"    ROS NODES         ",font=font,fill=255)
        draw.text((x, 40),"  Press < to confirm ",font=font,fill=255)
        
    if menu==60:
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        draw.text((x, 0),"    REBOTING                ",font=font,fill=255)
        draw.text((x,20),"    ROS NODES ...          ",font=font,fill=255)
        draw.text((x, 40),"                              ",font=font,fill=255)
        os.system("sudo systemctl restart start_turtle.service")  
        time.sleep(5)
        menu=0
    return (menu)

def limpa_tela():
        # Draw the image buffer.
        disp.image(image)
        disp.display()
        time.sleep(0.5)
        menu=0
        return (menu)
