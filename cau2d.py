def FCFS(yeu_cau, dau_doc):
    chuoi_tim_kiem = []  # Danh sách các vị trí đầu đọc di chuyển đến
    so_lan_tim_kiem = 0  # Số lần tìm kiếm
    for yc in yeu_cau:
        chuoi_tim_kiem.append(yc)  # Thêm yêu cầu vào chuỗi tìm kiếm | yc viết tắt là yêu cầu
        so_lan_tim_kiem += abs(yc - dau_doc)  # Tính khoảng cách di chuyển
        dau_doc = yc  # Cập nhật vị trí đầu đọc
    return so_lan_tim_kiem, chuoi_tim_kiem  # Trả về số lần tìm kiếm và chuỗi tìm kiếm

def SSTF(yeu_cau, dau_doc):
    chuoi_tim_kiem = []  # Danh sách các vị trí đầu đọc di chuyển đến
    so_lan_tim_kiem = 0  # Số lần tìm kiếm
    while yeu_cau:
        # Tìm yêu cầu gần nhất với vị trí hiện tại của đầu đọc
        yc_gan_nhat = min(yeu_cau, key=lambda x: abs(x - dau_doc))
        chuoi_tim_kiem.append(yc_gan_nhat)  # Thêm yêu cầu vào chuỗi tìm kiếm
        so_lan_tim_kiem += abs(yc_gan_nhat - dau_doc)  # Tính khoảng cách di chuyển
        dau_doc = yc_gan_nhat  # Cập nhật vị trí đầu đọc
        yeu_cau.remove(yc_gan_nhat)  # Loại bỏ yêu cầu khỏi danh sách
    return so_lan_tim_kiem, chuoi_tim_kiem  # Trả về số lần tìm kiếm và chuỗi tìm kiếm

def SCAN(yeu_cau, dau_doc, huong, kich_thuoc_dia):
    chuoi_tim_kiem = []  # Danh sách các vị trí đầu đọc di chuyển đến
    so_lan_tim_kiem = 0  # Số lần tìm kiếm
    trai = [0] + [yc for yc in yeu_cau if yc < dau_doc]  # Yêu cầu ở phía trái đầu đọc
    phai = [yc for yc in yeu_cau if yc >= dau_doc] + [kich_thuoc_dia - 1]  # Yêu cầu ở phía phải đầu đọc
    if huong == "trai":
    # Duyệt qua các yêu cầu phía trái đầu đọc, từ lớn đến nhỏ (từ phải sang trái)
        for yc in reversed(trai):  
            chuoi_tim_kiem.append(yc)  # Thêm yêu cầu vào chuỗi tìm kiếm
            so_lan_tim_kiem += abs(yc - dau_doc)  # Tính khoảng cách di chuyển từ vị trí đầu đọc hiện tại đến yêu cầu
            dau_doc = yc  # Cập nhật vị trí đầu đọc hiện tại
        
        # Duyệt qua các yêu cầu phía phải đầu đọc, từ nhỏ đến lớn (từ trái sang phải)
        for yc in phai:  
            chuoi_tim_kiem.append(yc)  # Thêm yêu cầu vào chuỗi tìm kiếm
            so_lan_tim_kiem += abs(yc - dau_doc)  # Tính khoảng cách di chuyển từ vị trí đầu đọc hiện tại đến yêu cầu
            dau_doc = yc  # Cập nhật vị trí đầu đọc hiện tại
    elif huong == "phai":
        for yc in phai:  # Duyệt từ trái sang phải
            chuoi_tim_kiem.append(yc)  # Thêm yêu cầu vào chuỗi tìm kiếm
            so_lan_tim_kiem += abs(yc - dau_doc)  # Tính khoảng cách di chuyển từ vị trí đầu đọc hiện tại đến yêu cầu
            dau_doc = yc  # Cập nhật vị trí đầu đọc hiện tại
        
        for yc in reversed(trai):  # Duyệt từ phải sang trái
            chuoi_tim_kiem.append(yc)  # Thêm yêu cầu vào chuỗi tìm kiếm
            so_lan_tim_kiem += abs(yc - dau_doc)  # Tính khoảng cách di chuyển từ vị trí đầu đọc hiện tại đến yêu cầu
            dau_doc = yc  # Cập nhật vị trí đầu đọc hiện tại
    return so_lan_tim_kiem, chuoi_tim_kiem  # Trả về số lần tìm kiếm và chuỗi tìm kiếm


def CSCAN(yeu_cau, dau_doc, kich_thuoc_dia):
    chuoi_tim_kiem = []  # Danh sách các vị trí đầu đọc di chuyển đến
    so_lan_tim_kiem = 0  # Số lần tìm kiếm
    trai = [yc for yc in yeu_cau if yc < dau_doc]  # Yêu cầu ở phía trái đầu đọc
    phai = [yc for yc in yeu_cau if yc >= dau_doc]  # Yêu cầu ở phía phải đầu đọc
    for yc in phai:  # Duyệt từ trái sang phải
        chuoi_tim_kiem.append(yc)
        so_lan_tim_kiem += abs(yc - dau_doc)
        dau_doc = yc
    if dau_doc != kich_thuoc_dia - 1:  # Nếu đầu đọc không ở vị trí cuối cùng
        so_lan_tim_kiem += abs(kich_thuoc_dia - 1 - dau_doc)  # Di chuyển đến cuối đĩa
        dau_doc = 0  # Cập nhật vị trí đầu đọc về đầu đĩa
        so_lan_tim_kiem += kich_thuoc_dia - 1  # Tính khoảng cách di chuyển
    for yc in trai:  # Duyệt từ đầu đĩa đến vị trí yêu cầu phía trái
        chuoi_tim_kiem.append(yc)
        so_lan_tim_kiem += abs(yc - dau_doc)
        dau_doc = yc
    return so_lan_tim_kiem, chuoi_tim_kiem  # Trả về số lần tìm kiếm và chuỗi tìm kiếm

# Dữ liệu mẫu
yeu_cau = [82, 170, 43, 140, 24, 16, 190]
dau_doc = 50
kich_thuoc_dia = 200
huong = "phai"

fcfs_so_lan_tim_kiem, fcfs_chuoi_tim_kiem = FCFS(yeu_cau, dau_doc)
print("FCFS Số lần tìm kiếm:", fcfs_so_lan_tim_kiem)
print("FCFS Chuỗi tìm kiếm:", fcfs_chuoi_tim_kiem)

sstf_so_lan_tim_kiem, sstf_chuoi_tim_kiem = SSTF(yeu_cau.copy(), dau_doc)
print("SSTF Số lần tìm kiếm:", sstf_so_lan_tim_kiem)
print("SSTF Chuỗi tìm kiếm:", sstf_chuoi_tim_kiem)

scan_so_lan_tim_kiem, scan_chuoi_tim_kiem = SCAN(yeu_cau.copy(), dau_doc, huong, kich_thuoc_dia)
print("SCAN Số lần tìm kiếm:", scan_so_lan_tim_kiem)
print("SCAN Chuỗi tìm kiếm:", scan_chuoi_tim_kiem)

cscan_so_lan_tim_kiem, cscan_chuoi_tim_kiem = CSCAN(yeu_cau.copy(), dau_doc, kich_thuoc_dia)
print("C-SCAN Số lần tìm kiếm:", cscan_so_lan_tim_kiem)
print("C-SCAN Chuỗi tìm kiếm:", cscan_chuoi_tim_kiem)
