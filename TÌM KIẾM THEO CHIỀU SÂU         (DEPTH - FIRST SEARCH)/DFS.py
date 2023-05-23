# Khai báo hàm dfs với 4 tham số: visited (danh sách các nút đã được duyệt),
#                                 graph (từ điển biểu diễn đồ thị),
#                                 node (nút bắt đầu cho việc duyệt đồ thị),
#                                 path (danh sách lưu các đỉnh theo thứ tự duyệt).
def dfs(visited, graph, node, path):
    # Nếu đỉnh chưa được duyệt, thêm vào path, visited.

    if node not in visited:
        path.append(node)
        visited.add(node)
        # Duyệt đỉnh kề đó nếu đỉnh kề chưa được duyệt.
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour, path)

def main():
    # Yêu cầu người dùng nhập đỉnh từ bàn phím.
    node_input = input("Nhập đỉnh: ")
    # Tạo một từ điển để lưu trữ đồ thị.
    graph = {}
    visited = set()
    path = []
    
    # Mở tệp đọc dữ liệu đầu vào.
    with open("DFS_INPUT.txt", "r") as f:
        for line in f:
            nodes = line.strip().split(":")
            neighbours = nodes[1].split(",")
            graph[nodes[0]] = neighbours

    dfs(visited, graph, node_input, path)
    result = " -> ".join(path)
    print(result)
    with open("DFS_OUTPUT.txt", "w") as f:
        f.write(result)
    
if __name__ == "__main__":
    main()