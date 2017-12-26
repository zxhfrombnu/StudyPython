def drop_first_last(grades) :
    first, *middle, last = grades
    avg = sum(middle)/len(middle)
    print(avg)

# date, name, price = ['December 23 2015', 'Bread', 8.51]

grades = [65,76,98,54,21]
grades.sort()
drop_first_last(grades)
# drop_first_last([65,76,98,54,21])