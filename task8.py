#Shahar Engel

class Uniform:
    # low- float
    # high- float

    def __init__(self, low, high):
        self.low = low
        self.high = high


def max_revenue_auction1(agent1, value1): #agent1: Uniform, value1:float
    """
    >>> max_revenue_auction1(Uniform(10,30), 17)
    Agent chosen and pays 15
    >>> max_revenue_auction1(Uniform(20,40), 20.91)
    Agent chosen and pays 20
    >>> max_revenue_auction1(Uniform(10,30), 10)
    Agent doesn't chosen
    """

    high = agent1.high
    treshold = high/2;
    rv = (2*value1)-high
    pay = max(treshold, agent1.low)
    if rv > 0:
        print("Agent chosen and pays " + str(pay))
    else:
        print("Agent doesn't chosen")


def max_revenue_auction2(agent1, agent2, value1, value2): #agent1: Uniform, agent2: Uniform, value1:float, value2:float
    '''
    >>> max_revenue_auction2(Uniform(10,30), Uniform(20,40), 23,27)
    Agent 1 wins and pays 22
    >>> max_revenue_auction2(Uniform(10,30), Uniform(20,40), 15.33, 30.35)
    Agent 2 wins and pays 20.33
    >>> max_revenue_auction2(Uniform(10,30), Uniform(20,40), 29.22, 20.61)
    Agent 1 wins and pays 15.61
    '''


    high1 = agent1.high
    rv1 = (2 * value1) - high1
    treshold1 = high1 / 2;
    high2 = agent2.high
    rv2 = (2 * value2) - high2
    treshold2 = high2 / 2;
    pay = 0
    if rv1 < 0 and rv2 < 0:
        print("No agent wins")
    elif rv1 > rv2 and rv1 > 0:
        pay = max(treshold1, (high1+rv2)/2)
        print("Agent 1 wins and pays " + str(pay))
    elif rv2>rv1 and rv2 > 0:
        pay = max(treshold2, (high2 + rv1)/2)
        print("Agent 2 wins and pays " + str(pay))


#main
agent1 = Uniform(10,30)
agent2 = Uniform(20,40)
# max_revenue_auction1(agent1, 31)
# max_revenue_auction2(agent1, agent2, 29.22, 20.61)
# max_revenue_auction2(agent1, agent2, 27.44, 39.51)

# call the testmod function
if __name__ == '__main__':
    import doctest
    (failures, tests) = doctest.testmod(report=True)
    print ("{} failures, {} tests".format(failures, tests))
