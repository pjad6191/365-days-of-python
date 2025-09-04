## September 3, 2025 - Day 26

### What I Worked On:  
- I did something different today. I went back to the Sleep dataset and walked through analyzing it and making some conclusions about the data. 
  
### Concepts Practiced:  
- Analyzing a dataset
- Graphing
    - Scatter plots
    - Bar charts
           
### What I Found Challenging:  
- Figuring out where to start was a challenge. Plus, I seemed to only disprove any hypotheses I had. 

### Key Accomplishments:  
- Analyzed a dataset. 
    
### Resources Used:  
- **ChatGPT**
- **Kaggle**
  
### Reflections/Insights:
- I wanted to put some of my skills to work. I analyzed some data. I started with simple bar charts,and then chatgpt helped me with some more sophisticated graphs.  
  
### Next Steps/Plans for Tomorrow: 
- Continue with chatGPT review

### Example Code: 
```python
#how many total missing values do we have? 
total_cells = np.product(df.shape)
total_missing = missing_values_count.sum()

#percent of data that is missing
percent_missing = (total_missing / total_cells)*100

print(percent_missing)

df.groupby("Sleep_Hours")["Stroop_Task_Reaction_Time"].mean().plot(kind="bar")
plt.title("Reaction Time by Sleep Hours")
plt.show()

df.groupby("Sleep_Hours")["Daytime_Sleepiness"].mean()

df.groupby("Sleep_Hours")["Daytime_Sleepiness"].mean().plot(kind="bar")
plt.title("Sleep Hours vs Daytime Sleepiness")
plt.show()

plt.figure(figsize=(8, 5))
sns.regplot(x="Sleep_Hours", y="PVT_Reaction_Time", data=df, scatter_kws={"s": 50}, line_kws={"color": "red"})
plt.title("Sleep Hours vs. PVT Reaction Time")
plt.xlabel("Sleep Hours")
plt.ylabel("PVT Reaction Time (ms)")
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
scatter = plt.scatter(df["Sleep_Hours"], df["PVT_Reaction_Time"],
                      c=df["Sleep_Quality_Score"], cmap="viridis", s=60)
plt.xlabel("Sleep Hours")
plt.ylabel("PVT Reaction Time (ms)")
plt.title("Sleep Hours vs. PVT Reaction Time (colored by Sleep Quality)")
plt.colorbar(scatter, label="Sleep Quality Score")
plt.grid(True)
plt.tight_layout()
plt.show()

```
