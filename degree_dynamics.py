import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import os
from natsort import natsorted
import imageio

def rs(seq, m):
    targets = set()
    while len(targets) < m:
        x = np.random.choice(seq)
        targets.add(x)
    return targets

def network(m0 = 100, m= 20, num_iter = 100, i_node = 101):
    """
    :param m0: initial number of node
    :param m: constant link number of the new node added to the network
    :param num_iter: the number of new nodes to add
    :param i_node: the node that to analyze
    :return:
    """
    G = nx.barabasi_albert_graph(m0, m)
    repeated_nodes = [n for n, d in G.degree() for _ in range(d)]
    print(len(G.nodes), len(G.edges))
    degree_list = []
    degree_list_approx = []

    for i in range(num_iter):
        colors = [(0.0, 0.0, 1.0, 1.0)] * (len(G.nodes))
        targets = rs(repeated_nodes, m)
        G.add_edges_from(zip([len(G.nodes)] * m, targets))
        colors.append((1.0, 0.0, 0.0, 1.0))
        repeated_nodes = [n for n, d in G.degree() for _ in range(d)]
        if i_node > len(G.nodes):
            continue
        degree_list.append(G.degree[i_node - 1])
        degree_list_approx.append(m*np.sqrt((i_node + i)/(i_node-1)))

        if (i+1) % 50 == 0:
            plt.figure(figsize=(10, 5))
            plt.subplot(1,2,1)
            nx.draw(G, node_size = 40, node_color=colors)
            plt.subplot(1,2,2)
            plt.plot(degree_list, "ro")
            plt.plot(degree_list_approx, "k")
            plt.xlabel("t (s)")
            plt.ylabel("k(t)")
            plt.xlim([0, num_iter])
            plt.ylim([0, m*np.sqrt(((i_node + num_iter))/(i_node - 1))+50])
            plt.legend(["Actual Degree", "Found Degree"])
            plt.savefig("./gif/{:d}.png".format(i+1))
            # plt.show()
    print(len(G.nodes), len(G.edges))

def gif():
    a = os.listdir("./gif/")
    a = natsorted(a)
    with imageio.get_writer("out.gif", fps=2) as writer:
        for i in range(len(a)):
            image = imageio.imread("./gif/"+a[i])
            writer.append_data(image)

if __name__ == '__main__':
    network(m0=100, m=50, num_iter=1000, i_node=105)
    # to make gif, after network() function was runned, comment the network function above and uncomment the line below
    # gif()