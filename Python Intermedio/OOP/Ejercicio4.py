class Head:
    def __init__ (self, eye_color, hair_color):
        self.eye_color = eye_color
        self.hair_color = hair_color
class Torso:
    def __init__ (self, head, right_arm, left_arm):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
class Arm:
    def __init__ (self, hand):
        self.hand = hand
class Hand:
    def __init__ (self, fingers, nails):
        self.fingers = fingers
        self.nails = nails
class Leg:
    def __init__ (self, foot):
        self.foot = foot
class Feet:
    def __init__ (self, toes):
        self.toes = toes
class Human:
    def __init__ (self, torso, right_leg, left_leg):
        self.torso = torso
        self.right_leg = right_leg
        self.left_leg = left_leg
    
head = Head("green", "blonde")
hand = Hand(5, "short")
foot = Feet(5)
right_arm = Arm(hand)
left_arm = Arm(hand)
right_leg = Leg(foot)
left_leg = Leg(foot)
torso = Torso(head, right_arm, left_arm)
human = Human(torso, right_leg, left_leg)