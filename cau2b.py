# Định nghĩa lớp Tiến Trình
class TienTrinh:
    def __init__(self, id, thoi_gian_chay, do_uu_tien):
        self.id = id  # ID của tiến trình
        self.thoi_gian_chay = thoi_gian_chay  # Thời gian chạy của tiến trình
        self.do_uu_tien = do_uu_tien  # Độ ưu tiên của tiến trình
        self.thoi_gian_cho = 0  # Thời gian chờ của tiến trình
        self.thoi_gian_hoan_thanh = 0  # Thời gian hoàn thành của tiến trình

# Thuật toán First-Come, First-Served (FCFS) Thực hiện theo thứ tự tiến trình đến trước, xử lý trước. Tính toán thời gian chờ và thời gian hoàn thành của mỗi tiến trình.
def fcfs(tien_trinh_list):
    thoi_gian_cho = 0  # Khởi tạo thời gian chờ ban đầu
    for tien_trinh in tien_trinh_list:
        tien_trinh.thoi_gian_cho = thoi_gian_cho  # Gán thời gian chờ cho tiến trình hiện tại
        tien_trinh.thoi_gian_hoan_thanh = tien_trinh.thoi_gian_cho + tien_trinh.thoi_gian_chay  # Tính thời gian hoàn thành
        thoi_gian_cho += tien_trinh.thoi_gian_chay  # Cập nhật thời gian chờ cho tiến trình tiếp theo

# Thuật toán Shortest Job First (SJF) Sắp xếp các tiến trình theo thời gian chạy ngắn nhất trước, sau đó áp dụng thuật toán FCFS.
def sjf(tien_trinh_list):
    # Sắp xếp danh sách tiến trình theo thời gian chạy tăng dần
    tien_trinh_list.sort(key=lambda x: x.thoi_gian_chay) # lambda x: x.thoi_gian_chay là một hàm ẩn danh, trong đó x là đối tượng trong tien_trinh_list. Hàm này trả về giá trị của thuộc tính thoi_gian_chay của đối tượng x.
    fcfs(tien_trinh_list)  # Áp dụng thuật toán FCFS sau khi sắp xếp

# Thuật toán Round Robin (RR) Xử lý tiến trình theo vòng tròn, mỗi tiến trình được cấp phát một đơn vị thời gian (quantum).
#  Nếu thời gian chạy của tiến trình lớn hơn quantum, tiến trình sẽ được xử lý tiếp trong vòng tiếp theo.
def round_robin(tien_trinh_list, quantum):
    thoi_gian = 0  # Khởi tạo thời gian ban đầu
    while True:
        done = True  # Biến để kiểm tra nếu tất cả tiến trình đã hoàn thành
        for tien_trinh in tien_trinh_list:
            if tien_trinh.thoi_gian_chay > 0:  # Nếu tiến trình chưa hoàn thành
                done = False  # Còn tiến trình cần thực hiện
                if tien_trinh.thoi_gian_chay > quantum:  # Nếu thời gian chạy của tiến trình lớn hơn quantum
                    thoi_gian += quantum  # Tăng thời gian thực hiện lên bằng quantum
                    tien_trinh.thoi_gian_chay -= quantum  # Giảm thời gian chạy còn lại của tiến trình
                else:
                    thoi_gian += tien_trinh.thoi_gian_chay  # Tăng thời gian thực hiện lên bằng thời gian chạy còn lại của tiến trình
                    tien_trinh.thoi_gian_cho = thoi_gian - tien_trinh.thoi_gian_chay  # Tính thời gian chờ
                    tien_trinh.thoi_gian_chay = 0  # Đánh dấu tiến trình đã hoàn thành
        if done:
            break  # Thoát khỏi vòng lặp nếu tất cả tiến trình đã hoàn thành

# Thuật toán Priority Scheduling Sắp xếp các tiến trình theo độ ưu tiên. Tiến trình có độ ưu tiên cao sẽ được xử lý trước.
def priority_scheduling(tien_trinh_list):
    # Sắp xếp danh sách tiến trình theo độ ưu tiên tăng dần
    tien_trinh_list.sort(key=lambda x: x.do_uu_tien) # lambda x: x.do_uu_tien là một hàm ẩn danh, trong đó x là đối tượng trong tien_trinh_list. Hàm này trả về giá trị của thuộc tính do_uu_tien của đối tượng x.
    thoi_gian_cho = 0  # Khởi tạo thời gian chờ ban đầu
    for tien_trinh in tien_trinh_list:
        tien_trinh.thoi_gian_cho = thoi_gian_cho  # Gán thời gian chờ cho tiến trình hiện tại
        tien_trinh.thoi_gian_hoan_thanh = tien_trinh.thoi_gian_cho + tien_trinh.thoi_gian_chay  # Tính thời gian hoàn thành
        thoi_gian_cho += tien_trinh.thoi_gian_chay  # Cập nhật thời gian chờ cho tiến trình tiếp theo

# Hàm in thông tin các tiến trình
def in_tien_trinh(tien_trinh_list):
    print("ID\tThời Gian Chạy\tThời Gian Chờ\tThời Gian Hoàn Thành\tĐộ Ưu Tiên")
    for tien_trinh in tien_trinh_list:
        print(f"{tien_trinh.id}\t{tien_trinh.thoi_gian_chay}\t\t{tien_trinh.thoi_gian_cho}\t\t{tien_trinh.thoi_gian_hoan_thanh}\t\t\t{tien_trinh.do_uu_tien}")

# Dữ liệu mẫu
tien_trinh_list = [
    TienTrinh(1, 24, 2),
    TienTrinh(2, 3, 1),
    TienTrinh(3, 3, 3),
    TienTrinh(3, 3, 2)
]

print("First-Come, First-Served (FCFS)")
fcfs(tien_trinh_list)
in_tien_trinh(tien_trinh_list)

print("\nShortest Job First (SJF)")
sjf(tien_trinh_list)
in_tien_trinh(tien_trinh_list)

quantum = 4
print("\nRound Robin (RR) với Quantum =", quantum)
round_robin(tien_trinh_list, quantum)
in_tien_trinh(tien_trinh_list)

print("\nPriority Scheduling")
priority_scheduling(tien_trinh_list)
in_tien_trinh(tien_trinh_list)
