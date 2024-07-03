import random

def generate_map(rows, cols, n_paths):
    vertices = []
    edges = []
    end_vertex = (random.randint(0, cols - 1), rows - 1)  # Chosen end vertex
    paths = []
    
    # Ensure unique first steps
    first_steps = set()
    while len(first_steps) < n_paths:
        first_steps.add(random.randint(0, cols - 1))
    first_steps = list(first_steps)

    for first_step in first_steps:
        current_path = [(end_vertex[0], rows - 1)]
        
        # Unique first step for each path
        current_col = first_step
        current_path.append((current_col, rows - 2))  # Second to last row

        # Subsequent steps with modified probabilities to favor turns
        for row in reversed(range(rows - 2)):  # Already included the last two rows
            direction = random.choices([-1, 0, 1], weights=[4, 2, 4], k=1)[0]
            current_col = max(0, min(cols - 1, current_col + direction))
            current_path.append((current_col, row))
        
        paths.append(current_path)

    # Reverse paths to correct orientation and collect all vertices
    for path in paths:
        path.reverse()  # Now the path starts at the top (beginning) and ends at the end vertex
        vertices.extend(path)

    # Find the minimum column index to justify all paths to the left
    min_col = min([col for col, row in vertices])
    
    # Adjust all vertices by subtracting the minimum column index
    justified_vertices = [(col - min_col, row) for (col, row) in vertices]
    justified_paths = []
    for path in paths:
        justified_path = [(col - min_col, row) for (col, row) in path]
        justified_paths.append(justified_path)

    # Define edges for justified paths
    edges = []
    start_vertices = []
    for path in justified_paths:
        start_vertices.append(path[0])
        for i in range(len(path) - 1):
            edges.append((path[i], path[i + 1]))

    # Define end vertex and neighborhoods for justified paths
    end_vertex = (end_vertex[0] - min_col, rows - 1)
    neighborhoods = {vertex: [] for vertex in justified_vertices}
    for source, destination in edges:
        neighborhoods[source].append(destination)

    return vertices, edges, neighborhoods, start_vertices, end_vertex

# Example usage
if __name__ == "__main__":
    vertices, edges, neighborhoods, start_vertices, definitive_end_vertex = generate_map(50, 100, 5)
    print("Vertices:", vertices)
    print("Edges:", edges)
    print("Neighborhoods:", neighborhoods)
    print("Start Vertices:", start_vertices)
    print("End Vertex:", definitive_end_vertex)
