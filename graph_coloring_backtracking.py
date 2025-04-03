import os

def is_safe(graph, colors, vertex, color):
    for neighbor in graph[vertex]:
        if colors[neighbor] == color:
            return False
    return True

def backtrack_coloring(graph, colors, vertex, K):
    if vertex == len(graph):
        return True
    
    for color in range(1, K + 1):
        if is_safe(graph, colors, vertex, color):
            colors[vertex] = color
            if backtrack_coloring(graph, colors, vertex + 1, K):
                return True
            colors[vertex] = 0
    return False

def graph_coloring(graph, N, K):
    colors = [0] * N
    if backtrack_coloring(graph, colors, 0, K):
        print(f"Coloring Possible with {K} Colors")
        print(f"Color Assignment: {colors}")
    else:
        print(f"Coloring Not Possible with {K} Colors")

def process_input_file(file_name):
    file_path = os.path.join(os.getcwd(), file_name)
    
    try:
        with open(file_path, "r") as file:
            N, M, K = map(int, file.readline().split())
            graph = [[] for _ in range(N)]
            
            for _ in range(M):
                u, v = map(int, file.readline().split())
                graph[u].append(v)
                graph[v].append(u)
            
            graph_coloring(graph, N, K)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

def main():
    input_files = ["input_case1.txt", "input_case2.txt"]
    for file_name in input_files:
        print(f"\nProcessing {file_name}...\n")
        process_input_file(file_name)

if __name__ == "__main__":
    main()
