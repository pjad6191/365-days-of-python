## September 1, 2025 - Day 24

### What I Worked On:  
- Today was just a quick review of more plotting and a review of pandas groupby. 
  
### Concepts Practiced:  
- **Pandas**: 
    - Groupby
- **Graphing**: 
    - Scatter plots
    - Bar charts
    - Histograms
       
### What I Found Challenging:  
- I ran into an issue where I was getting an error saying that matplotlib didn't have an attribute of xlabel. I needed to import matplotlib.plylot as plt and that fixed it. 

### Key Accomplishments:  
- Started a new month
    
### Resources Used:  
- **ChatGPT**
  
### Reflections/Insights:
- I was a little frustrated that my plots were not coming out, but it was a simple fix. 
  
### Next Steps/Plans for Tomorrow: 
- Continue with chatGPT review

### Example Code: 
```python
df = pd.DataFrame({
    "Sex": ["F", "M", "F", "F", "M", "M"],
    "Smoker": ["Yes", "No", "No", "Yes", "Yes", "No"],
    "BP_Sys": [125, 140, 130, 135, 145, 138]
})

#Group by Sex
avg_bp = df.groupby("Sex")["BP_Sys"].mean()
avg_bp.plot(kind="bar", title="Average Systolic BP by Sex")
plt.xlabel("Sex")
plt.ylabel("BP_Sys")
plt.show()

#Group by Smoker Status
avg_bp_smoker = df.groupby("Smoker")["BP_Sys"].mean()
avg_bp_smoker.plot(kind="bar", title="Average Systolic BP - Smoker vs. Non-Smoker")
plt.xlabel("Smoker Status")
plt.ylabel("BP_Sys")
plt.show()

#Group by both
bp_grouped = df.groupby(["Sex", "Smoker"])["BP_Sys"].mean()
bp_grouped.plot(kind="bar", title="Average Systolic BP - Smoker vs. Non-Smoker")
plt.xlabel("Smoker Status")
plt.ylabel("BP_Sys")
plt.show()

```
