## August 21, 2025 - Day 13

### What I Worked On:  
- Pandas with ChatGPT

### Concepts Practiced:  
- **Pandas DataFrames**: 
    - Filtering & Adding Columns Review 
    - Sorting Values
    - Grouping 
    - Missing Data 
       
### What I Found Challenging:  
- I think I have found my best way of learning Pandas. The ChatGPT tutor is "chef's kiss". It give me just the right amount of challenge, but not too much. 

### Key Accomplishments:  
- Became comfortable with sort_values() and groupby()
    
### Resources Used:  
- **ChatGPT**

### Reflections/Insights:
- I enjoy learning a lot more and can practice longer with this method of using ChatGPT. I can review past concepts to keep it fresh while adding to my repertoire. 
  
### Next Steps/Plans for Tomorrow: 
- Continue practicing Pandas with ChatGPT. 

### Example Code: 
```python

#Filtering and Adding Columns Review:
table[(table["passed"] == True) & (table["honor_roll"] == False)] 
table["extra_help"] = table["Age"] > 10

#Sorting:
table.sort_values(by=["passed", "age"], ascending=[True, False])
table.sort_values(by=["grade", "age"], ascending=[True, True], inplace=True)

#Grouping:
table.groupby("passed").agg({"age":"mean", "name":"count"})
table.groupby(["honor_roll", "grade"]).agg({"age":"mean", "name":"count"})

#Easier to read:
table.groupby(["HonorRoll", "Grade"]).agg({
    "Age":"mean", 
    "Name":"count"
}).rename(columns={
    "Age":"AverageAge", 
    "Name":"StudentCount"
}).reset_index()

#Count missing values per column:
table.isna().sum()

#Filling in missing ages with the average age:
table["age"] = table["age"].fillna(table["age"].mean())

```

