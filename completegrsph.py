import networkx as nx
import matplotlib.pyplot as plt

def create_complete_graph():
    try:
        n = int(input("Enter number of vertices (greater than 3): "))
        
        if n <= 3:
            print("Number of vertices must be greater than 3.")
            return
        
        G = nx.complete_graph(n)
        
       
        pos = nx.circular_layout(G) 
        nx.draw(G, pos, with_labels=True, node_color='skyblue', 
                node_size=1000, font_size=12, font_weight='bold')
        
        plt.title(f"Complete Graph with {n} Vertices")
        plt.show()
        
    except ValueError:
        print("Please enter a valid integer.")

create_complete_graph()
