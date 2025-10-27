## October 27, 2025 - Day 80

### What I Worked On:  
- Exercism - Created functions to: Find the difference between the square of the sum and the sum of the squares of the first N natural numbers.
- Worked on Problem Set 5, Parts 9-11 from Intro to Computer Programming in Python. 

### Concepts Practiced:  
- Object oriented programming
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
- [Problem 5](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/ps5/)
  
### Code: 
```python
#Exercism Code:
def square_of_sum(number):
    if number == 0:
        return 0 
    sum = 0
    for num in range(1, number+1):
        sum+=num
    return sum**2

def sum_of_squares(number):
    if number == 0:
        return 0
    sum = 0
    for num in range(1, number+1):
        sum += num**2
    return sum 

def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)



#Problem Set 5:
NA
```
