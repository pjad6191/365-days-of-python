## August 16, 2025 - Day 8

### What I Worked On:  
- Continued with the kaggle course on Pandas 

### Concepts Learned/Practiced:  
- **Pandas DataFrames: Indexing, Selecting & Assigning**
       
### What I Found Challenging:  
- I felt like I had a grasp on selecting, but kaggle introduced some new things to think about for me. The course was very helpful though. 

### Key Accomplishments:  
- Got more hands on experience with DataFrames in Pandas
    
### Resources Used:  
- **[Kaggle's Pandas Course](https://www.kaggle.com/learn/pandas)**
- **_Python for Data Analysis_** by Wes McKinney, Chapter 5 

### Reflections/Insights:
- I feel like this kaggle course has been the most helpful so far. It breaks things down and then gives you a chance to practice. It's better than just reading or watching or making up my own datasets. I get problems to work on and yet it's stuff I just learned/reviewed, so it's relevant and helps the material stick better.  
  
### Next Steps/Plans for Tomorrow: 
- Continue practicing selection in Pandas

### Sample Selecting & Indexing: 

```python

import pandas as pd

cols = ["country", "variety"]
frame = reviews.loc[:99,cols]

top_oceania_wines = reviews.loc[(reviews.country.isin(['Australia', 'New Zealand'])) & (reviews.points >= 95)]
```
