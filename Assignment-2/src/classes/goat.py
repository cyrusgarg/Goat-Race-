#----------------------------------------------------
# Goat implementation
#----------------------------------------------------
from .stack import Stack

class Goat:
    '''
    An object in this class represents a goat in the game "Goat Race".
    '''
    def __init__(self,colour,initialPosition: str = None):
        '''
        Assume initial poisiton :str(columnrow)format,colour: str("XYZ")format.
        '''
        if colour.upper() not in ["WHITE", "BLACK", "RED", "ORANGE", "GREEN"]:  # raises exception if colour is not in the defined list of colours
            raise Exception('Invalid colour selection')
     
        
        self.colour = colour
        self.column = -1            #initialize the goat's position outside the board
        self.row = -1               #initialize the goat's position outside the board
        self.position_set = False   #initialize the goat's position to False as initial goat's position is outside the board
        
    def get_position(self):
        '''
        returns the position of the goat
        '''
        if self.position_set:                                   #Execute if goat's position is set
            return str(chr(self.column+65))+str(self.row +1)    # returns the goat's position as respect of the board like 'A1'
        else:
            return str(-1)                                      #If position is not set, it will return '-1'
        
    def get_colour(self):
        '''
        returns the colour of the goat
        '''        
        return self.colour                                      # returns the colour of the goat   
    
    def set_position(self,row:int,column: int):
        '''
        position are comming as respect of board list like (0,0) which is row 1 and column 'A' on the board str
        '''
        self.column = column                                   # set the column position of the goat
        self.row = row                                         # set the row position of the goat
        self.position_set = True
    
    def __str__(self):
        '''
        returns the string of the goat representing its position
        '''        
        return str(chr(self.column+65))+str(self.row+1)       # returns the str representation of the goat's position like 'A1'
        
