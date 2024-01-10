import random

class CrewMember():
    def __init__(self, name, image_path):
        # Given a name for a crew member and a path to an image set,
        # construct an object describing this crew member.  Randomize
        # all their stats.
        self.name = name
        self.image_path = image_path
        self.status = {'experience': 0,
                       'health': 100,
                       'status': 'Ready',
                       'upgrades_ready': 0,
                       'image_file': 'normal'}
        self.attributes = {'tactical': random.randint(1,10),
                      'engineering': random.randint(1,10),
                      'medical': random.randint(1,10),
                      'physical': random.randint(1,10)}

    def upgrade_attribute(self, attribute):
        # This is the method that upgrades a person (like a "level up")
        # You provide which attribute is being upgraded.
        # If your attribute doesn't exist, or if the value is already maxed out,
        # This will respond with a "false" to let you know nothing was done.
        # Otherwise, it will update and then return a "true".
        if (attribute in self.attributes and self.status['upgrades_ready'] > 0):
            if self.attributes[attribute] == 10:
                return False
            else:
                self.attributes[attribute] += 1
                self.status['upgrades_ready'] -= 1
                return True
        else:
            return False
        
    def get_attribute(self, attribute):
        # If the attribute you ask for doesn't exist, you get a -1.
        if (attribute in self.attributes):
            return self.attributes[attribute]
        else:
            return -1
        
    def add_xp(self, value):
        self.status['experience'] += value
        if (self.status['experience'] >= 100):
            self.status['experience'] -= 100
            if (sum(self.attributes.values()) < 40):
                self.status['upgrades_ready'] += 1

    def damage_health(self, value):
        self.status['health'] -= value
        if (self.status['health'] < 1):
            self.status['health'] = 0
            self.status['status'] = 'Dead'
            self.status['image_file'] = 'dead'
        else:
            self.status['image_file'] = 'wounded'

    def restore_health(self, value):
        if (self.status['status'] == 'Dead'):
            pass
        else:
            self.status['health'] += value
            if (self.status['health'] > 99):
                self.status['health'] = 100
                self.status['image_file'] = 'normal'
