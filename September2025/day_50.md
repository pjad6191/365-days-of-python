## September 27, 2025 - Day 50

### What I Worked On:  
Exercism - Worked on manipulating tuples. I'm enjoying go back and working on basic skills. I'm gaining confidence and proficiency. Also, Exercism gives feedback that tells you how to improve your code which I really appreciate. I work on the functions until there is no further feedback. 

Google's Advanced Data Analytics Python course - Began exploring the TikTok data set

### Concepts Practiced:  
- Loops
- Tuple manipulation
- Writing clean minimal code
- Data cleaning and exploration
          
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
- [Google's Advanced Data Analytics Python Course](https://www.coursera.org/learn/get-started-with-python/home)
    
### Exercism Code: 
```python
"""Functions to help Azara and Rui locate pirate treasure."""

def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """
    return record[1]
    

def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """
    return tuple(coordinate)


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """
    coord1 = convert_coordinate(get_coordinate(azara_record))
    coord2 = rui_record[1]
    return coord1 == coord2


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """
    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    return "not a match"


def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.
    """
    return_string = ""
    for tup in combined_record_group: 
        new_record = []
        for index, unit in enumerate(tup):
            if index !=1:
                new_record.append(unit)
        return_string += (str(tuple(new_record)) + "\n")
        
    return return_string
       
```
