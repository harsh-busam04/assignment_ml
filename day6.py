#day 6

import pandas as pd

data = {
    "Name": ["John", "Alice", "Bob", "Diana"],
    "Age": [28, 34, 23, 29],
    "Department": ["HR", "IT", "Marketing", "Finance"],
    "Salary": [45000, 60000, 35000, 50000],
}
df = pd.DataFrame(data)

print(df.head(2))

df["Bonus"] = df["Salary"] * 0.10
print(df)

average_salary = df["Salary"].mean()
print(average_salary)

filtered_employees = df[df["Age"] > 25]
print(filtered_employees)
