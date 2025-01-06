def FIFO(trang, dung_luong):
    bo_nho = []  # Danh sách lưu trữ các trang trong bộ nhớ
    loi_trang = 0  # Đếm số lần lỗi trang
    for t in trang:  # Duyệt qua từng trang trong danh sách trang
        if t not in bo_nho:  # Nếu trang không có trong bộ nhớ
            if len(bo_nho) < dung_luong:  # Nếu bộ nhớ chưa đầy
                bo_nho.append(t)  # Thêm trang vào bộ nhớ
            else:  # Nếu bộ nhớ đã đầy
                bo_nho.pop(0)  # Loại bỏ trang đầu tiên trong bộ nhớ (theo quy tắc FIFO)
                bo_nho.append(t)  # Thêm trang mới vào bộ nhớ
            loi_trang += 1  # Tăng số lần lỗi trang
    return loi_trang  # Trả về số lần lỗi trang

def LRU(trang, dung_luong):
    bo_nho = []  # Danh sách lưu trữ các trang trong bộ nhớ
    loi_trang = 0  # Đếm số lần lỗi trang
    su_dung_gan_day = []  # Danh sách theo dõi các trang được sử dụng gần đây
    for t in trang:  # Duyệt qua từng trang trong danh sách trang
        if t not in bo_nho:  # Nếu trang không có trong bộ nhớ
            if len(bo_nho) < dung_luong:  # Nếu bộ nhớ chưa đầy
                bo_nho.append(t)  # Thêm trang vào bộ nhớ
            else:  # Nếu bộ nhớ đã đầy
                trang_lru = su_dung_gan_day.pop(0)  # Xác định trang ít được sử dụng gần đây nhất
                bo_nho.remove(trang_lru)  # Loại bỏ trang ít được sử dụng gần đây nhất khỏi bộ nhớ
                bo_nho.append(t)  # Thêm trang mới vào bộ nhớ
            loi_trang += 1  # Tăng số lần lỗi trang
        else:
            su_dung_gan_day.remove(t)  # Nếu trang đã có trong bộ nhớ, cập nhật danh sách sử dụng gần đây
        su_dung_gan_day.append(t)  # Thêm trang vào danh sách sử dụng gần đây
    return loi_trang  # Trả về số lần lỗi trang

def Optimal(trang, dung_luong):
    bo_nho = []  # Danh sách lưu trữ các trang trong bộ nhớ
    loi_trang = 0  # Đếm số lần lỗi trang
    for i in range(len(trang)):  # Duyệt qua từng trang trong danh sách trang
        if trang[i] not in bo_nho:  # Nếu trang không có trong bộ nhớ
            if len(bo_nho) < dung_luong:  # Nếu bộ nhớ chưa đầy
                bo_nho.append(trang[i])  # Thêm trang vào bộ nhớ
            else:  # Nếu bộ nhớ đã đầy
                su_dung_tuong_lai = []  # Danh sách theo dõi việc sử dụng trang trong tương lai
                for t in bo_nho:  # Duyệt qua các trang trong bộ nhớ
                    if t in trang[i+1:]:  # Nếu trang sẽ được sử dụng lại trong tương lai
                        su_dung_tuong_lai.append(trang[i+1:].index(t))  # Thêm vị trí sử dụng tương lai vào danh sách
                    else:
                        su_dung_tuong_lai.append(float('inf'))  # Nếu trang không được sử dụng lại, đánh dấu là vô tận
                bo_nho.pop(su_dung_tuong_lai.index(max(su_dung_tuong_lai)))  # Loại bỏ trang sẽ không được sử dụng lâu nhất
                bo_nho.append(trang[i])  # Thêm trang mới vào bộ nhớ
            loi_trang += 1  # Tăng số lần lỗi trang
    return loi_trang  # Trả về số lần lỗi trang

# Dữ liệu mẫu
trang = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
dung_luong = 3

print(f"Số lần lỗi trang FIFO: {FIFO(trang, dung_luong)}")
print(f"Số lần lỗi trang LRU: {LRU(trang, dung_luong)}")
print(f"Số lần lỗi trang Optimal: {Optimal(trang, dung_luong)}")
