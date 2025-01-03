def FIFO(trang, dung_luong):
    bo_nho = []
    loi_trang = 0
    for t in trang:
        if t not in bo_nho:
            if len(bo_nho) < dung_luong:
                bo_nho.append(t)
            else:
                bo_nho.pop(0)
                bo_nho.append(t)
            loi_trang += 1
    return loi_trang

def LRU(trang, dung_luong):
    bo_nho = []
    loi_trang = 0
    su_dung_gan_day = []
    for t in trang:
        if t not in bo_nho:
            if len(bo_nho) < dung_luong:
                bo_nho.append(t)
            else:
                trang_lru = su_dung_gan_day.pop(0)
                bo_nho.remove(trang_lru)
                bo_nho.append(t)
            loi_trang += 1
        else:
            su_dung_gan_day.remove(t)
        su_dung_gan_day.append(t)
    return loi_trang

def Optimal(trang, dung_luong):
    bo_nho = []
    loi_trang = 0
    for i in range(len(trang)):
        if trang[i] not in bo_nho:
            if len(bo_nho) < dung_luong:
                bo_nho.append(trang[i])
            else:
                su_dung_tuong_lai = []
                for t in bo_nho:
                    if t in trang[i+1:]:
                        su_dung_tuong_lai.append(trang[i+1:].index(t))
                    else:
                        su_dung_tuong_lai.append(float('inf'))
                bo_nho.pop(su_dung_tuong_lai.index(max(su_dung_tuong_lai)))
                bo_nho.append(trang[i])
            loi_trang += 1
    return loi_trang

# Dữ liệu mẫu
trang = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
dung_luong = 3

print(f"Số lần lỗi trang FIFO: {FIFO(trang, dung_luong)}")
print(f"Số lần lỗi trang LRU: {LRU(trang, dung_luong)}")
print(f"Số lần lỗi trang Optimal: {Optimal(trang, dung_luong)}")
