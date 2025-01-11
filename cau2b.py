# CÂU 2b. Xây dựng chương trình minh họa các giải thuật phân phối CPU cho các tiến trình

# Định nghĩa lớp Tiến Trình
class TienTrinh:
    def __init__(self, id, thoi_diem_vao, thoi_gian_xu_ly, do_uu_tien):
        self.id = id  # ID của tiến trình
        self.thoi_diem_vao = thoi_diem_vao  # Thời điểm vào của tiến trình
        self.thoi_gian_xu_ly = thoi_gian_xu_ly  # Thời gian xử lý của tiến trình
        self.thoi_gian_xu_ly_goc = thoi_gian_xu_ly  # Thời gian xử lý gốc của tiến trình
        self.do_uu_tien = do_uu_tien  # Độ ưu tiên của tiến trình
        self.thoi_gian_cho = 0  # Thời gian chờ của tiến trình
        self.thoi_gian_hoan_thanh = 0  # Thời gian hoàn thành của tiến trình

# Thuật toán First-Come, First-Served (FCFS)
def fcfs(tien_trinh_list):
    tien_trinh_list.sort(key=lambda x: x.thoi_diem_vao)  # Sắp xếp danh sách tiến trình theo thời điểm vào
    thoi_gian = 0  # Khởi tạo thời gian ban đầu
    for tien_trinh in tien_trinh_list:
        if thoi_gian < tien_trinh.thoi_diem_vao:
            thoi_gian = tien_trinh.thoi_diem_vao
        tien_trinh.thoi_gian_cho = thoi_gian - tien_trinh.thoi_diem_vao  # Gán thời gian chờ cho tiến trình hiện tại
        tien_trinh.thoi_gian_hoan_thanh = thoi_gian + tien_trinh.thoi_gian_xu_ly  # Tính thời gian hoàn thành
        thoi_gian += tien_trinh.thoi_gian_xu_ly  # Cập nhật thời gian cho tiến trình tiếp theo

# Thuật toán Shortest Job First (SJF)
def sjf(tien_trinh_list):
    tien_trinh_list.sort(key=lambda x: x.thoi_gian_xu_ly)  # Sắp xếp danh sách tiến trình theo thời gian xử lý tăng dần
    thoi_gian = 0  # Khởi tạo thời gian ban đầu
    for tien_trinh in tien_trinh_list:
        if thoi_gian < tien_trinh.thoi_diem_vao:
            thoi_gian = tien_trinh.thoi_diem_vao
        tien_trinh.thoi_gian_cho = thoi_gian - tien_trinh.thoi_diem_vao  # Gán thời gian chờ cho tiến trình hiện tại
        tien_trinh.thoi_gian_hoan_thanh = thoi_gian + tien_trinh.thoi_gian_xu_ly  # Tính thời gian hoàn thành
        thoi_gian += tien_trinh.thoi_gian_xu_ly  # Cập nhật thời gian cho tiến trình tiếp theo

# Thuật toán Round Robin (RR)
def round_robin(tien_trinh_list, quantum):
    thoi_gian = 0  # Khởi tạo thời gian ban đầu
    tien_trinh_list.sort(key=lambda x: x.thoi_diem_vao)  # Sắp xếp danh sách tiến trình theo thời điểm vào
    queue = tien_trinh_list.copy()  # Tạo hàng đợi tiến trình

    while queue:
        for tien_trinh in queue:
            if thoi_gian < tien_trinh.thoi_diem_vao:
                thoi_gian = tien_trinh.thoi_diem_vao
            if tien_trinh.thoi_gian_xu_ly > 0:  # Nếu tiến trình chưa hoàn thành
                if tien_trinh.thoi_gian_xu_ly > quantum:  # Nếu thời gian xử lý của tiến trình lớn hơn quantum
                    thoi_gian += quantum  # Tăng thời gian thực hiện lên bằng quantum
                    tien_trinh.thoi_gian_xu_ly -= quantum  # Giảm thời gian xử lý còn lại của tiến trình
                else:
                    thoi_gian += tien_trinh.thoi_gian_xu_ly  # Tăng thời gian thực hiện lên bằng thời gian xử lý còn lại của tiến trình
                    tien_trinh.thoi_gian_hoan_thanh = thoi_gian  # Cập nhật thời gian hoàn thành
                    tien_trinh.thoi_gian_cho = thoi_gian - tien_trinh.thoi_diem_vao - tien_trinh.thoi_gian_xu_ly_goc  # Tính thời gian chờ
                    tien_trinh.thoi_gian_xu_ly = 0  # Đánh dấu tiến trình đã hoàn thành

        # Loại bỏ các tiến trình đã hoàn thành khỏi hàng đợi
        queue = [tien_trinh for tien_trinh in queue if tien_trinh.thoi_gian_xu_ly > 0]

# Thuật toán Priority Scheduling
def priority_scheduling(tien_trinh_list):
    thoi_gian = 0  # Khởi tạo thời gian ban đầu
    tien_trinh_list.sort(key=lambda x: (x.do_uu_tien, x.thoi_diem_vao))  # Sắp xếp danh sách tiến trình theo độ ưu tiên và thời điểm vào
    for tien_trinh in tien_trinh_list:
        if thoi_gian < tien_trinh.thoi_diem_vao:
            thoi_gian = tien_trinh.thoi_diem_vao
        tien_trinh.thoi_gian_cho = thoi_gian - tien_trinh.thoi_diem_vao  # Gán thời gian chờ cho tiến trình hiện tại
        tien_trinh.thoi_gian_hoan_thanh = thoi_gian + tien_trinh.thoi_gian_xu_ly  # Tính thời gian hoàn thành
        thoi_gian += tien_trinh.thoi_gian_xu_ly  # Cập nhật thời gian cho tiến trình tiếp theo

# Hàm in thông tin các tiến trình
def in_tien_trinh(tien_trinh_list):
    tong_thoi_gian_cho = 0
    print("ID\tThời Điểm Vào\tThời Gian Xử Lý\tThời Gian Chờ\tThời Gian Hoàn Thành\tĐộ Ưu Tiên")
    for tien_trinh in tien_trinh_list:
        print(f"{tien_trinh.id}\t{tien_trinh.thoi_diem_vao}\t\t{tien_trinh.thoi_gian_xu_ly_goc}\t\t{tien_trinh.thoi_gian_cho}\t\t{tien_trinh.thoi_gian_hoan_thanh}\t\t\t{tien_trinh.do_uu_tien}")
        tong_thoi_gian_cho += tien_trinh.thoi_gian_cho
    thoi_gian_cho_trung_binh = tong_thoi_gian_cho / len(tien_trinh_list)
    thoi_gian_cho_str = " + ".join(str(tien_trinh.thoi_gian_cho) for tien_trinh in tien_trinh_list)
    print(f"Thời gian chờ trung bình: ({thoi_gian_cho_str}) / {len(tien_trinh_list)} = {thoi_gian_cho_trung_binh:.2f}")

# Nhập dữ liệu mẫu từ terminal
def nhap_du_lieu():
    so_luong = int(input("Nhập số lượng tiến trình: "))
    tien_trinh_list = []
    for i in range(so_luong):
        id = i + 1
        thoi_diem_vao = int(input(f"Nhập thời điểm vào của tiến trình {id}: "))
        thoi_gian_xu_ly = int(input(f"Nhập thời gian xử lý của tiến trình {id}: "))
        do_uu_tien = int(input(f"Nhập độ ưu tiên của tiến trình {id}: "))
        tien_trinh_list.append(TienTrinh(id, thoi_diem_vao, thoi_gian_xu_ly, do_uu_tien))
    return tien_trinh_list

# Chương trình chính
if __name__ == "__main__":
    tien_trinh_list = nhap_du_lieu()

    print("First-Come, First-Served (FCFS)")
    fcfs(tien_trinh_list)
    in_tien_trinh(tien_trinh_list)

    print("\nShortest Job First (SJF)")
    sjf(tien_trinh_list)
    in_tien_trinh(tien_trinh_list)

    quantum = int(input("\nNhập Quantum cho Round Robin (RR): "))
    print("\nRound Robin (RR) với Quantum =", quantum)
    round_robin(tien_trinh_list, quantum)
    in_tien_trinh(tien_trinh_list)

