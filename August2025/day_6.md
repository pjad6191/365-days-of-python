## August 14, 2025 - Day 6

### What I Worked On:  
- I wanted to get down when to use parentheses vs single brackets vs double brackets in Pandas, so I had ChatGPT make a mini chart showing when to use each. It is definitely helpful, and I think now that I have analyzed and thought about it, it will be a lot easier. 

### Concepts Learned/Practiced:  
- **DataFrames - Selection** in **Pandas**
       
### What I Found Challenging:  
- Creating a table in this Github file! 

### Key Accomplishments:  
- Got more hands on experience with DataFrames in Pandas
    
### Resources Used:  
- ChatGPT
- **_Python for Data Analysis_** by Wes McKinney, Chapter 5 

### Reflections/Insights:
- We lost power for a good portion of the day, so I used it for some reading time  
  
### Next Steps/Plans for Tomorrow: 
- Continue practicing with Pandas


### Table from ChatGPT 

| Method                  | Row selection                                | Column selection                         | Example                                         | Returns                                      |
|-------------------------|-----------------------------------------------|--------------------------------------------|-------------------------------------------------|----------------------------------------------|
| [] (single brackets)    | N/A (all rows) or boolean mask                | One column by name                         | `df['age']`                                     | Series (use `[['age']]` for DataFrame)       |
| [[]] (double brackets)  | N/A (all rows) or boolean mask                | Multiple columns by name                   | `df[['name', 'city']]`                          | DataFrame                                    |
| .loc[label, label]      | Explicit labels list (non-contiguous)         | Explicit names list (non-contiguous)       | `df.loc[[2, 5, 9], ['name', 'city']]`           | DataFrame                                    |
| .loc[cond, label]       | Boolean condition                             | Names list or single name                  | `df.loc[df['age'] > 30, ['name', 'city']]`      | DataFrame (Series if single column name)     |
| .loc[slice, slice]      | Label slice (inclusive)                       | Name slice (inclusive)                     | `df.loc['A':'C', 'age':'city']`                 | DataFrame                                    |
| .iloc[pos, pos]         | Positions list (non-contiguous)               | Positions list (non-contiguous)            | `df.iloc[[0, 3, 7], [1, 4]]`                    | DataFrame                                    |
| .iloc[slice, slice]     | Position slice (end-exclusive)                | Position slice (end-exclusive)             | `df.iloc[0:5, 1:3]`                             | DataFrame                                    |
| .loc[:, label]          | All rows                                      | Single name or list of names               | `df.loc[:, ['age', 'city']]`                    | DataFrame (Series if single name)            |
| .iloc[:, pos]           | All rows                                      | Single position or list of positions       | `df.iloc[:, [0, 2]]`                            | DataFrame (Series if single position)        |
| .at[label, name] / .iat[pos, pos] | Single label / single position       | Single name / single position              | `df.at[5, 'age']`  |   `df.iat[0, 1]`            | Scalar (fast lookups)                        |
| .reindex(index=..., columns=...)  | Arbitrary labels (adds NaN if missing)| Arbitrary names (adds NaN if missing)      | `df.reindex(index=[9,2,5], columns=['city','age'])` | DataFrame (keeps order you pass)         |
| .filter(items=..., like=..., regex=...) | N/A                            | Pattern or explicit list                    | `df.filter(regex='^score_')`                    | DataFrame                                    |
