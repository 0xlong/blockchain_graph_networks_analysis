import networkx as nx

def draw_graph(df, type):

    # Networkx graph constructor
    G = nx.DiGraph()
    G = nx.from_pandas_edgelist(df, 'from', 'to')

    return nx.draw_random(G, with_labels=False)