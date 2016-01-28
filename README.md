#Mini Golf Part I: Prototype

A while back, I asked for ideas for future challenges and /u/codex81 suggested mini-golf (thanks for a great idea!). Now that I've been working on it, I think this
 is a good candidate for a group project; together, I think we could make this into a pretty decent game. So as not to disappoint, there is a
 specific challenge for you to solve, but I'd like the true focus of this challenge to be planning out the final game that we'd be making and use subsequent challenges to 
 implement different parts of the game. The provided code is a playable prototype to help get the ideas flowing.


Project Goals:

- Produce a complete mini-golf game 

- Give people the opportunity to work collaboratively

- Have something you can point to and say, "I helped make that!"

Non-negotiables:

- Github for version control
 
- Project structure based on Mek's multi-scene template

- All code contributions must be licensed as public domain


Github repo:

Challenge thread:

#How It Works

###State Machine

This code uses [Mekire's multi-scene template]() in place of the simpler state machine I've been using previously. It's very similar, but better organized.  

###States

Splash - The title sequence. The ball and player objects are created during this state.

HoleStart - Displays the hole number and par for the current hole

Ball Placement - This state just fills the screen with white at the moment, but should allow the player to place the ball inside a tee area

Putting - Allows the player to move the putter with the mouse. The distance of the putter to the ball determines the amount of force applied
 and the angle from the center of the putter to the ball determines the angle the ball will be hit at. Clicking the mouse starts the swing.
 
Swinging - Show the putter travelling towards the ball until impact and set ball's velocity based on swing power and angle

Spectating - Move the ball and check for collisions with the hole's mask and the cup until the ball has dropped below a minimum velocity or goes in the cup.

View Scorecard - Displays a scorecard that shows the player's score for each hole 

###Holes

Each hole is represented by an instance of course_hole.CourseHole. The hole's image is created from two
 separate images, "hole*num*" and "green*num*" where num is the hole number. The "hole" image has the hole's walls drawn on it and is used to create a mask. The
 "green" image has the putting surface and any hills or ramps drawn to it.

###Ramps and Hills

Ramps and Hills work similarly by altering the ball's velocity. Ramps have a rect and a specific velocity, e.g., (-1, 0), while Hills apply velocity using a center point and radius.

###Collisions

The ball is moved one pixel at a time alternating between the x and y components of the ball's velocity and checked for collision with the hole's mask. When a collision is detected, whichever component
 of the ball's velocity was last used to move the ball is flipped.

###Putting

The ball's velocity after impact depends on two factors: the angle from the putter to the ball and the distance from the putter to the ball. A greater distance
 will result in more force being applied to the ball (up to the maximum allowed power).

###Controls

*F* Toggle Fullscreen

*M* Toggle Music

*S* Skip to next song

*ESC* Exit

#Challenge

Ball Placement - Currently, the ball is placed at the same position at the start of each hole. Add a new Rect attribute, tee_rect, to the Hole class. Modify the BallPlacement
 state so it allows the player to place the ball wherever they want within the hole's tee rect.

#Achievements

Wish List - Got a cool idea for the game? Let's hear it.

Prototype Review - The prototype is just that - a prototype; other than the "non-negotiables"  above, I'm not married to any of it.  What's missing? What's unnecessary? What did you like? What didn't you like?
 Any bugs or unexpected behavior?  


Good luck, have fun - let's make a game!