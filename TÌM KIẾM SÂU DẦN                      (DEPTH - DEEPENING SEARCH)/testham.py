def ids(graph, start, end, limit, visited=None):
    if visited is None:
        visited = set()
    if start == end:
        return [start]
    if start not in visited and limit > 0:
        visited.add(start)
        for neighbor in graph[start]:
            path = ids(graph, neighbor, end, limit - 1, visited)
            if path:
                return [start] + path
    return None

def main():
    with open('DDS_INPUT.txt', 'r') as f:
        lines = f.readlines()
        graph = {}
        for line in lines:
            nodes = line.strip().split(':')
            neighbors = nodes[1].split(',')
            graph[nodes[0]] = neighbors
    start = input("Nhập Điểm Đầu  : ").upper()
    end   = input("Nhập Điểm Cuối : ").upper()
    limit = 1
    path  = ids(graph, start, end, limit)
    found_path = False
    while not found_path:
        path = ids(graph, start, end, limit)
        if path:
            found_path = True
            print(f"ĐỘ SÂU: {limit}.")
            print(f"ĐƯỜNG ĐI TỪ {start} ĐẾN {end}: {' -> '.join(path)}\n")
            with open('DDS_OUTPUT.txt', 'w') as f:
                f.write(f"ĐỘ SÂU: {limit}.")
                f.write(f"ĐƯỜNG ĐI TỪ {start} ĐẾN {end}: {' -> '.join(path)}\n")
        limit += 1
    if not found_path:
        print(f"KHÔNG CÓ ĐƯỜNG ĐI TỪ {start} ĐẾN {end} VỚI GIỚI HẠN ĐỘ SÂU LÀ {limit - 1}\n")
        with open('DDS_OUTPUT.txt', 'w') as f:
            f.write(f"KHÔNG CÓ ĐƯỜNG ĐI TỪ {start} ĐẾN {end} \n")

if __name__ == '__main__':
    main()

