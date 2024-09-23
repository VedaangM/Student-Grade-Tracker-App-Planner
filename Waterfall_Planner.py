import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

tasks = [
    {'Task': 'Requirements Analysis', 'Start': '2024-10-01', 'End': '2024-10-10'},
    {'Task': 'System Design', 'Start': '2024-10-05', 'End': '2024-10-20'},
    {'Task': 'Frontend Development', 'Start': '2024-10-15', 'End': '2024-11-05'},
    {'Task': 'Backend Development', 'Start': '2024-10-22', 'End': '2024-11-12'},
    {'Task': 'Database Development', 'Start': '2024-10-20', 'End': '2024-10-27'},
    {'Task': 'Finalization and Testing', 'Start': '2024-11-01', 'End': '2024-11-20'},
    {'Task': 'Deployment', 'Start': '2024-11-18', 'End': '2024-11-25'},
    {'Task': 'Maintenance', 'Start': '2024-11-25', 'End': '2024-12-31'}  
]


df = pd.DataFrame(tasks)


df['Start'] = pd.to_datetime(df['Start'])
df['End'] = pd.to_datetime(df['End'])

# Set up the Gantt chart figure
fig, ax = plt.subplots(figsize=(10, 6))

# Loop through the tasks and plot the Gantt bars
for i, task in df.iterrows():
    ax.barh(task['Task'], (task['End'] - task['Start']).days, left=task['Start'], color=f'C{i}')

# Set the labels and title
ax.set_xlabel('Date')
ax.set_ylabel('Tasks')
ax.set_title('Gantt Chart for Student Grade Tracking App (Starting October 1st)')

ax.xaxis_date()
fig.autofmt_xdate()

plt.show()
