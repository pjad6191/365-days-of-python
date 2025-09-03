## September 2, 2025 - Day 25

### What I Worked On:  
- Parsing Dates
  
### Concepts Practiced:  
- Parsing dates
- to_datetime()
- Plotting the day of the month 
       
### What I Found Challenging:  
- I found it challenging to have the motivation to do this. I may be getting a little tired of the grind already. I need to take it easy on myself so that I can keep it going. 

### Key Accomplishments:  
- NA
    
### Resources Used:  
- **Kaggle: Data Cleaning**
  
### Reflections/Insights:
- I was tired of practicing today and wanted to do something different, so I just continued with the kaggle course. It was a fairly easy subject. I don't want to quit, so I need to take it easy on myself and just keep going until the motivation returns. 
  
### Next Steps/Plans for Tomorrow: 
- Continue with chatGPT review

### Example Code: 
```python
earthquakes.loc[3378, "Date"] = "02/23/1975"
earthquakes.loc[7512, "Date"] = "04/28/1985"
earthquakes.loc[20650, "Date"] = "03/13/2011"
earthquakes['date_parsed'] = pd.to_datetime(earthquakes['Date'], format="%m/%d/%Y")

day_of_month_earthquakes = earthquakes['date_parsed'].dt.day
```
