# Shahar Engel


def choices(values): # (values: List[float]) -> List[bool]
    choice = []
    # choose the 3 largest values
    for i in range(len(values)):
        choice.insert(i, 0)
    sort1 = [x for x in values]
    sort1.sort(reverse=True)
    max1 = sort1[0]
    max2 = sort1[1]
    max3 = sort1[2]

    choice[values.index(max1)] = 1
    choice[values.index(max2)] = 1
    choice[values.index(max3)] = 1

    # choose the number that large than 10
    # for i in range(len(values)):
    #     if values[i] > 10:
    #         choice.insert(i, 1)
    #     else:
    #         choice.insert(i, 0)

    # choose the 2nd large value
    # for i in range(len(values)):
    #     choice.insert(i, 0)
    # sort1 = [x for x in values]
    # sort1.sort(reverse=True)
    # choice[values.index(sort1[1])] = 1
    return choice


def payments(values): # (values: List[float]) -> List[float]
    list_len = len(values)
    choice = choices(values)
    i = 0
    pay = [] # list of payments
    values2 = [x for x in values]
    # check if the rule-choice is monotonous
    for i in range(list_len):
        j = 0
        if choice[i] == 1:
            while choice[i] == 1 and j < 10:
                values[i] += 50
                choice = choices(values)
                j += 1
            if j < 10:
                raise Exception("The rule of choice is not monotonous")

    # check the payments
    for i in range(list_len):
        if choice[i] == 0:
            pay.insert(i, 0)
        else:
            while choice[i] == 1:
                values2[i] -= 0.001
                choice = choices(values2)
            pay.insert(i, values2[i])

    return pay


# main
list = [5,8,9,10.01,3,2,11,7,6]
print(payments(list))