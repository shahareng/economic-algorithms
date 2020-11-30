# Shahar Engel
# חתימות הפונקציות שלי נראות כך (ולא כמו במטלה) כי גרסת הפייתון שלי לא תומכת בחתימות של המטלה

class Agent:

    def __init__(self, name, values):
        self.name = name
        self.values = values


     # נעזרתי בעמית רן כדי להבין איך לממש את פונקציה זו
    def value(self, option):
        return self.values[option-1]



def isParetoImprovement(agents, option1, option2):
    ans = 0 # check if it is the same option
    for agent in agents:
        op1 = agent.value(option1) # value of option1
        op2 = agent.value(option2) # value of option2
        # if op1 < op2 for sure it isn't pareto improvement
        if op1 < op2:
            return False
        # check if it is the same option
        elif op1 == op2:
            ans+=1

    if ans == len(agents):
        return False

    return True


def isParetoOptimal(agents, option, allOptions):
    # pass over all the option and check if there is option that pareto improvement for the given option
    for op in allOptions:
        ans = isParetoImprovement(agents, op, option)
        # if there is pareto improvement
        if (ans):
            return False

    return True


# main
agent1 = Agent("Ami", [1,2,3,4,5])
agent2 = Agent("Tami", [3,1,2,5,4])
agent3 = Agent("Rami", [3,5,5,1,1])
agents = [agent1, agent2, agent3]
opt1 = 3
opt2 = 2

print(isParetoImprovement(agents, opt1, opt2))
print (isParetoOptimal(agents, 3, [1,2,3,4,5]))
