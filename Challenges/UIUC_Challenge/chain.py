import json

with open("/Users/aryank/Developer/DSA_Prep/Challenges/UIUC/challenge_info.json", "r") as f:
    data = json.load(f)


import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

for i in data["alliances"]:
    G.add_edge(i[0][6:], i[1][6:])


# Visualize the graph
pos = nx.circular_layout(G)  # Positioning of nodes
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=100,
    node_color="skyblue",
    font_size=10,
    font_color="black",
    font_weight="bold",
    arrowsize=10,
)
connected_components = list(nx.connected_components(G.to_undirected()))
print("Connected Components:")

maxGoodness = 0
bestGroup = None

for idx, component in enumerate(connected_components, 1):
    print(f"Group {idx}: {list(component)}")
    print(
        f"Goodness: {sum(data['people'][f'wizard{wizard}'] for wizard in component)}"
    )
    if sum(data["people"][f"wizard{wizard}"] for wizard in component) > maxGoodness:
        maxGoodness = sum(data["people"][f"wizard{wizard}"] for wizard in component)
        bestGroup = component


print("-------------------------------------")
print(maxGoodness)
print(bestGroup)

# Show the plot
plt.show()
