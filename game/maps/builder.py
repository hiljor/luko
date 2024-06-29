import pygame
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay, distance_matrix
from scipy.stats.qmc import PoissonDisk
import heapq

# Function to compute Euclidean distance heuristic for A*
def _heuristic(a, b):
    """Computes the Euclidean distance between two points.

    Args:
        a (tuple): First point.
        b (tuple): Second point.

    Returns:
        float: Euclidean distance between the points.
    """
    return np.linalg.norm(np.array(a) - np.array(b))


def _generatePointsOnCircle(radius, num_points):
    """Generates points on a circle using Poisson Disc Sampling.

    Args:
        radius (float): Minimum distance between points.
        num_points (int): Number of points to generate.

    Returns:
        np.ndarray: Array of points.
    """
    engine = PoissonDisk(d=2, radius=radius, seed=None, ncandidates=num_points*40)  # Smaller radius for denser packing
    sample = engine.random(num_points)
    return sample


def _applyDelaunayTriangulation(points):
    """Applies Delaunay triangulation on the given points.

    Args:
        points (np.ndarray): Array of points.

    Raises:
        ValueError: If less than 2 points are provided.

    Returns:
        scipy.spatial.qhull.Delaunay: Delaunay triangulation object.
    """
    if points.shape[0] < 2:  # Delaunay needs at least 2 points
        raise ValueError("At least two points are required for Delaunay triangulation, got {}".format(points.shape[0]))
    tri = Delaunay(points)
    return tri


def _convertToGraph(tri):
    """Converts the Delaunay triangulation to a graph.

    Args:
        tri (scipy.spatial.qhull.Delaunay): Delaunay triangulation object.

    Returns:
        dict: Graph representation of the triangulation.
    """
    points = tri.points
    graph = {i: set() for i in range(len(points))} # Adjacency list representation

    # Add edges between points in each simplex, directed graph (both directions, not a DAG)
    for simplex in tri.simplices:
        for i in simplex:
            for j in simplex:
                if i != j:
                    graph[i].add(j)

    return graph


# A* pathfinding with path exclusion in subsequent iterations
def _findPaths(tri, num_paths, start, end, removal_probability=0.8):
    """Finds multiple paths between two points using A* algorithm, with controlled path sharing.

    Args:
        tri (scipy.spatial.qhull.Delaunay): Delaunay triangulation object.
        num_paths (int): Number of paths to find.
        start (int): Index of the starting point.
        end (int): Index of the ending point.
        removal_probability (float): Probability of removing an edge after use.

    Returns:
        list: List of paths.
        dict: Graph representation of the triangulation.
    """
    graph = _convertToGraph(tri)
    paths = []
    
    def a_star(graph, start, goal):
        open_heap = []
        heapq.heappush(open_heap, (0 + _heuristic(tri.points[start], tri.points[goal]), 0, start, [start]))
        visited = set()

        while open_heap:
            est_cost, cost, curr, path = heapq.heappop(open_heap)
            if curr == goal:
                return path

            if curr not in visited:
                visited.add(curr)
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        g_cost = cost + _heuristic(tri.points[curr], tri.points[neighbor])
                        f_cost = g_cost + _heuristic(tri.points[neighbor], tri.points[goal])
                        heapq.heappush(open_heap, (f_cost, g_cost, neighbor, path + [neighbor]))

        return []

    for _ in range(num_paths):
        result_path = a_star(graph, start, end)
        if result_path:
            paths.append(result_path)
            for i in range(len(result_path) - 1):
                if random.random() < removal_probability:  # Remove with a given probability
                    graph[result_path[i]].discard(result_path[i + 1])
                    graph[result_path[i + 1]].discard(result_path[i])
        else:
            break

    return paths, graph

# (Optional) Function to display the map using matplotlib
def _displayMap(points, paths, start, end):
    """Displays the map with paths using matplotlib.

    Args:
        tri (scipy.spatial.qhull.Delaunay): Delaunay triangulation object.
        paths (list): List of paths.
        start (int): Index of the starting point.
        end (int): Index of the ending point.
    """
    
    plt.figure(figsize=(10, 10))
    plt.plot(points[:, 0], points[:, 1], 'bo')  # Points in blue
    plt.plot(points[start, 0], points[start, 1], 'ro')  # Start point in red
    plt.plot(points[end, 0], points[end, 1], 'go')  # End point in green

    # plot lines as arrows in the direction of the path
    for path in paths:
        for i in range(len(path) - 1):
            plt.arrow(points[path[i], 0], points[path[i], 1], points[path[i+1], 0] - points[path[i], 0], points[path[i+1], 1] - points[path[i], 1], head_width=0.02, head_length=0.02, fc='k', ec='k')
            
    
    plt.show()
    

def _reindexGraphPaths(points, paths, graph, start, end):
    unique_indices = set(idx for path in paths for idx in path)  # Find all unique indices used in paths
    new_index_map = {old_idx: new_idx for new_idx, old_idx in enumerate(unique_indices)}  # Map old indices to new indices
    
    # Create new points array with only used points
    new_points = points[list(unique_indices)]
    
    # Create a new graph with reindexed nodes
    new_graph = {
        new_index_map[old_idx]: set(new_index_map[old_neighbor] 
                                    for old_neighbor in neighbors 
                                    if old_neighbor in new_index_map)
            for old_idx, neighbors in graph.items() if old_idx in new_index_map
    }
    
    # Reindexed paths
    new_paths = [[new_index_map[idx] for idx in path] for path in paths]
    
    # Get new indices for start and end
    new_start = new_index_map[start]
    new_end = new_index_map[end]

    return new_points, new_paths, new_graph, new_start, new_end

def generateMap(num_points=50, num_paths=5):
    radius = num_points / 1000  # Dynamic radius based on the number of points
    points = _generatePointsOnCircle(radius, num_points)
    start_idx = np.argmin(points[:, 1])  # Start at the lowest y-coordinate
    end_idx = np.argmax(points[:, 1])    # End at the highest y-coordinate
    triangulation = _applyDelaunayTriangulation(points)
    paths, graph = _findPaths(triangulation, num_paths, start_idx, end_idx)

    if paths:
        # Reindex graph and paths to include only points in the found paths, also adjust start and end points
        points, paths, graph, new_start, new_end = _reindexGraphPaths(points, paths, graph, start_idx, end_idx)

    return graph, points, paths, new_start, new_end


# Main function to generate and display the map
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode([500, 500])
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        screen.fill((255, 255, 255))
        
        num_points = 50
        radius = 0.05
        
        # generate map
        newGraph, points, paths, start, end = generateMap()
        # find top most point as end and bottom most point as start
        _displayMap(points, paths, start, end)
        
        pygame.display.flip()
    
    pygame.quit()