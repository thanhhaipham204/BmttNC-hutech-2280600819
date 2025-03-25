so_gio_lam = float(input("Nhập số giờ làm mỗi tuần: "))
Luong_gio = float(input("Nhập thù lao trên mỗi giờ làm tiêu chuẩn: "))
gio_tieu_chuan = 44 
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan)
thuc_linh = so_gio_lam * Luong_gio + gio_vuot_chuan * Luong_gio * 1.5
print(f"số tiền thực lĩnh của nhân viên: {thuc_linh}")