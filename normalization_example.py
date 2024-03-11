salaries = [70000,60000,52000]
ages     = [45,44,40]
min_sal = min(salaries)
max_sal = max(salaries)
min_age,max_age = min(ages),max(ages)
normalize=lambda x,x_min,x_max: (x-x_min)/(x_max-x_min)
for i in range(len(salaries)):
  salaries[i] = normalize(salaries[i],min_sal,max_sal)
  ages[i] = normalize(ages[i],min_age,max_age)
  print(f"{salaries[i]} {ages[i]}")
