## August 24, 2025 - Day 16

### What I Worked On:  
- Pandas with ChatGPT

### Concepts Practiced:  
- **Pandas DataFrames**: 
    - Examining a dataset 
          
### Resources Used:  
- **ChatGPT**

### Reflections/Insights:
-   I wanted to practice going through a dataset to come up with my own person algorithm for examining a dataset to gain insight. 
  
### Next Steps/Plans for Tomorrow: 
- Continue practicing Pandas with ChatGPT. 

### Example Code: 
```python

import pandas as pd

#Create an example DataFrame
df = pd.DataFrame({
    "PatientID": [101, 102, 103, 104, 105],
    "Age": [45, 52, 36, 28, None],
    "Sex": ["F", "M", "F", "F", "M"],
    "Diagnosis": ["Hypertension", "Diabetes", "Hypertension", "None", "Diabetes"],
    "BP_Sys": [140, 160, 135, 120, None],
    "BP_Dia": [90, 100, 85, 80, None],
    "Smoker": ["Yes", "No", "Yes", "No", "Yes"]
})

#Take a look at the data
df.info()
df.describe()

#Fill in the missing values with the average:
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["BP_Sys"] = df["BP_Sys"].fillna(df["BP_Sys"].mean())
df["BP_Dia"] = df["BP_Dia"].fillna(df["BP_Dia"].mean())

#Average systolic blood pressure for smokers vs nonsmokers
df.groupby("Smoker").agg({"BP_Sys": "mean"})

#Count how many of each diagnosis:
df["Diagnosis"].value_counts()

#Compare avg BP by diagnosis:
df.groupby("Diagnosis").agg({"BP_Sys": "mean", "BP_Dia": "mean"})

```

