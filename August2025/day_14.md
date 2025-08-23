## August 22, 2025 - Day 14

### What I Worked On:  
- Pandas with ChatGPT

### Concepts Practiced:  
- **Pandas DataFrames**: 
    - Dropping missing data - Remove rows with NaN values
    - Merging tables
       
### What I Found Challenging:  
- Pandas is getting easier, so there wasn't much challenge today. Honestly I thought filtering was harder.  

### Key Accomplishments:  
- Completed two full weeks of practicing Python every day. 
    
### Resources Used:  
- **ChatGPT**

### Reflections/Insights:
- I am proud that I finished two weeks of doing this everyday, and it's becoming a lot easier. I don't plan on stopping. 
  
### Next Steps/Plans for Tomorrow: 
- Continue practicing Pandas with ChatGPT. 

### Example Code: 
```python

#Dropping missing values, but keeps rows with at least 3 non-Nan values:
table.dropna(thresh=3)

#Merging two tables with different column names:
pd.merge(students, grades, left_on="StudentID", right_on="ID")

#Merging with mismatched keys, left join, renaming & dropping a column:
table = pd.merge(students, grades, left_on="StudentID", right_on="ID", how="left")
table = table.rename(columns={"Grade":"FinalGrade"})
table = table.drop(columns=['ID'])

```

