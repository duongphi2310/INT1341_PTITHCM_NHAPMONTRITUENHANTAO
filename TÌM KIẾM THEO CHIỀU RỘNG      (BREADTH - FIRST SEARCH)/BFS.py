# Khai báo hàm bfs với 4 tham số: visited (danh sách các nút đã được duyệt),
#                                 graph (từ điển biểu diễn đồ thị),
#                                 node (nút bắt đầu cho việc duyệt đồ thị),
#                                 queue (hàng đợi để lưu các nút chưa được duyệt).
def bfs(visited, graph, node, queue):
    visited.append(node)    # Thêm node vào visited.
    queue.append(node)      # thêm node vào queue.
    result = []

    # Duyệt đồ thị theo BFS.
    while queue:
        s = queue.pop(0)    # Lấy ra nút đầu tiên từ queue.
        result.append(s)    # Thêm vào result.

        # Duyệt qua các nút kề của nút hiện tại đang xét
        for neighbour in graph[s]:
            # Kiểm tra xem nút này đã được duyệt chưa.
            # Nếu chưa được duyệt, thêm nó vào danh sách visited và hàng đợi queue để duyệt nó.
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    
    # Mở tệp để ghi kết quả.            
    with open('BFS_OUTPUT.txt', 'w') as f:
        print("ĐƯỜNG ĐI: ", end = '')
        for i, node in enumerate(result):
            print(node, end = "", file = f)
            if i != len(result) - 1:
                print(" -> ", end = "", file = f)
    # Mở tệp để đọc kết quả.
    # Hiện kết quả ra màn hình.
    with open('BFS_OUTPUT.txt', 'r') as f:
        content = f.read()
        print(content)

def main():
    print("TÌM KIẾM VỚI CHI PHÍ CỰC TIỂU")
    print("UNIFORM COST SEARCH")
    node_input = input("Nhập đỉnh: ")
    with open('BFS_INPUT2.txt', 'r') as f:
        lines = f.readlines()

    graph = {}

    for line in lines:
        parts = line.strip().split(':')
        node = parts[0]
        neighbours = parts[1].split(',')
        graph[node] = neighbours

    visited = []
    queue = []
    bfs(visited, graph, node_input, queue)

if __name__ == '__main__':
    main()

