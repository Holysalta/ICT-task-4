from random import randint
def rollPairOfDice():
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    roll = dice1 + dice2
    return roll

def generate_expected_values():
    matrix = [[0 for x in range(6)] for y in range(6)]
    for i in range(6):
        for j in range(6):
            matrix[i][j] = i + 1 + j + 1
    keys = []
    values = []
    for k in range(2,13):
        count = 0
        keys.append(str(k))
        for i in range(6):
            for j in range(6):
                if(matrix[i][j] == k):
                    count+=1
        values.append(round((count / 36) * 100, 2))
    expected_values = {k:v for k,v in zip(keys, values)}

    return expected_values

def run_simulation():
    keys = []
    values = [0] * 11
    for k in range(2,13):
            keys.append(str(k))   
    n = 1000 #count of experiments
    for i in range(n):
        dice_roll = rollPairOfDice()
        for k in range(2,13):
            if(dice_roll == k):
                values[k-2] += 1
    for i in range(len(values)):
        values[i] = values[i] / (n / 100)
    simulated_percent = {k:v for k,v in zip(keys, values)}

    return simulated_percent

simulation_result = run_simulation()
generated_expected_values = generate_expected_values()
print('Total', '              Simulated percent', '                Expected percent')
print("---------------------------------------------------------------")
for key in simulation_result:
    print ("%s:\t\t\t%f\t\t%s" % (key , simulation_result[key], expected_values[key]))

