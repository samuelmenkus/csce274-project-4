
# csce274-001-fall2018-project4

# Samuel Menkus
# Donyelle Wallace
# Trinity Gough


## Files ##
connection.py -> send and receive information from robot

interface.py  -> set state of the robot
              -> send Drive direct command
              -> read state of power button
              -> converts decimal to 2's complement hexadecimal
              -> splits hexadecimal in half
              -> converts hexadecimal to decimal
              -> read state of the bumpers
              -> read state of the wheel drop sensors
              -> read state of cliff sensors
              -> sets up a song
              -> plays a song
              -> reads character received by the omnidirectional IR receiver
              -> checks how far the robot has gone since the last check
              -> checks how far the robot has turned since the last check
              -> reads the intensity of the right IR sensor
              -> reads the intensity of the center right IR sensor
              -> reads the intensity of the front right IR sensor
              -> reads the intensity of the left IR sensor
              -> reads the intensity of the center left IR sensor
              -> reads the intensity of the front left IR sensor
              -> checks the state of the IR sensors

driver.py     -> waits for a button press
              -> follows the wall on the right
              -> uses a PD controller to account for errors
              -> if the bumpers are activated it backs up and then continues
              -> if button is pressed while it is moving it stops
              -> continues until terminated
              -> if a dock is in range to the left of the robot
              -> turns 90 degrees
              -> drives toward the dock
              -> docks properly on the dock
              -> stops moving
              -> plays a song "Song of Storms - Legend of Zelda"
              -> terminates the program


## How To Run ##
To run program have all files in a folder
Use 'python driver.py' to start
Terminates properly when it docks itself
To terminate program use '^C'
