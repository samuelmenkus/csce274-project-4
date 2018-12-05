import interface
import time

#Resets connection
interface.connection.close()
interface.connection.open()
#Starts robot sets to passive mode
interface.state('start')
#Sets robot to safe mode
interface.state('safe')
#Sets robot to full mode
interface.state('full')
#set button_pressed state to false
button_pressed = False
#set turned state to false
turned = False
#set docking state to false
docking = False
time.sleep(.015)
#previous error
error_pri = 0
#proportional gain
Kp = .075
#derivative gain
Kd = .01
#iteration time (seconds)
iter_time = .155
#runs forever
while(1):
    #runs while button_pressed state is true
    while(button_pressed):
        #checks the omnidirectional dock sensor
        robot_docked = interface.dock()
        #if the dock sensor sees the red beam then the robot should
        #go into docking state equal true
        if robot_docked == 168:
            docking = True
        #while docking state equal true
        while(docking == True):
            #if the robot is still following the wall
            if turned == False:
                #turn 90 degrees away from the wall
                interface.drive(100,-100)
                time.sleep(1)
                #set turned state equal to true
                turned = True
            #updates what the robot sees from the omnidirectional dock sensor
            robot_docked = interface.dock()
            #if the robot hits something
            if interface.bumpers():
                #back up a litte, stop, play song, exit program
                interface.drive(-60,-60)
                interface.drive(0,0)
                interface.state('stop')
            #if the sensor sees the red and green buoys go straight
            elif robot_docked == 172:
                #print("straight")
                interface.drive(60,60)
            #if the robot senses the red buoy then turn slightly left
            elif robot_docked == 168:
                #print("left")
                interface.drive(60,30)
            #if the robot senses the green buoy then turn slightly right
            elif robot_docked == 164:
                #print("right")
                interface.drive(30,60)
        #wall follows while it doesnt see the dock
        while(interface.dock() == 0):
            #PD controller
            #error for this iteration
            #set point is 250
            error = 250 - interface.lightRight()
            #derivative for this iteration
            deriv = (error - error_pri)/iter_time
            #output for the controller
            output = Kp*error + Kd*deriv
            #set previous error for the next iteration
            error_pri = error
            #gets the intensities of the IR sensors
            left = interface.lightLeft()
            frontLeft = interface.lightFrontLeft()
            frontRight = interface.lightFrontRight()
            centerLeft = interface.lightCenterLeft()
            centerRight = interface.lightCenterRight()
            #if other sensors are too intense turn left
            if(centerLeft > 200 or centerRight > 145 or left > 200 or frontLeft > 200 or frontRight > 145):
                interface.drive(100, -100)
            #else if the output is in a good range
            #go straight
            elif(0 < output < 230):
                interface.drive(output,100)
            #else if the output is negative
            #turn slightly to the left
            elif(output < 0):
                interface.drive(100, 100+output)
            #if the output is too great
            #turn slightly to the right
            elif(output > 237):
                interface.drive(output-100,100)
            if interface.buttonPressed() == True:
                button_pressed = False
                break
        #if a bumper is hit
        if interface.bumpers():
            #back up for .03 seconds
            interface.drive(-200,-200)
            time.sleep(.03)
        #if the button is pressed change the button_pressed state to  false
        if interface.buttonPressed() == True:
            button_pressed = False
    #stop/ don't move/ don't start
    interface.drive(0,0)
    #if the button is pressed change button_pressed state to true
    if interface.buttonPressed() == True:
        button_pressed = True
