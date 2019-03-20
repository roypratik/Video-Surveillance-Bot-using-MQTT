# Video-Surveillance-Bot-using-MQTT

A video surveillance bot with rotatable camera using MQTT. A bot on four wheels equipped with 2 motor drivers along with a raspberry pi interfaced with the GPIO pins. The camera of rpi is mounted on a servo motor so as to rotate the camera to 270 degrees.

The video surveillance feed is given directly to a web page with the miniumum lag possible and high frame rates depending on the connectivity.

A seperate node mcu connected to a 10k Ohms potentiometer which acts as physical real-time rotation of the servo motor on which the camera is mounted.

motor.py for controlling the motors using raspberry pi from the keyboard.

node.ino to upload in node mcu for publish the values of potentiometer using MQTT.

rpi_camera.py to upload the real time video feed to the webpage.

mqtt_pot.py to subscribe to the values sent by node mcu using MQTT and mapping the angle of servo motor with potentiometer values sent. 
