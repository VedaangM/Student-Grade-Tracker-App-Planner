import matplotlib.pyplot as plt
import pandas as pd

sprints = ['Sprint 1', 'Sprint 2', 'Sprint 3', 'Sprint 4']
total_story_points = [30, 40, 35, 25]  
completed_story_points = [10, 25, 30, 20]  


remaining_story_points = [total - completed for total, completed in zip(total_story_points, completed_story_points)]


data = {
    'Sprint': sprints,
    'Total': total_story_points,
    'Completed': completed_story_points,
    'Remaining': remaining_story_points
}

df = pd.DataFrame(data)


plt.figure(figsize=(10, 6))

plt.plot(df['Sprint'], df['Total'], marker='o', label='Total Story Points', color='blue')
plt.plot(df['Sprint'], df['Completed'], marker='o', label='Completed Story Points', color='green')
plt.plot(df['Sprint'], df['Remaining'], marker='o', label='Remaining Story Points', color='red')


plt.title('Agile Burndown Chart')
plt.xlabel('Sprint')
plt.ylabel('Story Points')
plt.xticks(rotation=45)
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
