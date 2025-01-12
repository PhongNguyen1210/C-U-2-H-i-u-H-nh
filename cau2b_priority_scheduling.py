from random import randint

# Lớp Tiến Trình
class TienTrinh:
    def __init__(self, id, thoi_diem_vao, thoi_gian_xu_ly, do_uu_tien):
        self.id = id
        self.thoi_diem_vao = thoi_diem_vao
        self.thoi_gian_xu_ly = thoi_gian_xu_ly
        self.thoi_gian_xu_ly_goc = thoi_gian_xu_ly
        self.do_uu_tien = do_uu_tien
        self.thoi_gian_cho = 0
        self.thoi_gian_hoan_thanh = 0

# Hàm nhập dữ liệu từ terminal
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

# Thuật toán Priority Scheduling không chiếm dụng
def priority_scheduling(tien_trinh_list):
    thoi_gian = 0
    tien_trinh_list.sort(key=lambda x: (x.do_uu_tien, x.thoi_diem_vao))
    for tien_trinh in tien_trinh_list:
        if thoi_gian < tien_trinh.thoi_diem_vao:
            thoi_gian = tien_trinh.thoi_diem_vao
        tien_trinh.thoi_gian_cho = thoi_gian - tien_trinh.thoi_diem_vao
        thoi_gian += tien_trinh.thoi_gian_xu_ly
        tien_trinh.thoi_gian_hoan_thanh = thoi_gian

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

# Chương trình chính
if __name__ == "__main__":
    tien_trinh_list = nhap_du_lieu()

    print("\nPriority Scheduling")
    priority_scheduling(tien_trinh_list)
    in_tien_trinh(tien_trinh_list)
