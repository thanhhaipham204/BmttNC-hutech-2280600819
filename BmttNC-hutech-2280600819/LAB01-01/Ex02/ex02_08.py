def chia_het_cho_5(so_nhi_phan):
    so_thap_phan = int(so_nhi_phan, 2)
    if so_thap_phan % 5==0:
        return True
    else:
        return False
chuoi_nhi_phan = input("Nhập chuỗi số nhị phân (phân tách bởi dấu phẩy):")
so_thap_phan_list = chuoi_nhi_phan.split(',')
so_chia_het_cho_5 = [so for so in so_thap_phan_list if chia_het_cho_5(so)]
ket_qua = ', '.join(so_chia_het_cho_5)
if so_chia_het_cho_5:
    print("Các số nhị phân chia hết cho 5 là:", ket_qua)
else:
    print("Không có số nào chia hết cho 5 trong chuỗi đã nhập.")