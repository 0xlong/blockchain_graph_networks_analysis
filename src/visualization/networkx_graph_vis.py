import networkx as nx



def wallet_network(df):
    plt.figure(figsize=(12, 12))
    G = nx.DiGraph()
    G = nx.from_pandas_edgelist(df, 'from', 'to')

    nx.draw_random(G, with_labels=False)
    
    #filtering based on last letter, if it is 8
    for x in G.nodes:
        if x.endswith('8'):
            G.nodes[x]['color']='red'
        else:
            G.nodes[x]['color']='green'
    
    nt = Network("800px", width="100%", directed=True)
    nt.from_nx(G)
    nt.show_buttons(filter_=['physics'])

    nt.show("nx.html")
    
    return plt.show(G)