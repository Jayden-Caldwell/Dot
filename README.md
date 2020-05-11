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
  
## References
Azarian, B. (2016, April 13). Designing Robots That Avoid The Uncanny Valley. Retrieved from [https://www.psychologytoday.com/us/blog/mind-in-the-machine/201604/designing-robots-avoid-the-uncanny-valley](https://www.psychologytoday.com/us/blog/mind-in-the-machine/201604/designing-robots-avoid-the-uncanny-valley)

Cherry, K. (2020, January 17). How White Impact Moods, Feelings, and Behaviors. Retrieved from [https://www.verywellmind.com/color-psychology-white-2795822](https://www.verywellmind.com/color-psychology-white-2795822)

Cook, W. (2018, February 15). The designers helping us embrace robots. Retrieved from [https://www.bbc.com/future/article/20180215-the-designers-helping-us-embrace-robots](https://www.bbc.com/future/article/20180215-the-designers-helping-us-embrace-robots)
