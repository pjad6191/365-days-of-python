## October 29, 2025 - Day 82

### What I Worked On:  
**Exercism:**  
I worked on an Exercism problem that involved object oriented programming and created a class with methods. This was good because I'm just starting to feel comfortable with it. It was a fairly easy assignment though, and I was able to do it without looking at notes or looking anything up. 

### Concepts Practiced:  
- Object Oriented Programming
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
    
### Exercism Code: 
```python

class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    health = 3
    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        Alien.total_aliens_created += 1

    def hit(self):
        if self.health > 0:
            self.health -= 1
        
    def is_alive(self):
        if self.health > 0:
            return True
        return False
    
    def teleport(self, new_x, new_y):
        self.x_coordinate += new_x
        self.y_coordinate += new_y
        return self.x_coordinate, self.y_coordinate

    def collision_detection(self, other_object):
        pass

    
#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.

def new_aliens_collection(alien_start_positions):
    aliens = []
    for item in alien_start_positions:
        aliens.append(Alien(item[0], item[1]))
    return aliens
    
```
