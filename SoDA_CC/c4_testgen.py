import random
import string
import os
from typing import Dict, List, Set

def generate_connected_graph(num_planets: int, edge_density: float = 0.3) -> Dict[str, List[str]]:
    """Generate a connected undirected graph with given number of planets"""
    # Create planet names
    planets = [str(i) for i in range(num_planets)]
    
    # Start with a minimum spanning tree to ensure connectivity
    graph = {p: [] for p in planets}
    used_planets = {planets[0]}
    remaining_planets = set(planets[1:])
    
    # Connect all planets
    while remaining_planets:
        planet = random.choice(list(remaining_planets))
        connect_to = random.choice(list(used_planets))
        graph[planet].append(connect_to)
        graph[connect_to].append(planet)
        used_planets.add(planet)
        remaining_planets.remove(planet)
    
    # Add additional random edges based on density
    max_additional_edges = int(num_planets * (num_planets - 1) * edge_density / 2)
    for _ in range(max_additional_edges):
        p1 = random.choice(planets)
        p2 = random.choice([p for p in planets if p != p1 and p not in graph[p1]])
        if p2:
            graph[p1].append(p2)
            graph[p2].append(p1)
    
    return graph

def generate_water_types(planets: List[str], min_fresh: int = 2, min_salt: int = 1) -> Dict[str, str]:
    """Generate water types ensuring minimum fresh and salt water planets"""
    water_types = {}
    
    # Ensure minimum fresh water planets
    fresh_planets = random.sample(planets, min_fresh)
    for planet in fresh_planets:
        water_types[planet] = 'F'
    
    # Ensure minimum salt water planets
    remaining = [p for p in planets if p not in water_types]
    salt_planets = random.sample(remaining, min_salt)
    for planet in salt_planets:
        water_types[planet] = 'S'
    
    # Randomly assign remaining planets
    remaining = [p for p in planets if p not in water_types]
    for planet in remaining:
        water_types[planet] = random.choice(['F', 'S', 'N'])
    
    return water_types

def generate_test_case(num_planets: int, edge_density: float = 0.3) -> tuple:
    """Generate a single test case"""
    # Generate graph
    graph = generate_connected_graph(num_planets, edge_density)
    
    # Generate water types
    water_types = generate_water_types(list(graph.keys()))
    
    # Choose start and end planets
    planets = list(graph.keys())
    start = random.choice(planets)
    end = random.choice([p for p in planets if p != start])
    
    # Choose n (number of fresh water planets needed)
    n = random.randint(1, min(num_planets, 3))
    
    return graph, water_types, start, end, n

def write_test_case(f, graph: Dict[str, List[str]], water_types: Dict[str, str], 
                   start: str, end: str, n: int):
    """Write a single test case to file"""
    # Write number of vertices and edges
    num_edges = sum(len(neighbors) for neighbors in graph.values()) // 2
    f.write(f"{len(graph)} {num_edges}\n")
    
    # Write edges (each edge only once)
    written_edges = set()
    for planet, neighbors in graph.items():
        for neighbor in neighbors:
            edge = tuple(sorted([planet, neighbor]))
            if edge not in written_edges:
                f.write(f"{edge[0]} {edge[1]}\n")
                written_edges.add(edge)
    
    # Write water types
    for planet, wtype in water_types.items():
        f.write(f"{planet} {wtype}\n")
    
    # Write start, end and n
    f.write(f"{start}\n")
    f.write(f"{end}\n")
    f.write(f"{n}\n")

def generate_test_cases():
    """Generate multiple test cases"""
    test_cases = []
    
    # Add example test cases from problem description
    example1 = (
        {"Earth": ["Mars", "Venus"], "Mars": ["Earth", "Jupiter"], 
         "Venus": ["Earth", "Jupiter"], "Jupiter": ["Mars", "Venus"]},
        {"Earth": "F", "Mars": "F", "Venus": "S", "Jupiter": "F"},
        "Earth", "Jupiter", 1
    )
    example2 = (
        {"Earth": ["Mars"], "Mars": ["Earth", "Venus"], "Venus": ["Mars"]},
        {"Earth": "N", "Mars": "N", "Venus": "N"},
        "Earth", "Venus", 1
    )
    test_cases.extend([example1, example2])
    
    # Generate random test cases of various sizes
    sizes = [5, 10, 20, 50, 100, 200, 500, 1000]
    for size in sizes:
        test_cases.append(generate_test_case(size))
    
    # Add edge cases
    min_case = generate_test_case(2, 1.0)  # Minimum possible size
    dense_case = generate_test_case(20, 0.8)  # Dense graph
    sparse_case = generate_test_case(20, 0.1)  # Sparse graph
    test_cases.extend([min_case, dense_case, sparse_case])
    
    return test_cases

def write_test_cases(test_cases, output_dir="tests"):
    """Write all test cases to files"""
    os.makedirs(output_dir, exist_ok=True)
    
    for i, (graph, water_types, start, end, n) in enumerate(test_cases, 1):
        with open(os.path.join(output_dir, f"input{i:02d}.txt"), "w") as f:
            write_test_case(f, graph, water_types, start, end, n)

if __name__ == "__main__":
    test_cases = generate_test_cases()
    write_test_cases(test_cases) 