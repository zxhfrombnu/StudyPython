def health_calculator(age, apples_ate, cigs_smoked):
    answer = (100 - age) + (apples_ate * 3.5) - (cigs_smoked * 2)
    print(answer)

bucky_data = [27, 20, 0]
health_calculator(bucky_data[0], bucky_data[1], bucky_data[2])
health_calculator(*bucky_data)