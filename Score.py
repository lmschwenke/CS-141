#Complete
import math
class Score:
    def __init__(self, player_name):
        self.player_name = player_name
        self.current_score = 0
        self.current_level = 0
        self.current_multiplier = 1
        self.lives_remaining = 3
    def add_points(self, amount):
        self.current_score = self.current_score + (amount * self.current_multiplier)
        if self.current_score < 9999:
            self.current_level = 0
            return self.current_level
        else:
            self.current_level = int(math.log2(self.current_score/10000)) + 1
        
        return self.current_score
    def subtract_points(self, amount):
        self.current_multiplier = 1
        self.current_score = (self.current_score - amount)
        if self.current_score < 9999:
          self.current_level = 0
        else:
          self.current_level= int(math.log2(self.current_score/10000)) + 1
        if self.current_score < 0:
          self.current_score = 0         
        return self.current_score

    def get_multiplier(self):
        return self.current_multiplier
    def increment_multiplier(self):
        self.current_multiplier = self.current_multiplier + 1
        return self.current_multiplier
    def get_score(self):
        return self.current_score
    def get_level(self):
        return self.current_level
    def get_lives(self):
        return self.lives_remaining
    def lose_life(self):
        self.lives_remaining = (self.lives_remaining - 1)
        if self.lives_remaining == 0:
            return False
        return True
    
    def gain_life(self):
        self.lives_remaining = self.lives_remaining + 1
    def __str__(self):
        a_string = "Player: {}, Score: {}, Level: {}, Multiplier: {}, Lives: {}"\
        .format(self.player_name, self.current_score, self.current_level, \
        self.current_multiplier, self.lives_remaining)
        return a_string

if __name__ == '__main__':
                                                
    player1 = Score(" ~ Test Name ~ ")
     #~ Test Name ~ signifies where the player would type their own name.
    print(player1)