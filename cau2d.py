def FCFS(yeu_cau, dau_doc):
    chuoi_tim_kiem = []
    so_lan_tim_kiem = 0
    for yc in yeu_cau:
        chuoi_tim_kiem.append(yc)
        so_lan_tim_kiem += abs(yc - dau_doc)
        dau_doc = yc
    return so_lan_tim_kiem, chuoi_tim_kiem

def SSTF(yeu_cau, dau_doc):
    chuoi_tim_kiem = []
    so_lan_tim_kiem = 0
    while yeu_cau:
        yc_gan_nhat = min(yeu_cau, key=lambda x: abs(x - dau_doc))
        chuoi_tim_kiem.append(yc_gan_nhat)
        so_lan_tim_kiem += abs(yc_gan_nhat - dau_doc)
        dau_doc = yc_gan_nhat
        yeu_cau.remove(yc_gan_nhat)
    return so_lan_tim_kiem, chuoi_tim_kiem

def SCAN(yeu_cau, dau_doc, huong, kich_thuoc_dia):
    chuoi_tim_kiem = []
    so_lan_tim_kiem = 0
    trai = [0] + [yc for yc in yeu_cau if yc < dau_doc]
    phai = [yc for yc in yeu_cau if yc >= dau_doc] + [kich_thuoc_dia - 1]
    if huong == "trai":
        for yc in reversed(trai):
            chuoi_tim_kiem.append(yc)
            so_lan_tim_kiem += abs(yc - dau_doc)
            dau_doc = yc
        for yc in phai:
            chuoi_tim_kiem.append(yc)
            so_lan_tim_kiem += abs(yc - dau_doc)
            dau_doc = yc
    elif huong == "phai":
        for yc in phai:
            chuoi_tim_kiem.append(yc)
            so_lan_tim_kiem += abs(yc - dau_doc)
            dau_doc = yc
        for yc in reversed(trai):
            chuoi_tim_kiem.append(yc)
            so_lan_tim_kiem += abs(yc - dau_doc)
            dau_doc = yc
    return so_lan_tim_kiem, chuoi_tim_kiem

def CSCAN(yeu_cau, dau_doc, kich_thuoc_dia):
    chuoi_tim_kiem = []
    so_lan_tim_kiem = 0
    trai = [yc for yc in yeu_cau if yc < dau_doc]
    phai = [yc for yc in yeu_cau if yc >= dau_doc]
    for yc in phai:
        chuoi_tim_kiem.append(yc)
        so_lan_tim_kiem += abs(yc - dau_doc)
        dau_doc = yc
    if dau_doc != kich_thuoc_dia - 1:
        so_lan_tim_kiem += abs(kich_thuoc_dia - 1 - dau_doc)
        dau_doc = 0
        so_lan_tim_kiem += kich_thuoc_dia - 1
    for yc in trai:
        chuoi_tim_kiem.append(yc)
        so_lan_tim_kiem += abs(yc - dau_doc)
        dau_doc = yc
    return so_lan_tim_kiem, chuoi_tim_kiem

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
