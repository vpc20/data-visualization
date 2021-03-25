from graphviz import Digraph

bt = Digraph()

# bt.node('1')
# bt.node('2')
# bt.node('3')

bt.edges(['12', '13'])
bt.render('temp.gv', view=True)

