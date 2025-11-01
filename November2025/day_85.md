## November 1, 2025 - Day 85

### What I Worked On:  
**Exercism**
- Finished an exercise dealing with creating a class object "SpaceAge" to determine the age in years someone would be on each planet.
- Finished up the learning portion of Exercism with generator functions. I have never worked with generator functions, so it took me a little bit of time to get the hang of it. Regardless of the fact that it was new, I did not seek outside help. I figured it out on my own. 

**Introduction to Computer Science and Programming in Python**
- Finally finished the last problem set from this class!
  
### Concepts Practiced:  
- Object oriented programming
- Generator functions
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
- [Problem 5](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/ps5/)
  
### Code: 
```python
#Exercism Code:
class SpaceAge:
    """
    Given an age in seconds, calculate how old someone would be on a planet in our solar system
    """
    def __init__(self, seconds):
        self.seconds = seconds
        
    def on_earth(self):
        age = self.seconds / 31_557_600
        return round(age, 2)

    def on_mercury(self):
        age = (self.seconds/31_557_600)/.2408467
        return round(age, 2)

    def on_venus(self):
        age = (self.seconds/31_557_600)/.61519726
        return round(age, 2)

    def on_mars(self):
        age = (self.seconds/31_557_600)/1.8808158
        return round(age, 2)

    def on_jupiter(self):
        age = (self.seconds/31_557_600)/11.862615
        return round(age, 2)

    def on_saturn(self):
        age = (self.seconds/31_557_600)/29.447498
        return round(age, 2)

    def on_uranus(self):
        age = (self.seconds/31_557_600)/84.016846
        return round(age, 2)

    def on_neptune(self):
        age = (self.seconds/31_557_600)/164.79132
        return round(age, 2)


#To Finish up all the learning modules on Exercism 
"""Functions to automate Conda airlines ticketing system."""

def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    seat_letters = ["A", "B", "C", "D"]
    seat_index = 0
    count = 0
    while count < number:
        yield seat_letters[seat_index]
        if seat_index < 3:
            seat_index += 1
        else:
            seat_index = 0
        count += 1


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    row = 1
    seat_letter = generate_seat_letters(number)
    count = 0
    while count < number:
        seat = str(row) + next(seat_letter)
        yield seat
        count +=1
        if count%4 == 0:
            row+=1
            if row == 13:
                row+=1
        

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    passenger_dict = {}
    num_of_seats = len(passengers)
    seat = generate_seats(num_of_seats)
    for person in passengers:
        passenger_dict[person]=next(seat)
    return passenger_dict


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    num_of_codes = len(seat_numbers)
    count = 0
    while count < num_of_codes:
        num_of_zeros = 12 - len(flight_id) - len(seat_numbers[count]) 
        flight_code = seat_numbers[count] + flight_id +(num_of_zeros*"0")
        yield flight_code
        count+=1


#Problem Set 5:
# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    filtered_stories = []

    for story in stories:
        for trig in triggerlist:
            if trig.evaluate(story):
                filtered_stories.append(story)
                break  # once one trigger fires, move to next story

    return filtered_stories


# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers
    trigger_name_dict = {
        "TITLE":"TitleTrigger", 
        "DESCRIPTION":"DescriptionTrigger", 
        "AND":"AndTrigger", 
        "NOT":"NotTrigger", 
        "OR":"OrTrigger"}
    trigger_dict = {}
    trigger_list = []
    for line in lines:
        #Take out the commas
        pieces = line.split(",")
        parts = []
        for piece in pieces:
            parts.append(piece.strip())
        
        #To add the names of the trigger to the trigger list
        if parts[0] == "ADD":
            for name in parts[1:]:
                trigger_list.append(trigger_dict[name])
            
        else: 
            # Trigger definition
            name = parts[0]
            trigger_type = parts[1]

            if trigger_type == "TITLE":
                trigger = TitleTrigger(parts[2])

            elif trigger_type == "DESCRIPTION":
                trigger = DescriptionTrigger(parts[2])

            elif trigger_type == "AFTER":
                trigger = AfterTrigger(parts[2])

            elif trigger_type == "BEFORE":
                trigger = BeforeTrigger(parts[2])

            elif trigger_type == "NOT":
                trigger = NotTrigger(trigger_dict[parts[2]])

            elif trigger_type == "AND":
                trig1 = trigger_dict[parts[2]]
                trig2 = trigger_dict[parts[3]]
                trigger = AndTrigger(trig1, trig2)

            elif trigger_type == "OR":
                trig1 = trigger_dict[parts[2]]
                trig2 = trigger_dict[parts[3]]
                trigger = OrTrigger(trig1, trig2)

            trigger_dict[name] = trigger

    return trigger_list
```
