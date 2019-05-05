# Fetch Roboy: 
## Roboy Hackathon Project

The idea of this project is to allow a gripper robot to move not only in 2D, but also in 3D. For this purpose we use 4 ropes attached to the robot that is hanging right beneath the cealing, while the gripper hand hangs from below and can fetch objects. 

## Control Topics
topic | datatype | description
--- | --- | ---
`the_claw/GoTo` | geometry_msgs/Pose2D | Euclidean coordinates of desired position
`the_claw/MoveBox` | roboy_middleware_msgs/MotorCommand | Actuate the servos of the box (always id:"0")
`the_claw/CommandGripper` | std_msgs/Int16 | Commands gripper motor

#### TODO

- [x] Investigation of initial code
- [x] Servo control
- [x] LED controll
- [x] Movement rules based on rope length
- [x] Hardware preparation
- [x] Design of bot case
- [ ] Cutting the bot case out

##### Nice to have
- [x] Regulate speed 
- [ ] Simple pose recognition for control

