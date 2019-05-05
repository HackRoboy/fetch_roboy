# Fetch Roboy: 
## Roboy Hackathon Project

Servo Control notes: 
- pulse 1: clockwise turn
- pulse 2: counter-clockwise turn
## Control Topics
topic | datatype | description
--- | --- | ---
`the_claw/GoTo` | geometry_msgs/Pose2D | Euclidean coordinates of desired position
`the_claw/MoveBox` | roboy_middleware_msgs/MotorCommand | Actuate the servos of the box (always id:"0")
`the_claw/CommandGripper` | std_msgs/Int16 | Commands gripper motor
#### TODO

- [x] Making servos run
- [x] Basic formula for rope length - coordinate dependency
- [ ] Rope
- [ ] Controlling 6 servos at the same time
- [ ] Cutting the bot case out

##### Nice to have
- [ ] Regulate speed 
- [ ] Simple recognition
