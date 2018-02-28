import networkx as nx
import sys


def max_congestion(G):
    num_of_nodes = G.number_of_nodes()
    max_value = 0
    for x in range(num_of_nodes):
        if G.degree(x) <= max_value:
            continue
        elif G.degree(x) == 1:
            max_value = 1
            continue
        for y in range(x+1, num_of_nodes):
            if G.degree(y) <= max_value:
                continue
            elif G.degree(y) == 1:
                max_value = 1
                continue
            else:
                current_value = nx.maximum_flow_value(G, x, y)
                if max_value < current_value:
                    max_value = current_value
                if G.degree(x) <= max_value:
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
    order_of_graph = sys.stdin.readline()
    order_of_graph = int(order_of_graph[:-1])
    while order_of_graph != 0:
        G = nx.Graph()
        for i in range(order_of_graph):
            G.add_node(i)
            edges = sys.stdin.readline().split()
            for e in edges:
                if G.has_edge(int(e), i):
                    continue
                G.add_edge(i, int(e), capacity=1)
        max_congestion(G)
        order_of_graph = sys.stdin.readline()
        if '\n' in order_of_graph:
            order_of_graph = int(order_of_graph[:-1])
        else:
            order_of_graph = int(order_of_graph)


main()


