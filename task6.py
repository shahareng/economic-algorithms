#Shahar Engel

from doctest import testmod


class Agent:

    def __init__(self, name, values):
        self.name = name
        self.values = values


    def value(self, option):
        return self.values[option]


def vcg(agents, num_options):
    '''
    >>> vcg([Agent("Ami", [8,4,3]), Agent("Tami", [5,8,1]), Agent("Rami", [3,5,3])], 3)
    The chosen option is 2.
    Agent #0 pays  0
    Agent #1 pays  2
    Agent #2 pays  1
    ok
    >>> vcg([Agent("Ami", [7,0,0,0]), Agent("Tami", [0,8,0,0]), Agent("Rami", [0,0,4,0])], 4)
    The chosen option is 2.
    Agent #0 pays  0
    Agent #1 pays  7
    Agent #2 pays  0
    ok
    >>> vcg([Agent("Ami", [7,0,0,0]), Agent("Tami", [0,8,0,0]), Agent("Rami", [0,0,4,0])], 4)
    The chosen option is 2.
    Agent #0 pays  0
    Agent #1 pays  4
    Agent #2 pays  0
    failed
    '''

    max1=best_option=0
    list_sum=[0]
    for op in range(num_options):
        sum=0
        for agent in agents:
            sum += agent.value(op)
        list_sum.append(sum)
        if sum > max1:
            max1=sum
            best_option=op+1
    print("{} {}.".format("The chosen option is", best_option))

    i=0
    for agent in agents:
        max2=best_option_whitout=0
        for op in range(num_options):
            sum_without = list_sum[op+1]-agent.value(op)
            if sum_without>max2:
                max2=sum_without
                best_option_whitout=op+1
        if best_option==best_option_whitout:
            pay = 0
        else:
            pay = max2-(list_sum[best_option]-agent.value(best_option-1))
        print("{}{} {} {}".format("Agent #", i, "pays ", pay))
        i+=1


#main
agent1 = Agent("Ami", [8,4,3])
agent2 = Agent("Tami", [5,8,1])
agent3 = Agent("Rami", [3,5,3])
agent4 = Agent("Ami", [7,0,0,0])
agent5 = Agent("Tami", [0,8,0,0])
agent6 = Agent("Rami", [0,0,4,0])
agent7 = Agent("Ami", [0,10,20,30,21,31,41,52])
agent8 = Agent("Tami", [0,31,21,11,43,33,23,53])
agents1 = [agent1, agent2, agent3]
agents2 = [agent4, agent5, agent6]
agents3 = [agent7, agent8]
num1 = 3
num2 = 4
num3 = 8
vcg(agents3, num3)
#vcg(agents1, num1)
#vcg(agents2,num2)

# call the testmod function
#if __name__ == '__main__':
#    testmod(name='vcg', verbose=True)
