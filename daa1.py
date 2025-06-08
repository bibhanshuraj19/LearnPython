import matplotlib.pyplot as plt
import networkx as nx

# Create a graph for the Karatsuba algorithm computation
G = nx.DiGraph()

# Add nodes for the main problem and subproblems
G.add_node("1212 x 2121")
G.add_node("12 x 21 (a x c)")
G.add_node("12 x 21 (b x d)")
G.add_node("(12+12)(21+21) - a*c - b*d")

# Connect main problem to subproblems
G.add_edges_from([
    ("1212 x 2121", "12 x 21 (a x c)"),
    ("1212 x 2121", "12 x 21 (b x d)"),
    ("1212 x 2121", "(12+12)(21+21) - a*c - b*d")
])

# Add nodes for final results of a*c, b*d, and cross-term computation
G.add_node("Result a x c")
G.add_node("Result b x d")
G.add_node("Cross-term result")

# Connect subproblems to their results
G.add_edges_from([
    ("12 x 21 (a x c)", "Result a x c"),
    ("12 x 21 (b x d)", "Result b x d"),
    ("(12+12)(21+21) - a*c - b*d", "Cross-term result")
])

# Create layout and plot
plt.figure(figsize=(10, 6))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=10, font_weight="bold", edge_color="gray")
plt.title("Karatsuba Multiplication Divide-and-Conquer Graph", fontsize=14)
plt.show()
