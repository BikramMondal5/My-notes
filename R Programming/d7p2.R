data = read.csv("sample.csv")

name = data$name
write.csv(name, "names.csv")

print(data)

min_salary = min(data$salary)
max_salary = max(data$salary)

print(paste("The salary ranges between", min_salary, "and", max_salary))
for (i in 1:nrow(data)) {
  salary = data$salary[i]
  if (salary >= 30000 && salary <= 50000) {
    print(data$name[i])
  }
}

print(paste("The maximum salary is",max_salary))

IT_index = which(data$department == "IT")
IT_employees = data$name[IT_index]
print(IT_employees)
