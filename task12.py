#Shahar Engel

#!python3
import networkx as nx


class Agent:

    def __init__(self, name, pref, cur):
        self.name = name #str
        self.preferences = pref #list
        self.current_shift = cur #int
        self.new_shift = -1 #int


def exchange_shifts(workers): #(workers: List[Agents]) -> void
    """
    >>> agent1 = Agent("A", [3,2,4,1], 1)
    >>> agent2 = Agent("B", [1,4,3,2], 2)
    >>> agent3 = Agent("C", [1,4,2,3], 3)
    >>> agent4 = Agent("D", [3,4,2,1], 4)
    >>> workers = [agent1, agent2, agent3,agent4]
    >>> exchange_shifts(workers)
    A moves from shift 1 to shift 3
    B moves from shift 2 to shift 2
    C moves from shift 3 to shift 1
    D moves from shift 4 to shift 4
    >>> agent1 = Agent("A", [2,3,4,1], 1)
    >>> agent2 = Agent("B", [3,4,2,1], 2)
    >>> agent3 = Agent("C", [1,2,4,3], 3)
    >>> agent4 = Agent("D", [1,2,3,4], 4)
    >>> workers = [agent1, agent2, agent3,agent4]
    >>> exchange_shifts(workers)
    A moves from shift 1 to shift 2
    B moves from shift 2 to shift 3
    C moves from shift 3 to shift 1
    D moves from shift 4 to shift 4
    """
    nodes = []
    G = nx.DiGraph()
    for i in range(len(workers)):
        nodes.append(workers[i].current_shift)
        G.add_edge(workers[i].current_shift, workers[i].preferences[0])
    # print(list(G.edges))
    # print(G.size())
    while G.size() != 0:
        for cycle in nx.simple_cycles(G):
            for i in range(len(workers)):
                if workers[i].current_shift in cycle:
                    new = cycle.index(workers[i].current_shift)
                    if new == len(cycle)-1:
                        workers[i].new_shift = cycle[0]
                    else:
                        workers[i].new_shift = cycle[new+1]
                    nodes.remove(workers[i].current_shift)
                    G.remove_node(workers[i].current_shift)
            break

        # print(list(G.edges))
        # print(G.size())
        for i in range(len(workers)):
            if workers[i].new_shift == -1:
                pref = workers[i].preferences
                for j in range(len(workers[i].preferences)):
                    if pref[j] in nodes:
                        G.add_edge(workers[i].current_shift, workers[i].preferences[j])
                        break

    #print answer
    for i in range(len(workers)):
        print("{} {} {} {} {}".format(workers[i].name, "moves from shift", workers[i].current_shift, "to shift", workers[i].new_shift))


# agent1 = Agent("A", [3,2,4,1], 1)
# agent2 = Agent("B", [1,4,3,2], 2)
# agent3 = Agent("C", [1,4,2,3], 3)
# agent4 = Agent("D", [3,4,2,1], 4)
agent1 = Agent("A", [2,3,4,1], 1)
agent2 = Agent("B", [3,4,2,1], 2)
agent3 = Agent("C", [1,2,4,3], 3)
agent4 = Agent("D", [1,2,3,4], 4)
workers = [agent1, agent2, agent3,agent4]
exchange_shifts(workers)

if __name__ == '__main__':
    import doctest
    (failures, tests) = doctest.testmod(report=True)
    print ("{} failures, {} tests".format(failures, tests))