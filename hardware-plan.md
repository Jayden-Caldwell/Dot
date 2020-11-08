# Hardware

## Contents
- [Hardware](#hardware)
  * [Hardware we will use](#What-hardware-will-dot-use)
  * [Why we chose the hardware](#why-we-chose-the-hardware)
  * [IRobot Create 2](#irobot-create-2)
  * [Raspberry Pi 4](#raspberry-pi-4)
  * [Helpful links](#helpful-links)


### What hardware will Dot use
The Dot robot consists of multiple pieces of hardware each working together to produce an approachable robot that can interact with people. The main piece of hardware is the iRobot create 2 which is a programmable Roomba. This is used to move Dot around a room and avoid hitting obstacles along the way. The iRobot will be communicating through the raspberry pi 4 attached to it in which is then connected to a touch display that allows users to communicate directly with the Dot. The touch display will have survey questions that are provided from a python app. These questions once answered are stored, completely the main purpose of Dot to collect information.

### Why we chose the hardware
The iRobot create was a perfect suit for what we wanted to create as it comes with motors and sensors already connected and has perfect detection of surfaces allowing the robot to move around freely. Also, the robot was circular and had a wide base, this allows us to easily fit a shell onto the iRobot to give our robot the warm feeling of a Dot. Basically, the iRobot was the prefect chassis for what we wanted to make. To speak to the iRobot, we are using a Raspberry Pi 4. The reasoning for using the pi 4 is for the Wi-Fi capabilities allowing us to send the data from the iRobot to a different location instead of storing it onboard. Finally, the touch display. This is used as the face of Dot. When Dot is moving around the room the display will show a face that is welcoming for people. Once Dot has approached a person it will ask if they would like to take part in a survey, if this is the case the questions will display on the screen. To answer a question that has been displayed on the screen you simply touch of the answer you would like to provide. The questions will be simple yes no answers at first but can be more complex in the future.

### IRobot Create 2
The iRobot is a mobile robot that is made up completely of remanufactured parts from Roombas. The iRobot is used for educational purposes including developers, high-school and university students. With the iRobot you can program it to create your own projects or you can even start out online with sample projects provided. The best feature about the iRobot and why it stood out to us was the fact that it is completely ready to go out of the box with working motors and sensors. It also has a docking station that the iRobot can find manually on its own when it has completed a task or is simply running low on battery. The robot uses a serial connection to communicate with computers, other microcontrollers or in our case a raspberry pi being a microcomputer

### Raspberry Pi 4
The raspberry pi is a perfect suit for what we are trying to achieve, not only do we use python in most of our classes, but python is the leading software in the world. This made the Pi a suitable choice for use to create a program to control not only how the robot functions but to also run a GUI program for the survey. Connecting the Pi to the iRobot is not a simple task though. The iRobot’s serial port uses 5V logic-level asynchronous serial communication. This would be ideal if we were to use an Arduino since they use 5V logic. However, since we are using a Pi they run on lower voltage level logic, meaning we will need to step down the 5V to 3.3V so the Pi can safely work with the iRobot without getting damaged.

### Helpful links
[Tutorial form iRobot about the 3.3V logic](https://www.irobotweb.com/-/media/MainSite/PDFs/About/STEM/Create/Create_2_Serial_to_33V_Logic.pdf)
