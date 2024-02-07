data = {"alliances":[["wizard11","wizard38"],["wizard23","wizard8"],["wizard43","wizard6"],["wizard4","wizard42"],["wizard36","wizard24"],["wizard29","wizard51"],["wizard1","wizard26"],["wizard22","wizard16"],["wizard34","wizard31"],["wizard15","wizard41"],["wizard42","wizard10"],["wizard46","wizard13"],["wizard38","wizard36"],["wizard45","wizard50"],["wizard49","wizard21"],["wizard24","wizard9"],["wizard16","wizard32"],["wizard25","wizard7"],["wizard44","wizard28"],["wizard47","wizard45"],["wizard7","wizard11"],["wizard9","wizard18"],["wizard17","wizard2"],["wizard20","wizard17"],["wizard13","wizard33"],["wizard32","wizard34"],["wizard26","wizard30"],["wizard3","wizard52"],["wizard50","wizard39"],["wizard27","wizard43"],["wizard40","wizard3"],["wizard10","wizard46"],["wizard19","wizard48"],["wizard37","wizard1"],["wizard8","wizard49"],["wizard31","wizard12"],["wizard28","wizard47"],["wizard48","wizard5"],["wizard41","wizard19"],["wizard35","wizard37"],["wizard18","wizard15"],["wizard52","wizard23"],["wizard30","wizard29"],["wizard14","wizard22"],["wizard6","wizard20"]],"wizards":{"wizard1":308,"wizard10":1562,"wizard11":1985,"wizard12":1192,"wizard13":375,"wizard14":-997,"wizard15":-1112,"wizard16":-695,"wizard17":390,"wizard18":180,"wizard19":-909,"wizard2":941,"wizard20":-1848,"wizard21":-741,"wizard22":814,"wizard23":-1563,"wizard24":-119,"wizard25":600,"wizard26":-160,"wizard27":-247,"wizard28":-437,"wizard29":-2014,"wizard3":339,"wizard30":1820,"wizard31":-439,"wizard32":1586,"wizard33":-1073,"wizard34":-1571,"wizard35":473,"wizard36":-1416,"wizard37":-2022,"wizard38":-1606,"wizard39":1793,"wizard4":-1128,"wizard40":996,"wizard41":-1833,"wizard42":-26,"wizard43":1597,"wizard44":1941,"wizard45":836,"wizard46":481,"wizard47":-460,"wizard48":-1038,"wizard49":702,"wizard5":-1552,"wizard50":410,"wizard51":-448,"wizard52":1976,"wizard6":2013,"wizard7":-449,"wizard8":-840,"wizard9":728}}


import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

for i in data["alliances"]:
    G.add_edge(i[0][6:], i[1][6:])



# Visualize the graph
pos = nx.circular_layout(G)  # Positioning of nodes
nx.draw(G, pos, with_labels=True, node_size=100, node_color="skyblue", font_size=10, font_color="black", font_weight="bold", arrowsize=10)
connected_components = list(nx.connected_components(G.to_undirected()))
print("Connected Components:")

maxGoodness = 0
bestGroup = None

for idx, component in enumerate(connected_components, 1):
    print(f"Group {idx}: {list(component)}")
    print(f"Goodness: {sum(data['wizards'][f'wizard{wizard}'] for wizard in component)}")
    if sum(data['wizards'][f'wizard{wizard}'] for wizard in component) > maxGoodness:
        maxGoodness = sum(data['wizards'][f'wizard{wizard}'] for wizard in component)
        bestGroup = component
        

print("-------------------------------------")
print(maxGoodness)
print(bestGroup)

# Show the plot
plt.show()
