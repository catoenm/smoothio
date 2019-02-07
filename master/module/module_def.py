#################################################
# Class definition and signal codes for modules #
#################################################

class Blender:
    # Slave address
    BLENDER_ADD = 0x04

    # Use to encode states for communication
    blender_states = {
        0 : "IDLE",
        1 : "ON"
    }
    elevator_states = {
        0 : "IDLE",
        1 : "ASCEND",
        2 : "DESCEND",
        3 : "HOME"
    }
    pivot_states = {
        0 : "IDLE",
        1 : "CW",
        2 : "CCW",
        3 : "HOME"
    }
    routine_states = {
        0 : "IDLE",
        1 : "BLEND AND CLEAN",
        2 : "CLEAN",
        3 : "BLEND"
    }

    # Init variables
    def __init__(self):
        self.blender1 = 0
        self.blender2 = 0
        self.elevator = 0
        self.pivot = 0
        self.routine = 0
        self.pivot_deg = 0
        self.elevator_height = 0
        self.limit1 = 0
        self.limit2 = 0

    # Read data from blend module
    def read_data(self, i2cbus):
        data = i2cbus.read_i2c_block_data(BLENDER_ADD, 0, 9)
        #print ''.join(map(chr, data)) # Print raw incomming data
        self.blender1 = data[0]
        self.blender2 = data[1]
        self.elevator = data[2]
        self.pivot = data[3]
        self.routine = data[4]
        self.pivot_deg = data[5]
        self.elevator_height = data[6]
        self.limit1 = data[7]
        self.limit2 = data[8]
        print "Blender 1: {}".format(blender_states[self.blender1])
        print "Blender 2: {}".format(blender_states[self.blender2])
        print "Elevator: {}".format(elevator_states[self.elevator])
        print "Pivot: {}".format(pivot_states[self.pivot])
        print "Routine: {}".format(routine_states[self.routine])
        print "Pivot Angle: {} degrees".format(self.pivot_deg)
        print "Elevator Height: {}cm".format(self.elevator_height)
        print "Limit Switch 1: {}".format(self.limit1)
        print "Limit Switch 2: {}".format(self.limit2)


    # Selectors
    def print_selectors(self):
        print """
            Selector Numbers
            --------------
            0: Read state
            1: Blender 1
            2: Blender 2
            3: Pivot
            4: Elevator
            5: Routine
            255: Reset
        """

    # Actions
    def print_actions(self, selector):
        print """
            Actions
            --------------
        """
        if selector == 1 or selector == 2:
            for key,val in blender_states.items():
                print "{} : {}".format(key,val)
        elif selector == 3:
            for key,val in pivot_states.items():
                print "{} : {}".format(key,val)
        elif selector == 4:
            for key,val in elevator_states.items():
                print "{} : {}".format(key,val)
        elif selector == 5:
            for key,val in routine_states.items():
                print "{} : {}".format(key,val)

class Carousel:
    CAROUSEL_ADD = 0x05

    ABORT = 0x01
    ROTATE_SIGNAL = 0x02

class Dispense:
    DISPENSE_ADD = 0x06

    ABORT = 0x01
    DISPENSE_LIQUID = 0x02
    

