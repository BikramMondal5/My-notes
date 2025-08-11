# 8. str = "Python is amazing. Python is powerful."
s = "Python is amazing. Python is powerful."
# a) Position of 'Python' (first and second)
first_pos = s.find("Python")
second_pos = s.find("Python", first_pos + 1)
print(first_pos, second_pos)
# b) Using rfind to get last position of 'Python'
print(s.rfind("Python"))
# c) Replace 'Python' with 'Java'
print(s.replace("Python", "Java"))
# d) Count number of 'p'
print(s.lower().count("p"))