# Khai báo hàm dds với 5 tham số: graph   (từ điển biểu diễn đồ thị),
#                                 start   (điểm đầu),
#                                 end     (điểm cuối),
#                                 limit   (giới hạn độ sâu tìm kiếm),
#                                 visited (danh sách các nút đã được duyệt).
def dds(graph, start, end, limit, visited=None):
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
            path = dds(graph, neighbor, end, limit - 1, visited)
            # Tìm thấy đường đi từ đỉnh kề đến đỉnh cuối,
            # trả về đường đi từ điểm đầu đến điểm kề, đến khi kết thúc.
            if path:
                return [start] + path
    return None

def main():
    # Mở tệp đọc dữ liệu đầu vào.
    # Mỗi chuỗi tương ứng 1 dòng.
    with open('DDS_INPUT.txt', 'r') as f:
        lines = f.readlines()
        graph = {}
        # Tách điểm và điểm kể.
        for line in lines:
            nodes = line.strip().split(':')
            neighbors = nodes[1].split(',')
            graph[nodes[0]] = neighbors
    start = input("Nhập Điểm Đầu  : ").upper()
    end   = input("Nhập Điểm Cuối : ").upper()
    limit = 1
    path  = dds(graph, start, end, limit)
    found_path = False
    while not found_path:
        path = dds(graph, start, end, limit)
        if path:  # Nếu tìm thấy đường đi, cập nhật biến và in ra kết quả.
            found_path = True
            print(f"ĐỘ SÂU: {limit}.")
            print(f"ĐƯỜNG ĐI TỪ {start} ĐẾN {end}: {' -> '.join(path)}\n")
            with open('DDS_OUTPUT.txt', 'w') as f:
                f.write(f"ĐỘ SÂU: {limit}.")
                f.write(f"ĐƯỜNG ĐI TỪ {start} ĐẾN {end}: {' -> '.join(path)}\n")
        limit += 1
    if not found_path:  # Nếu không tìm thấy đường đi, in ra thông báo.
        print(f"KHÔNG CÓ ĐƯỜNG ĐI TỪ {start} ĐẾN {end} VỚI GIỚI HẠN ĐỘ SÂU LÀ {limit-1}\n")
        with open('DDS_OUTPUT.txt', 'w') as f:
            f.write(f"KHÔNG CÓ ĐƯỜNG ĐI TỪ {start} ĐẾN {end} \n")

if __name__ == '__main__':
    main()