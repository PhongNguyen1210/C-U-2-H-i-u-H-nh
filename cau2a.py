def la_an_toan(tien_trinh, tai_nguyen_kha_dung, tai_nguyen_toi_da, tai_nguyen_phan_bo):
    so_tien_trinh = len(tien_trinh)  # Số lượng tiến trình
    so_tai_nguyen = len(tai_nguyen_kha_dung)  # Số lượng loại tài nguyên
    hoan_thanh = [False] * so_tien_trinh  # Danh sách để theo dõi các tiến trình đã hoàn thành
    chuoi_an_toan = [0] * so_tien_trinh  # Chuỗi an toàn lưu thứ tự thực hiện các tiến trình
    tai_nguyen_lam_viec = tai_nguyen_kha_dung[:]  # Tài nguyên khả dụng hiện tại
    count = 0  # Khởi tạo biến đếm

    # In trạng thái tài nguyên ban đầu
    print("Trạng thái tài nguyên ban đầu:")
    print("Tài nguyên khả dụng:", tai_nguyen_lam_viec)
    print("Tài nguyên phân bổ:", tai_nguyen_phan_bo)
    print("Tài nguyên tối đa:", tai_nguyen_toi_da)
    print()

    # Kiểm tra từng tiến trình cho đến khi tất cả tiến trình hoàn thành hoặc không thể tìm thấy tiến trình nào có thể hoàn thành
    while count < so_tien_trinh:
        tim_thay = False  # Biến để theo dõi nếu tìm thấy tiến trình có thể hoàn thành
        for i in range(so_tien_trinh): #i: Biến này được dùng trong vòng lặp for để duyệt qua từng tiến trình.
            if not hoan_thanh[i]:  # Kiểm tra nếu tiến trình chưa hoàn thành
                print(f"Đang kiểm tra tiến trình P{i}")
                j = 0 #j: Biến này được dùng trong vòng lặp while để duyệt qua từng loại tài nguyên.
                # Kiểm tra nếu tài nguyên cần thiết của tiến trình <= tài nguyên khả dụng
                while j < so_tai_nguyen and tai_nguyen_toi_da[i][j] - tai_nguyen_phan_bo[i][j] <= tai_nguyen_lam_viec[j]:
                    j += 1
                if j == so_tai_nguyen:  # Nếu tất cả tài nguyên cần thiết đều <= tài nguyên khả dụng
                    # Giải phóng tài nguyên sau khi tiến trình hoàn thành
                    for k in range(so_tai_nguyen):
                        tai_nguyen_lam_viec[k] += tai_nguyen_phan_bo[i][k]
                    chuoi_an_toan[count] = i  # Thêm tiến trình vào chuỗi an toàn
                    count += 1  # Tăng biến đếm
                    hoan_thanh[i] = True  # Đánh dấu tiến trình đã hoàn thành
                    tim_thay = True  # Tìm thấy tiến trình có thể hoàn thành
                    print(f"Tiến trình P{i} có thể hoàn thành và giải phóng tài nguyên.")
                    print("Tài nguyên khả dụng sau khi giải phóng:", tai_nguyen_lam_viec)
                else:
                    print(f"Tiến trình P{i} không thể hoàn thành với tài nguyên hiện tại.")
        if not tim_thay:  # Nếu không tìm thấy tiến trình nào có thể hoàn thành
            print("Hệ thống không ở trạng thái an toàn.")
            return False
    print("Hệ thống ở trạng thái an toàn.\nChuỗi an toàn là: ", end=" ")
    print(chuoi_an_toan)
    return True


def main():
    # Dữ liệu đầu vào
    tien_trinh = [0, 1, 2, 3, 4]
    tai_nguyen_kha_dung = [3, 3, 2]
    tai_nguyen_toi_da = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3]
    ]
    tai_nguyen_phan_bo = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2]
    ]
    # Gọi hàm la_an_toan để kiểm tra trạng thái an toàn
    la_an_toan(tien_trinh, tai_nguyen_kha_dung, tai_nguyen_toi_da, tai_nguyen_phan_bo)


if __name__ == "__main__":
    main()  # Chạy hàm main nếu chương trình được thực thi
