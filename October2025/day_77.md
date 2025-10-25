## October 24, 2025 - Day 77

### What I Worked On:  
- Began a learning exercise on Exercism regarding packing and unpacking interables. 
- Started Problem Set 5 from Intro to Computer Programming in Python. 
- Read 12.1 in textbook (Introduction to Computation and Programming Using Python)
- Watched Lecture 1: Introduction and Optimization Problems from Introduction to Computational Thinking and Data Science

### Concepts Practiced:  
- Packing / unpacking iterables
- Object oriented programming
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
- [Introduction to Computational Thinking and Data Science](https://ocw.mit.edu/courses/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/)
    
### Code: 
```python
#Problem Set 5 
class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        '''
        Initializes a NewsStory object
                
        guid (string): globally unique identifier (GUID)
        title (string): the news story's headline
        description (string): a summary of the news story
        link (string): website link to the story
        pubdate (datetime): date the news was published      
        '''
        self.guid = guid
        self.title = title 
        self.description = description
        self.link = link
        self.pubdate = pubdate
    
    def get_guide(self):
        return self.guide
        
    def get_title(self):
        return self.title
        
    def get_description(self):
        return self.description
    
    def get_link(self):
        return self.link
        
    def get_pubdate(self):
        return self.pubdate


#Exercism Code
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

```
