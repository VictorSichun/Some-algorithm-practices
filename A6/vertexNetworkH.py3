import networkx as nx
import sys


order_of_graph = 0


def max_congestion(DG):
    global order_of_graph
    max_value = 0
    for x in range(order_of_graph):
        if DG.out_degree(x + 41) <= max_value:
            continue
        elif DG.out_degree(x + 41) == 1:
            max_value = 1
            continue
        for y in range(x+1, order_of_graph):
            if DG.out_degree(y + 41) <= max_value:
                continue
            elif DG.out_degree(y + 41) == 1:
                max_value = 1
                continue
            else:
                current_value = nx.maximum_flow_value(DG, x + 41, y)
                if max_value < current_value:
                    max_value = current_value
                if DG.out_degree(x + 41) <= max_value:
                    break
    print(max_value)


'''def ford_fulkerson(G, s, t):
    cap = 1
    G_f = nx.Graph()
    for e in G.edges():
        G_f.add_edge(e, flow=0)
        path = all_simple_paths(G_f, s, t)
        while len(path) > 0:
            max_value = '''


def main():
    global order_of_graph
    order_of_graph = sys.stdin.readline()
    order_of_graph = int(order_of_graph[:-1])
    while order_of_graph != 0:
        DG = nx.DiGraph()
        for i in range(order_of_graph):
            DG.add_node(i)
            DG.add_node(41+i)
            DG.add_edge(i, 41 + i, capacity=1)
            edges = sys.stdin.readline().split()
            for e in edges:
                DG.add_edge(i + 41, int(e), capacity=1)
        #print(DG.edges())
        max_congestion(DG)
        order_of_graph = sys.stdin.readline()
        if '\n' in order_of_graph:
            order_of_graph = int(order_of_graph[:-1])
        else:
            order_of_graph = int(order_of_graph)


main()


