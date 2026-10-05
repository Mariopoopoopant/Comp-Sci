robot_location = 30
ball_location = 35
goal_location = 20 
have_ball = False

if robot_location < ball_location:
    print("Almost at ball")

if robot_location > ball_location:
    print("You are beyond the goal")

if robot_location == goal_location:
    print("The robot is at the goal")

robot_location += 5

if robot_location == ball_location:
    print("At the ball")
    print("Picking up the ball")
    have_ball = True
    print("Now make your way to the goal")

robot_location -= 15

if robot_location < goal_location:
    print("You went too far.")

if robot_location == goal_location and have_ball is True:
    print("You scored a goal")
    have_ball = False