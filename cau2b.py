class TienTrinh:
    def __init__(self, id, thoi_gian_chay, do_uu_tien):
        self.id = id
        self.thoi_gian_chay = thoi_gian_chay
        self.do_uu_tien = do_uu_tien
        self.thoi_gian_cho = 0
        self.thoi_gian_hoan_thanh = 0

def fcfs(tien_trinh_list):
    thoi_gian_cho = 0
    for tien_trinh in tien_trinh_list:
        tien_trinh.thoi_gian_cho = thoi_gian_cho
        tien_trinh.thoi_gian_hoan_thanh = tien_trinh.thoi_gian_cho + tien_trinh.thoi_gian_chay
        thoi_gian_cho += tien_trinh.thoi_gian_chay

def sjf(tien_trinh_list):
    tien_trinh_list.sort(key=lambda x: x.thoi_gian_chay)
    fcfs(tien_trinh_list)

def round_robin(tien_trinh_list, quantum):
    thoi_gian = 0
    while True:
        done = True
        for tien_trinh in tien_trinh_list:
            if tien_trinh.thoi_gian_chay > 0:
                done = False
                if tien_trinh.thoi_gian_chay > quantum:
                    thoi_gian += quantum
                    tien_trinh.thoi_gian_chay -= quantum
                else:
                    thoi_gian += tien_trinh.thoi_gian_chay
                    tien_trinh.thoi_gian_cho = thoi_gian - tien_trinh.thoi_gian_chay
                    tien_trinh.thoi_gian_chay = 0
        if done:
            break

def priority_scheduling(tien_trinh_list):
    tien_trinh_list.sort(key=lambda x: x.do_uu_tien)
    thoi_gian_cho = 0
    for tien_trinh in tien_trinh_list:
        tien_trinh.thoi_gian_cho = thoi_gian_cho
        tien_trinh.thoi_gian_hoan_thanh = tien_trinh.thoi_gian_cho + tien_trinh.thoi_gian_chay
        thoi_gian_cho += tien_trinh.thoi_gian_chay

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
