# Khai báo hàm dls với 5 tham số: graph   (từ điển biểu diễn đồ thị),
#                                 start   (điểm đầu),
#                                 end     (điểm cuối),
#                                 limit   (giới hạn độ sâu tìm kiếm),
#                                 visited (danh sách các nút đã được duyệt).
def dls(graph, start, end, limit, visited=None):
    # Kiểm tra xem 'visited' có phải là một tập hợp rỗng không.
    # Nếu không, tạo ra một tập hợp rỗng.
    if visited is None:
        visited = set()
    # Nếu điểm đầu trùng với điểm cuối, trả về một phần tử duy nhất.
    if start == end:
        return [start]
    # Kiểm tra xem điểm đầu đã được thăm trước đó hay chưa
    # và giới hạn độ sâu tìm kiếm còn lớn hơn 0 hay không
    if start not in visited and limit > 0:
        # Nếu không, thêm điểm đầu vào tập hợp.
        visited.add(start)
         # Duyệt đỉnh kề đó nếu đỉnh kề chưa được duyệt.
        for neighbor in graph[start]:
            # Gọi đệ quy, 'limit' giảm đi 1, cập nhật các nút đã được duyệt.
            path = dls(graph, neighbor, end, limit - 1, visited)
            # Tìm thấy đường đi từ đỉnh kề đến đỉnh cuối,
            # trả về đường đi từ điểm đầu đến điểm kề, đến khi kết thúc.
            if path:
                return [start] + path
    return []

def main():
    # Mở tệp đọc dữ liệu đầu vào.
    # Mỗi chuỗi tương ứng 1 dòng.
    with open('DLS_INPUT.txt', 'r') as f:
        lines = f.readlines()
        graph = {}
        # Tách điểm và điểm kể.
        for line in lines:
            nodes = line.strip().split(':')
            neighbors = nodes[1].split(',')
            graph[nodes[0]] = neighbors
    start = input("Nhập Điểm Đầu  : ").upper()
    end   = input("Nhập Điểm Cuối : ").upper()
    limit = int(input("Nhập Độ Sâu    : "))
    path  = dls(graph, start, end, limit)
    
    with open('DLS_OUTPUT.txt', 'w') as f:
        if path:
            f.write(f"ĐỘ SÂU: {limit}.")
            f.write(f"ĐƯỜNG ĐI TỪ {start} ĐẾN {end}: {' -> '.join(path)}\n")
        else:
            f.write(f"KHÔNG CÓ ĐƯỜNG ĐI TỪ {start} ĐẾN {end} VỚI ĐỘ SÂU {limit}\n")
    
    if path:
        print(f"ĐỘ SÂU: {limit}.")
        print(f"ĐƯỜNG ĐI TỪ {start} ĐẾN {end}: {' -> '.join(path)}\n")
    else:
        print(f"KHÔNG CÓ ĐƯỜNG ĐI TỪ {start} ĐẾN {end} VỚI ĐỘ SÂU {limit}\n")


if __name__ == "__main__":
    main()
