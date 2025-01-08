import pandas as pd

screen_time = [2, 4, 6, 7, 1]
sleep_hours = [8, 7, 6, 4, 9]
study_hours = [3, 5, 2, 1, 4]
exercise_hours = [1, 2, 0, 1, 3]
stu_name = ["Alice", "Mike", "Raju", "Sophia", "John"]

dic1 = {
    "stu_name": stu_name,
    "screen_time": screen_time,
    "sleep_hours": sleep_hours,
    "study_hours": study_hours,
    "exercise_hours": exercise_hours
}

print(dic1)

df = pd.DataFrame(dic1)
print(df)

