# Fetch Roboy: 
## Roboy Hackathon Project

Servo Control notes: 
- pulse 1: clockwise turn
- pulse 2: counter-clockwise turn
## Control Topics
topic | datatype | description
--- | --- | ---
`shy_roboy/nearest_distance` | Float32 | Mean of the closest points to camera (depends on the threshold)
`shy_roboy/state` | Int8 | 0: IDLE, 1: OCCURED, 2: SHOUT, 3: WATCH (an object / a person was altready asked to leave, but didn't leave yet) 

#### TODO

- [x] Making servos run
- [x] Basic formula for rope length - coordinate dependency
- [ ] Rope
- [ ] Controlling 6 servos at the same time
- [ ] Cutting the bot case out

##### Nice to have
- [ ] Regulate speed 
- [ ] Simple recognition
