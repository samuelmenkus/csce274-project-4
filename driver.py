import interface
import time

#Resets connection
interface.connection.close()
interface.connection.open()
#Starts robot sets to passive mode
interface.state('start')
#Sets robot to safe mode
interface.state('safe')
#set button_pressed state to false
button_pressed = False
time.sleep(.015)
#previous error
error_pri = 0
#proportional gain
Kp = .075
#derivative gain
Kd = .01
#iteration time (seconds)
iter_time = .15
#runs forever
while(1):
    #runs while button_pressed state is true
    while(button_pressed):
        #if a bumper is hit
        if interface.bumpers():
            #back up for .03 seconds
            interface.drive(-200,-200)
            time.sleep(.03)
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
            interface.drive(200, -200)
        #else if the output is in a good range
        #go straight
        elif(0 < output < 230):
            interface.drive(output,200)
        #else if the output is negative
        #turn slightly to the left
        elif(output < 0):
            interface.drive(200, 200+output)
        #if the output is too great
        #turn slightly to the right
        elif(output > 237):
            interface.drive(output-200,200)
        #if the button is pressed change the button_pressed state to  false
        if interface.buttonPressed() == True:
            button_pressed = False

    #stop/ don't move/ don't start
    interface.drive(0,0)

    #if the button is pressed change button_pressed state to true
    if interface.buttonPressed() == True:
        button_pressed = True
