def la_an_toan(tien_trinh, tai_nguyen_kha_dung, tai_nguyen_toi_da, tai_nguyen_phan_bo):
    so_tien_trinh = len(tien_trinh)
    so_tai_nguyen = len(tai_nguyen_kha_dung)
    hoan_thanh = [False] * so_tien_trinh
    chuoi_an_toan = [0] * so_tien_trinh
    tai_nguyen_lam_viec = tai_nguyen_kha_dung[:]
    count = 0  # Khởi tạo biến count

    print("Trạng thái tài nguyên ban đầu:")
    print("Tài nguyên khả dụng:", tai_nguyen_lam_viec)
    print("Tài nguyên phân bổ:", tai_nguyen_phan_bo)
    print("Tài nguyên tối đa:", tai_nguyen_toi_da)
    print()

    while count < so_tien_trinh:
        tim_thay = False
        for i in range(so_tien_trinh):
            if not hoan_thanh[i]:
                print(f"Đang kiểm tra tiến trình P{i}")
                j = 0
                while j < so_tai_nguyen and tai_nguyen_toi_da[i][j] - tai_nguyen_phan_bo[i][j] <= tai_nguyen_lam_viec[j]:
                    j += 1
                if j == so_tai_nguyen:
                    for k in range(so_tai_nguyen):
                        tai_nguyen_lam_viec[k] += tai_nguyen_phan_bo[i][k]
                    chuoi_an_toan[count] = i
                    count += 1
                    hoan_thanh[i] = True
                    tim_thay = True
                    print(f"Tiến trình P{i} có thể hoàn thành và giải phóng tài nguyên.")
                    print("Tài nguyên khả dụng sau khi giải phóng:", tai_nguyen_lam_viec)
                else:
                    print(f"Tiến trình P{i} không thể hoàn thành với tài nguyên hiện tại.")
        if not tim_thay:
            print("Hệ thống không ở trạng thái an toàn.")
            return False
    print("Hệ thống ở trạng thái an toàn.\nChuỗi an toàn là: ", end=" ")
    print(chuoi_an_toan)
    return True


def main():
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
    la_an_toan(tien_trinh, tai_nguyen_kha_dung, tai_nguyen_toi_da, tai_nguyen_phan_bo)


if __name__ == "__main__":
    main()
