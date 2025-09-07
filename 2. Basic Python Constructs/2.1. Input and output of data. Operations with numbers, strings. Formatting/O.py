hours = int(input())
minutes = int(input())
delivery_time = int(input())

summary_time = hours * 60 + minutes + delivery_time
summary_time = summary_time % 1440

print(f'{summary_time // 60:02}:{summary_time % 60:02}')