#Shahar Engel

from doctest import testmod

class Uniform:
    # low- float
    # high- float

    def __init__(self, low, high):
        self.low = low
        self.high = high


def max_revenue_auction1(agent1, value1): #agent1: Uniform, value1:float
    '''
    >>> max_revenue_auction1(Uniform(10,30), 15)
    Agent chosen and pays 15
    ok
    >>> max_revenue_auction1(Uniform(20,40), 20.91)
    Agent chosen and pays 20
    ok
    >>> max_revenue_auction1(Uniform(10,30), 10)
    Agent chosen and pays 15
    failed
    '''

    high = agent1.high
    treshold = high/2;
    rv = (2*value1)-high
    if rv >= 0:
        print("{} {}".format("Agent chosen and pays", treshold))
    else:
        print("Agent doesn't chosen")


def max_revenue_auction2(agent1, agent2, value1, value2): #agent1: Uniform, agent2: Uniform, value1:float, value2:float
    '''
    >>> max_revenue_auction2(Uniform(10,30), Uniform(20,40), 23,27)
    Agent 1 wins and pays 22
    ok
    >>> max_revenue_auction2(Uniform(10,30), Uniform(20,40), 15.33, 30.35)
    Agent 2 wins and pays 20.33
    ok
    >>> max_revenue_auction2(Uniform(10,30), Uniform(20,40), 23,27)
    Agent 2 wins and pays 15
    failed
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
        print("{} {}".format("Agent 1 wins and pays", pay))
    elif rv2>rv1 and rv2 > 0:
        pay = max(treshold2, (high2 + rv1)/2)
        print("{} {}".format("Agent 2 wins and pays", pay))


#main
agent1 = Uniform(10,30)
agent2 = Uniform(20,40)
max_revenue_auction1(agent1, 15.01)
max_revenue_auction2(agent1, agent2, 15.33, 30.35)

# call the testmod function
# if __name__ == '__main__':
   # testmod(name='max_revenue_auction1', verbose=True)
   # testmod(name='max_revenue_auction2', verbose=True)
