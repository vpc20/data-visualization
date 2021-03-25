import networkx as nx
import matplotlib.pyplot as plt

# __all__ = ['bipartite_layout',
#            'circular_layout',
#            'kamada_kawai_layout',
#            'random_layout',
#            'rescale_layout',
#            'shell_layout',
#            'spring_layout',
#            'spectral_layout',
#            'planar_layout',
#            'fruchterman_reingold_layout',
#            'spiral_layout']


# G = nx.dodecahedral_graph()
# nx.draw_networkx(G)
# plt.show(nx)

# g = nx.Graph()
# # Cormen book example dfs
# # g.add_edges_from([('u', 'v'), ('u', 'x'), ('v', 'y'), ('x', 'v'), ('y', 'x'), ('w', 'y'), ('w', 'z'), ('z', 'z')])
# # dg.add_edges_from([('m', 'q'), ('m', 'r'), ('m', 'x'), ('n', 'o'), ('n', 'q'), ('n', 'u'),
# #                   ('o', 'r'), ('o', 's'), ('o', 'v'), ('p', 'o'), ('p', 's'), ('p', 'z'), ('q', 't'),
# #                   ('r', 'u'), ('r', 'y'), ('s', 'r'), ('v', 'w'), ('v', 'x'), ('y', 'v')])
# # g.add_edges_from([(1, 5), (1, 6), (2, 6), (2, 7), (3, 7), (3, 8), (4, 8), (4, 9),
# #                   (5, 10), (5, 11), (6, 11), (6, 12), (7, 12), (7, 13), (8, 13), (8, 14), (9, 14),
# #                   (10, 15), (11, 15), (11, 16), (12, 16), (12, 17), (13, 17), (13, 18), (14, 18), (14, 19),
# #                   (15, 20), (16, 20), (16, 21), (17, 21), (17, 22), (18, 22), (18, 23), (19, 23)
# #                   ])
# g.add_nodes_from([0, 1, 2, 3])
# g.add_edges_from([(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)])
#
# # layout = nx.planar_layout(g)
# # layout = nx.shell_layout(g)
# layout = nx.spring_layout(g)
# # print(layout)
# nx.draw_networkx(g, layout, node_size=750, node_color='y')
# plt.show(nx)


# g = nx.Graph()
# g.add_nodes_from([0, 1, 2, 3])
# g.add_edges_from([(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)])
# layout = nx.spring_layout(g)
# nx.draw_networkx(g, layout, node_size=750, node_color='y')
# plt.show(nx)

dg = nx.DiGraph()
dg.add_nodes_from([0, 1, 2, 3, 4])
dg.add_edges_from([(0, 1), (1, 2), (2, 1), (1, 3), (3, 4)])
layout = nx.spring_layout(dg)
nx.draw_networkx(dg, layout, node_size=750, node_color='y')
plt.show(nx)

# for u, v in list(nx.eulerian_path(g, 5))[::-1]:
#     print(f'({v}, {u}) ', end=' ')
# print(g.edges)
# nx.write_gml(g, r'c:\temp\test.gml')
