from pyvis.network import Network
import networkx as nx

# Define the hierarchical structure for a simpler visualization
simple_structure = {
    "Main Integration Function": [
        "Initialise Network Application",
        "Setup Main Screen",
        "Configure MDI",
        "Setup Network Infrastructure",
        "Visualize Blockchain TPS",
        "Initialise SARBP",
        "Setup Network Manager",
        "Finalise Integration and Validate"
    ],
    "Initialise Network Application": [
        "Initialise Socket",
        "Configure Socket Parameters",
        "Setup Socket Connections"
    ],
    "Setup Main Screen": [
        "Configure Panels",
        "Add CRUD Buttons",
        "Set Entry Point"
    ],
    "Configure MDI": [
        "Initialise MDI Form",
        "Configure Menu Strip",
        "Create Load Event Handlers"
    ],
    "Setup Network Infrastructure": [
        "Configure Router On A Stick",
        "Configure VLANs",
        "Validate Network Configuration"
    ],
    "Visualize Blockchain TPS": [
        "Prepare TPS Data",
        "Generate Bar Chart",
        "Display Chart"
    ],
    "Initialise SARBP": [
        "Configure Dual Encryption",
        "Setup Smart Contract Access Control",
        "Optimize For AR Devices"
    ],
    "Setup Network Manager": [
        "Initialise Network Manager Class",
        "Configure Client Server Model",
        "Setup Synchronization Callbacks"
    ],
    "Finalise Integration and Validate": [
        "Run System Checks",
        "Perform Security Validations",
        "Ensure Data Integrity"
    ]
}

# Create a NetworkX directed graph
G_simple = nx.DiGraph()

# Add nodes and edges for the simple structure
for parent, children in simple_structure.items():
    for child in children:
        G_simple.add_edge(parent, child)

# Create a pyvis network
net = Network(notebook=True, height="800px", width="100%", directed=True)
net.repulsion(node_distance=250, spring_length=200)

# Add nodes and edges to the pyvis network from the NetworkX graph
net.from_nx(G_simple)

# Custom styles for nodes and edges
for node in net.nodes:
    node['size'] = 20
    node['color'] = {
        'background': 'lightblue',
        'border': 'blue'
    }
    node['font'] = {
        'color': 'black',
        'size': 18,
        'face': 'arial',
        'strokeWidth': 2,
        'strokeColor': '#ffffff'
    }
    node['borderWidth'] = 2

for edge in net.edges:
    edge['color'] = {
        'color': 'gray',
        'highlight': 'blue',
        'hover': 'red'
    }
    edge['arrows'] = {
        'to': {
            'enabled': True,
            'scaleFactor': 1.5
        }
    }

# Set options for better readability and interactivity
net.set_options("""
var options = {
  "nodes": {
    "shape": "dot",
    "size": 20,
    "color": {
      "border": "blue",
      "background": "lightblue"
    },
    "font": {
      "color": "black",
      "size": 18,
      "face": "arial",
      "strokeWidth": 2,
      "strokeColor": "#ffffff"
    },
    "borderWidth": 2
  },
  "edges": {
    "color": {
      "color": "gray",
      "highlight": "blue",
      "hover": "red"
    },
    "arrows": {
      "to": {
        "enabled": true,
        "scaleFactor": 1.5
      }
    }
  },
  "interaction": {
    "hover": true,
    "navigationButtons": true,
    "zoomView": true
  },
  "physics": {
    "forceAtlas2Based": {
      "gravitationalConstant": -50,
      "centralGravity": 0.01,
      "springLength": 200,
      "springConstant": 0.08
    },
    "maxVelocity": 50,
    "solver": "forceAtlas2Based",
    "timestep": 0.35,
    "stabilization": {
      "enabled": true,
      "iterations": 200
    }
  }
}
""")

# Generate and display the network
net.show("holobine_interactive_custom.html")
