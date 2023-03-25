#----------------------------------------------------
# Player implementation
#----------------------------------------------------

from .goat import Goat

class Player:
    '''
    An object in this class represents a player in the game Goat Race.
    '''
    def __init__(self,colour):
        '''
        initialize the player with attributes of colour and list of empty goats
        '''
        self.colour = colour
        self.goat = []
            
                
    def add_goat(self):
        '''
        adds the goat in player's goat list
        '''
        goat = Goat(self.colour.upper())                            # creates goat object
        self.goat.append(goat)                                      # append the goat object
    
    def remove_goat(self):
        '''
        remove the goat from player's goat list
        '''
        #goat = str(self.colour[0].upper()) + str(len(self.goat))   # Don't need this with current revision 
        self.goat.pop()                                             #removes the last goat object from the list
        
    def get_colour(self):
        '''
        returns the player colour
        '''
        return self.colour
    
    def get_goat_numbers(self):
        '''
        returns the number of goat the player has
        '''
        return len(self.goat)
    
    def __str__(self):
        '''
        returns the string of player attribute and goats the player holds at particular position
        '''
        header = (self.get_colour()+"\n" +"Goats:\n") 
        for goat in self.goat:
            body = (goat.get_colour()+' '+ goat.get_position()+"\n")
            header += body
        return header

if __name__ == '__main__':
    player = Player("White")                #TEST CASES
    player.add_goat()