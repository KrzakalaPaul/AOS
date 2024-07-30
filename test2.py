import seaborn as sns
glue = sns.load_dataset("glue").pivot(index="Model", columns="Task", values="Score")

print(glue)