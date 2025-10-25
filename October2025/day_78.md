## October 25, 2025 - Day 78

### What I Worked On:  
- Exercism - Finished the learning exercise dealing with unpakcing and multiple assignments. 
- Worked on Problem Set 5 from Intro to Computer Programming in Python. 
- Started ch.13 in textbook (Introduction to Computation and Programming Using Python)

### Concepts Practiced:  
- Packing / unpacking iterables
- Object oriented programming
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
- [Problem 5](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/ps5/)
- [Introduction to Computational Thinking and Data Science](https://ocw.mit.edu/courses/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/)
    
### Code: 
```python
#Problem Set 5 - Problem 2 
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase.lower()
        
    def is_trigger_present(self, text):
        # Normalize text
        text = text.lower()
        for punc in string.punctuation:
            text = text.replace(punc, " ")
        text = " ".join(text.split())

        # Normalize phrase
        phrase_words = self.phrase.split()
        text_words = text.split()

        # Check for exact match of consecutive words
        n = len(phrase_words)
        for i in range(len(text_words) - n + 1):
            if text_words[i:i+n] == phrase_words:
                return True
        return False


#Exercism Code
"""Functions which helps the locomotive engineer to keep track of the train."""

def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    first, second, third, *last = each_wagons_id
    beginning = [third]
    end = [first, second]
    *all_wagons, = *beginning, *missing_wagons, *last, *end

    return all_wagons


def add_missing_stops(routing, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    stops_dict = kwargs
    stops_list = list(stops_dict.values())
    routing["stops"]= stops_list

    return routing


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    routing_info = {**route, **more_route_information}

    return routing_info


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    a, b, c = zip(*wagons_rows)
    new_list = [list(a), list(b), list(c)]

    return new_list

```
