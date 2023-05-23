import heapq
# Khai báo hàm ucs với 3 tham số: start (điểm đầu),
#                                 goal  (điểm cuối),
#                                 loaidothi (1. VÔ HƯỚNG & 2. CÓ HƯỚNG)
def ucs(start, end, loaidothi):
    # Mở tệp đọc dữ liệu đầu vào.
    # Mỗi chuỗi tương ứng 1 dòng.
    with open('UCS_INPUT.txt', 'r') as f:
        data = f.readlines()
    graph = {} # Tạo từ điển để lưu trữ đồ thị.
    
    for line in data:
        # Tách điểm đầu, điểm cuối, chi phí.
        node1, node2, cost = line.strip().split() 
        cost = int(cost) # Chuyển chi phí thành kiểu số nguyên.
        # Kiểm tra xem đỉnh 'node1' đã được thêm vào đồ thị chưa. Nếu chưa, thêm 'node1' vào đồ thị. 
        if node1 not in graph:
            graph[node1] = {}
        # Kiểm tra xem đỉnh 'node2' đã được thêm vào đồ thị chưa. Nếu chưa, thêm 'node2' vào đồ thị. 
        if node2 not in graph:    graph[node2] = {}

        # Nếu đồ thị là CÓ HƯỚNG 
        if loaidothi == '2':     graph[node1][node2] = cost
            
        # Nếu đồ thị là VÔ HƯỚNG
        elif loaidothi == '1':
            graph[node2][node1] = cost
            graph[node1][node2] = cost
        
    visited = set() # Tạo một tập hợp lưu trữ các đỉnh đã được duyệt.
    queue = [(0, start, [])] # Khởi tạo hàng đợi ưu tiên.

    while queue:
        # Lấy ra bộ giá trị (chi phí, đỉnh hiện tại, đường đi) từ hàng đợi và xử lý.
        (cost, current, path) = heapq.heappop(queue)
        # Nếu đỉnh hiện tại chưa được duyệt, đánh dấu là đã duyệt và cập nhật đường đi.
        if current not in visited:
            visited.add(current)
            path = path + [current]

            # Kiểm tra xem đỉnh hiện tại có phải là đích không,
            # nếu đúng thì ghi lại đường đi và chi phí vào file OUTPUT.
            if current == end:
                with open('UCS_OUTPUT.txt', 'w') as file:
                    file.write(f"ĐƯỜNG ĐI: {' -> '.join(path)}\n")
                    file.write(f"CHI PHÍ : {cost}\n")
                return path, cost

            # Lặp qua tất cả các đỉnh kề của đỉnh hiện tại và chi phí tương ứng của chúng.
            for neighbor, neighborcost in graph[current].items():
                # Nếu đỉnh kề chưa được duyệt thì thêm nó vào hàng đợi,
                # với chi phí tính từ đỉnh hiện tại đến đỉnh kề.
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + neighborcost, neighbor, path))

    with open('UCS_OUTPUT.txt', 'w') as file:
        file.write("KHÔNG TÌM THẤY ĐƯỜNG ĐI !\n")
    return None, None

def main():
    print("TÌM KIẾM VỚI CHI PHÍ CỰC TIỂU")
    print("UNIFORM COST SEARCH")
    diemdau   = input("NHẬP ĐIỂM ĐẦU : ").upper()
    diemcuoi  = input("NHẬP ĐIỂM CUỐI: ").upper()
    print("\nCHỌN LOẠI ĐỒ THỊ: ")
    print("1. VÔ HƯỚNG.")
    print("2. CÓ HƯỚNG.")
    loaidothi = input("Chọn: ")
    path, cost = ucs(diemdau, diemcuoi, loaidothi)
    if path:
        print(f"ĐƯỜNG ĐI: {' -> '.join(path)}")
        print(f"CHI PHÍ : {cost}")
    else:
        print("KHÔNG TÌM THẤY ĐƯỜNG ĐI !")

if __name__ == "__main__":
    main()