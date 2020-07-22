# Dot

## Contents
- [Laws](#three-laws-of-robotics)
- [Human Interaction](#human-interaction)
  * [Human Safety](#human-safety)
  * [Communication](#communication)
  * [Approaching Humans](#approaching-humans)
- [Robot Design](#robot-design)
  * [Common features](#common-features-in-human-interacting-robots)
  * [Reasons for these features](#reasons-for-these-design-choices)
  * [How these apply to Dot](#how-these-apply-to-dot)
  * [Example videos](#some-videos-showing-human-robot-interaction)
- [Hardware](#hardware)
  * [Hardware we will use](#What-hardware-will-dot-use)
  * [Why we chose the hardware](#why-we-chose-the-hardware)
  * [IRobot Create 2](#irobot-create-2)
  * [Raspberry Pi 4](#raspberry-pi-4)
  * [Helpful links](#helpful-links)
- [Reflection](#reflection)
- [References](#references)
  
### Three Laws of Robotics

1. A robot may not injure a human being or, through inaction, allow a human being to come to harm.

2. A robot must obey any orders given to it by human beings, except where such orders would conflict with the First Law.

3. A robot must protect its own existence as long as such protection does not conflict with the First or Second Law.


## Human Interaction

### Human Safety

As the plan is for DOT to move around a room autonomously, there is concern that
 DOT could run into people and cause them harm. To combat this we will need to make sure we are using enough sensors and have done extensive testing before putting DOT 
 into an area with unsuspecting humans.
If DOT was prone to running into people this would cause people to activly try to avoid DOT, which is not what we want to happen.

### Communication

Communication between human and robot is extremely important in creating a positive experience.  

A few ideas we have had:
- Creating a GUI, which would display the questions on a touch screen, where 
 the user can then press "Yes" or "No" in answer to the question. This would be the easiest to implement, and will be what we aim to do for the first iteration of DOT

- Expanding on the previous idea would be using text to voice and voice to text. DOT would ask the question using a voice that we deemed appropriate(not scary) and
 then the human/user interacting with DOT could then answer by simply saying "Yes" or "No". Using this method would make people more likely to want to interact with
 DOT. Using this method in conjuntion with the previous method would also open DOT up to be used by a range of different people with different abilities. e.g. 
 hearing impaired can use the touch screen, sight impaired can use voice.


### Approaching Humans

DOT is planned to be autonomous, DOT will be approaching humans without outside interference. 

The way that DOT approaches a human is very important. We don't want DOT to rush up on someone and get into their space and start demanding they take a survey, as 
that could make the human extremely uncomfortable or angry.
<i>"An Approach from a robot is not an easy problem since the robot’s approach needs to be acknowledged nonverbally in advance; otherwise, the approached
 person might not recognize that the robot is approaching him/her or would be surprised by the robot’s impolite interruption."</i> (Satake et al., 2020)

To avoid an uncomfortable approach we could focus on making DOT passive. Not approaching people but waiting for people to 
approach first. I believe this would quite succesful most of the time as most people find robots qutie facinating and would want to interact with DOT, 
especially if they are coming to an I.T. related event. 

What about the people who are a little unsure about approaching, or want to interact with DOT and not really sure how they should initiate the interaction.

Perhaps a way to sense the position of a human. 
- If they have their back to the robot or side on in deep conversation with someone = not intersted 
- Looking directly at robot = interested
This would be quite difficult to implement and involve extensive research and hardware to make happen. 

The first iteration of DOT could involve the passive approach, where DOT will stay in one area, as people pass by or approach 
 DOT would greet the human and wait for a response, before asking if they would like to participate in a survey. This would be the best option for a room that is 
quite small or crowded, like the project room.

After that we could work on getting DOT moving around a larger area like the Hub. Figuring out the best option of approaching someone that looks interested, but 
not invading that persons space.

An extremely good research paper on approaching humans is [here](https://www.researchgate.net/publication/221473299_How_to_Approach_Humans-Strategies_for_Social_Robots_to_Initiate_Interaction-)

---

## Robot design

### Common features in human-interacting robots
* White in colour
* Large bright eyes, almost anime-like in style
* Cartoon like features: Soft curves, no edges, sometimes blob like
* In most cases, childlike in appearance
* About as tall as a 5-10 year old child
* The robot's screen either serves a dual-purpose as its face and interaction point, or is appended to their chest
* Has human features, such as hands, face, eyes, but avoids making them look too realistic
* Its face can convey cartoon like expressions such as: happiness, anger (in a cute way), distress (also in a cute way)
* Have some form of body-language that resemble what a human does

### Reasons for these design choices
* Large eyes, soft features, childlike appearance, and body language make the robot seem non-threatening, approachable, friendly, and cute (Cook, 2018). Very important for if you are dealing with real humans. White colour adds to this, as it is associated with safety, innocence and cleanliness (Cherry, 2020).
	
* Allows the robot to be used in a variety of contexts without needing to change the design, which saves on production costs. For example, this particular model of robot has been used as a gimmick for a store front ([www.youtube.com/watch?v=v931a6sPUZw](https://www.youtube.com/watch?v=v931a6sPUZw)) and as a lecturer ([www.youtube.com/watch?v=Amfrm2V_KO0](https://www.youtube.com/watch?v=Amfrm2V_KO0)).

* Avoids crossing the uncanny valley, which is probably the most important aspect of the design. If you attempt to make a robot that looks *too* much like a real person, it will end up looking surreal, strange or sometimes creepy (Azarian, 2016).
  * [http://www.youtube.com/watch?v=Sq36J9pNaEo](http://www.youtube.com/watch?v=Sq36J9pNaEo)  
    While the AI is very impressive, the jerky mouth and hand movements are off putting.
	
### How these apply to Dot
* Dot's current design has several of the the above features, including a cute cartoony design, and avoids the uncanny valley, but resembles a penguin more than a human. While penguins are both cute and friendly-looking, it limits the contexts in which Dot can be used. The penguin design would be visually appropriate in the arctic section of a zoo, but not much else. Switching to a more human-blob-like design may increase the approachability of Dot in the context we want it to be used for.

* While complicated body-language may be out of reach considering our resources, cartoonish facial expressions *should* be fairly straightforward to implement. Not only would this give Dot a bit more depth, but would also be effective for comedic effect or an "aww" factor. A few examples:
  * If Dot gets stuck, beads of sweat could appear and their eyes could screw up as it tries to free itself. 
  * If someone taps on Dot's screen before it has initiated a quiz proper, it could display a cartoony angry face or one of discomfort.
  * An extra happy face when someone completes the quiz, says "thank you" or something along those lines.

### Some videos showing human robot interaction

[China International Robot Show defines the future of robotic industry](https://www.youtube.com/watch?v=Sj8lK65fJic)

[UBTECH AI robots offer a helping hand in COVID-19 treating hospitals](https://www.youtube.com/watch?v=Z8QPcTUB9O4)

[Meet Germany's first robot lecturer | DW Documentary](https://www.youtube.com/watch?v=Amfrm2V_KO0)

[Robotic Retail - Robot Ice Cream store developed by Special Patterns](https://www.youtube.com/watch?v=NW8a3D7iVYI)

[Interactive Talking and Dancing Robot at Microsoft Store](https://www.youtube.com/watch?v=v931a6sPUZw)

[Meet Sophia, World's First AI Humanoid Robot | Tony Robbins](https://www.youtube.com/watch?v=Sq36J9pNaEo)

---

## Hardware

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

---

## Reflection
When we decided to do this project, we had to decide what hardware we wanted to use so that we could order it as we knew it would take some time to arrive. While we were waiting, we setup our Github repository and collated all the tutorials that we thought we might need to connect a raspberry PI to the Roomba. We also planned out how Dot was going to look regarding size and what we though would be more appealing to users/customers. This included the location of the touch screen to allow users to communicate effectively.

Up to this point there had been talk of the Polytechnic closing due to COVID-19. This hadn’t affected us much except for the shipping times for parts from overseas. But once lockdown started the Polytechnic was closed forcing us to work separately from home via Teams. Due to the nature of this project, this was devastating to our productivity and motivation, and subsequently we were not able to work with any of the hardware. Because of this we had to get creative and do our best to just research and document this research. During this time, we started making a GUI in python for the user interface for Dot.

Once all the hardware arrived, we had to get it to a team member for them to work on. Since the Roomba was sent from the United States it had a different plug than what we use in New Zealand meaning we needed an adapter. Unfortunately, because of lockdown this prevented us from going and buying one since the shops were closed, meaning the project was delayed even further.

Once lockdown was taken down to level 2, we could access the building and the equipment. Because of health concerns we were not comfortable with extending our bubbles. Even so, we managed to have a play around with the Roomba and connect it to the computer. We found a program called Realterm that was able to connect to the port required by the Roomba and the correct Baud number. Once this was set up we were able to send number codes to the Roomba provided from the ICreate manual. To test the Roomba was communicating with the PC we used the number codes to set the correct time and get it to make noise. Additionally, we managed to get the touch screen communicating with the Raspberry Pi, so that we could touch the screen and interact with the Pi. However, this is pretty much all we were able to accomplish.

Our plan for next semester is to get the raspberry PI talking to the Roomba by following a tutorial online. Once this is working, we would have a better understanding on how we are going to achieve what we set out to do. Overall, we feel that this semester we tried our best considering the circumstances and we will start next semester fresh and ready to achieve greatness.

---
## References
Azarian, B. (2016, April 13). Designing Robots That Avoid The Uncanny Valley. Retrieved from [https://www.psychologytoday.com/us/blog/mind-in-the-machine/201604/designing-robots-avoid-the-uncanny-valley](https://www.psychologytoday.com/us/blog/mind-in-the-machine/201604/designing-robots-avoid-the-uncanny-valley)

Cherry, K. (2020, January 17). How White Impact Moods, Feelings, and Behaviors. Retrieved from [https://www.verywellmind.com/color-psychology-white-2795822](https://www.verywellmind.com/color-psychology-white-2795822)

Cook, W. (2018, February 15). The designers helping us embrace robots. Retrieved from [https://www.bbc.com/future/article/20180215-the-designers-helping-us-embrace-robots](https://www.bbc.com/future/article/20180215-the-designers-helping-us-embrace-robots)
