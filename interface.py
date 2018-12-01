import connection
import struct
import time

#set state of robot
def state(state):
    if state == 'start':
        connection.write(128)
        pass
    elif state == 'reset':
        connection.write(7)
        pass
    elif state == 'stop':
        playSongs()
        connection.write(173)
        pass
    elif state == 'safe':
        connection.write(131)
        pass
    elif state == 'full':
        connection.write(132)
        pass
    pass

#This method reads the state of the buttons
def buttons():
    connection.write(142)
    connection.write(18)
    data = connection.read(1)
    byte = struct.unpack('B', data)[0]
    return byte
    pass

#gets the intensity of the IR sensor on the right
def lightRight():
    connection.write(142)
    connection.write(51)
    data = connection.read(2)
    byte = struct.unpack('>H', data)[0]
    return byte
    pass

#gets the intensity of the IR sensor on the left
def lightLeft():
    connection.write(142)
    connection.write(46)
    data = connection.read(2)
    byte = struct.unpack('>H', data)[0]
    return byte
    pass

#gets the intensity of the IR sensor on the  centre right
def lightCenterRight():
    connection.write(142)
    connection.write(49)
    data = connection.read(2)
    byte = struct.unpack('>H', data)[0]
    return byte
    pass

#gets the intensity of the IR sensor on the front right
def lightFrontRight():
    connection.write(142)
    connection.write(50)
    data = connection.read(2)
    byte = struct.unpack('>H', data)[0]
    return byte
    pass

#gets the intensity of the IR sensor on the front left
def lightFrontLeft():
    connection.write(142)
    connection.write(47)
    data = connection.read(2)
    byte = struct.unpack('>H', data)[0]
    return byte
    pass

#gets the intensity of the IR sensor on the center left
def lightCenterLeft():
    connection.write(142)
    connection.write(48)
    data = connection.read(2)
    byte = struct.unpack('>H', data)[0]
    return byte
    pass

#get light bumpers (Infrared sensors)
def lightBump():
    connection.write(142)
    connection.write(45)
    data = connection.read(1)
    byte = struct.unpack('B', data)[0]
    return byte;
    pass

#get bumpers and wheels
def bumpDrops():
    connection.write(142)
    connection.write(7)
    data = connection.read(1)
    byte = struct.unpack('B', data)[0]
    return byte
    pass

#check wheels
def wheelDropped():
    byte = bumpDrops()
    bi = "{0:4b}".format(byte)
    if bi[0] == "1" or bi[1] == "1":
        return True
    return False
    pass

#check which bumpers
def bump():
    byte = bumpDrops()
    bi = "{0:4b}".format(byte)
    #left bump
    if bi[2] == "1" and bi[3] == "0":
        return 3
    #both bumps
    elif bi[2] == "1" and bi[3] == "1":
        return 2
    #right bump
    elif bi[3] == "1" and bi[2] == "0":
        return 1
    #no bumps
    return 0
    pass

#checks the bumpers
def bumpers():
    byte = bumpDrops()
    bi = "{0:4b}".format(byte)
    if(bi[2] == "1" or bi[3] == "1"):
        return True
    else:
        return False
    pass

#check for cliffs
def cliffs():
    connection.write(149)
    connection.write(4)
    connection.write(9)
    connection.write(10)
    connection.write(11)
    connection.write(12)
    data = connection.read(1)
    byte0 = struct.unpack('B', data)[0]
    data = connection.read(1)
    byte1 = struct.unpack('B', data)[0]
    data = connection.read(1)
    byte2 = struct.unpack('B', data)[0]
    data = connection.read(1)
    byte3 = struct.unpack('B', data)[0]
    if byte0 or byte1 or byte2 or byte3 == 1:
        return True
    return False
    pass

#This method checks if the button has been pressed
def buttonPressed():
   if buttons() == 1:
      #Stops accidental double clicks
      if buttons() == 1:
          return True
   return False
   pass

#Turns decimal values into 2's complemented hexadecimal values
def dec2hex2comp(val):
    base=16
    size=4
    return hex(int(val) & (1<<base)-1)[2:].zfill(size)
    pass

#Returns the higher 2 values in a length 4 value
def hexSplitTop(val):
    return val[0:2]
    pass

#Returns the lower 2 values in a length 4 value
def hexSplitBot(val):
    return val[2:4]
    pass

#Turns hexadecimal values into decimal values
def hex2dec(val):
    base=16
    return int(val, base)
    pass

#This method sets the velocity of both wheels
def drive(vr, vl):
    #Gets velocity in correct form for right wheel
    vrh=hex2dec(hexSplitTop(dec2hex2comp(vr)))
    vrl=hex2dec(hexSplitBot(dec2hex2comp(vr)))
    #Gets velocity in correct form for left wheel
    vlh=hex2dec(hexSplitTop(dec2hex2comp(vl)))
    vll=hex2dec(hexSplitBot(dec2hex2comp(vl)))
    #Sends the command to the robot Direct Drive
    connection.write(145)
    #Sets velocity right wheel high
    connection.write(vrh)
    #Sets velocity right wheel low
    connection.write(vrl)
    #Sets velocity left wheel high
    connection.write(vlh)
    #Sets velocity left wheel low
    connection.write(vll)
    pass

def dock():
    connection.write(142)
    connection.write(17)
    data = connection.read(1)
    byte = struct.unpack('B', data)[0]
    return byte
    pass

#Song of Storms - Legend of Zelda - Ocarina of Time
def songing():
    #song 0
    connection.write(140)
    connection.write(0)
    connection.write(14)
    connection.write(74)
    connection.write(8)
    connection.write(77)
    connection.write(8)
    connection.write(86)
    connection.write(32)
    connection.write(74)
    connection.write(8)
    connection.write(77)
    connection.write(8)
    connection.write(86)
    connection.write(32)
    connection.write(88)
    connection.write(48)
    connection.write(89)
    connection.write(8)
    connection.write(88)
    connection.write(8)
    connection.write(89)
    connection.write(8)
    connection.write(88)
    connection.write(8)
    connection.write(84)
    connection.write(8)
    connection.write(81)
    connection.write(16)
    connection.write(0)
    connection.write(16)
    #song 1
    connection.write(140)
    connection.write(1)
    connection.write(10)
    connection.write(81)
    connection.write(16)
    connection.write(74)
    connection.write(16)
    connection.write(77)
    connection.write(8)
    connection.write(79)
    connection.write(8)
    connection.write(81)
    connection.write(48)
    connection.write(81)
    connection.write(16)
    connection.write(74)
    connection.write(16)
    connection.write(77)
    connection.write(8)
    connection.write(79)
    connection.write(8)
    connection.write(76)
    connection.write(48)
    pass

#plays a song
def playSong(number):
    connection.write(141)
    connection.write(number)
    pass

#plays both songs in order
def playSongs():
    songing()
    playSong(0)
    time.sleep(3.5)
    playSong(1)

#returns how far the robot has turned since the last time it was called
def angle():
    connection.write(142)
    connection.write(20)
    data = connection.read(1)
    byte0 = struct.unpack('B', data)[0]
    data = connection.read(1)
    byte1 = struct.unpack('B', data)[0]
    number_hex = dec2hex2comp(str(byte0)+str(byte1))
    number_dec = hex2dec(number_hex)
    num = number_dec/.324056
    return num
    pass

#returns how far the robot has gone since the last time it was called
def distance():
    connection.write(142)
    connection.write(43)
    data = connection.read(1)
    byte0 = struct.unpack('B', data)[0]
    connection.write(142)
    connection.write(44)
    data = connection.read(1)
    byte1 = struct.unpack('B', data)[0]
    num = byte0 + byte1
    num = num/2
    return num
    pass
