## October 26, 2025 - Day 79

### What I Worked On:  
- Exercism - Recreated some common exisiting functions.
- Worked on Problem Set 5, Parts 3-8 from Intro to Computer Programming in Python. 

### Concepts Practiced:  
- Loops
- Lists
- Object oriented programming
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
- [Problem 5](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/ps5/)
  
### Code: 
```python
#Exercism Code:
def append(list1, list2):
    return list1 + list2

def concat(lists):
    returnlist = []
    for item in lists:
        returnlist = returnlist + item
    return returnlist

def filter(function, list):
    returnlist = []
    for item in list:
        if function(item):
            returnlist.append(item)
    return returnlist

def length(list):
    count = 0
    for item in list:
        count+=1
    return count

def map(function, list):
    returnlist = []
    for item in list:
        returnlist.append(function(item))
    return returnlist

def foldl(function, list, initial):
    for item in list:
        initial = function(initial, item)
    return initial

def foldr(function, list, initial):
    for item in reversed(list):
        initial = function(initial, item)
    return initial

def reverse(list):
    return list[::-1]



#Problem Set 5:

# Problem 3
# TODO: TitleTrigger
class TitleTrigger(PhraseTrigger):
    def evaluate(self, story):
        return self.is_phrase_in(story.get_title())

# Problem 4
# TODO: DescriptionTrigger
class DescriptionTrigger(PhraseTrigger):
    def evaluate(self, story):
        return self.is_phrase_in(story.get_description())

# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.
class TimeTrigger(Trigger):
    def __init__(self, time_string):
        time = datetime.strptime(time_string, "%d %b %Y %H:%M:%S")
        self.time = time
           
# Problem 6
# TODO: BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    def evaluate(self, story):
        pubdate = story.get_pubdate()
        return pubdate < self.time
            
class AfterTrigger(TimeTrigger):
    def evaluate(self, story):
        pubdate = story.get_pubdate()
        return pubdate > self.time

# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger = trigger
    
    def evaluate(self, story):
        return not self.trigger.evaluate(story)

# Problem 8
# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2
    
    def evaluate(self, story):
        return self.trigger1.evaluate(story) and self.trigger2.evaluate(story)

# Problem 9
# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2
    
    def evaluate(self, story):
        return self.trigger1.evaluate(story) or self.trigger2.evaluate(story)

```
