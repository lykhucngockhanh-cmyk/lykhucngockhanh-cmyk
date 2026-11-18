
# ============================================================
# CHUONG TRINH TINH TIEN DIEN
# Quan ly khach hang va tinh tien dien
# ============================================================

import csv

FILE_DATA = "du_lieu_khach_hang.txt"

# Bang gia dien mau (VND/kWh).
BAC_GIA = [
    (50, 1806),
    (50, 1866),
    (100, 2167),
    (200, 2729),
    (100, 3050),
    (float("inf"), 3151)
]

danh_sach_khach_hang = []


def ke_ngang(ky_tu="=", do_dai=58):
    print(ky_tu * do_dai)


def hien_thi_menu():
    """Hien thi menu theo bo cuc."""
    print()
    ke_ngang("=")
    print("                CHUONG TRINH TINH TIEN DIEN")
    ke_ngang("=")
    print()
    print("QUAN LY KHACH HANG                 TRA CUU VA SAP XEP")
    print()
    print("1. Them khach hang                 5. Tim kiem khach hang")
    print("2. Hien thi danh sach              6. Sap xep khach hang")
    print("3. Cap nhat thong tin")
    print("4. Xoa khach hang")
    print()
    print("TINH TOAN VA THONG KE              QUAN LY DU LIEU")
    print()
    print("7. Tinh tien dien                  9. Luu du lieu vao file TXT")
    print("8. Thong ke tien dien              10. Doc du lieu tu file TXT")
    print()
    print("0. Thoat chuong trinh")
    print()
    ke_ngang("-")


def nhap_so_nguyen(thong_bao, toi_thieu=None):
    while True:
        try:
            gia_tri = int(input(thong_bao))

            if toi_thieu is not None and gia_tri < toi_thieu:
                print(f"Vui long nhap so >= {toi_thieu}.")
                continue

            return gia_tri

        except ValueError:
            print("Du lieu khong hop le. Vui long nhap so nguyen.")


def tim_khach_hang(ma_kh):
    for kh in danh_sach_khach_hang:
        if kh["ma"] == ma_kh:
            return kh
    return None


def tinh_tien(kWh):
    """Tinh tien dien theo bac thang va tra ve tong tien, chi tiet."""
    chi_tiet = []
    tong_tien = 0
    con_lai = kWh

    for gioi_han, don_gia in BAC_GIA:
        if con_lai <= 0:
            break

        so_kwh = min(con_lai, gioi_han)
        thanh_tien = so_kwh * don_gia

        chi_tiet.append((so_kwh, don_gia, thanh_tien))
        tong_tien += thanh_tien
        con_lai -= so_kwh

    return tong_tien, chi_tiet


def them_khach_hang():
    print("\n-------- THEM KHACH HANG --------")

    ma = input("Nhap ma khach hang: ").strip()

    if not ma:
        print("Ma khach hang khong duoc de trong.")
        return

    if tim_khach_hang(ma):
        print("Ma khach hang da ton tai.")
        return

    ten = input("Nhap ten khach hang: ").strip()

    if not ten:
        print("Ten khach hang khong duoc de trong.")
        return

    chi_so_cu = nhap_so_nguyen("Nhap chi so dien cu (kWh): ", toi_thieu=0)
    chi_so_moi = nhap_so_nguyen("Nhap chi so dien moi (kWh): ", toi_thieu=chi_so_cu)

    dien_tieu_thu = chi_so_moi - chi_so_cu

    kh = {
        "ma": ma,
        "ten": ten,
        "cu": chi_so_cu,
        "moi": chi_so_moi,
        "tieu_thu": dien_tieu_thu
    }
    danh_sach_khach_hang.append(kh)
    print("-> Them khach hang thanh cong!")


def hien_thi_danh_sach():
    print("\n---------------------- DANH SACH KHACH HANG ---------------------")

    if not danh_sach_khach_hang:
        print("Danh sach trong.")
        return

    print(
        f"{'Ma KH':<10} | {'Ho Ten':<20} | "
        f"{'So Cu':<8} | {'So Moi':<8} | {'Tieu Thu':<8}"
    )

    ke_ngang("-", 65)

    for kh in danh_sach_khach_hang:
        print(
            f"{kh['ma']:<10} | {kh['ten']:<20} | "
            f"{kh['cu']:<8} | {kh['moi']:<8} | "
            f"{kh['tieu_thu']:<8}"
        )


def cap_nhat_thong_tin():
    print("\n-------- CAP NHAT THONG TIN --------")

    ma = input("Nhap ma khach hang can cap nhat: ").strip()
    kh = tim_khach_hang(ma)

    if not kh:
        print("Khong tim thay khach hang.")
        return

    print(f"Dang sua thong tin cho: {kh['ten']}")

    kh['ten'] = (
        input(f"Ten moi (Bo qua nhap lai '{kh['ten']}'): ").strip()
        or kh['ten']
    )

    kh['cu'] = nhap_so_nguyen(
        f"Chi so cu moi [{kh['cu']}]: ", toi_thieu=0
    )

    kh['moi'] = nhap_so_nguyen(
        f"Chi so moi moi [{kh['moi']}]: ",
        toi_thieu=kh['cu']
    )

    kh['tieu_thu'] = kh['moi'] - kh['cu']

    print("-> Cap nhat thanh cong!")


def xoa_khach_hang():
    print("\n-------- XOA KHACH HANG --------")

    ma = input("Nhap ma khach hang can xoa: ").strip()
    kh = tim_khach_hang(ma)

    if not kh:
        print("Khong tim thay khach hang.")
        return

    danh_sach_khach_hang.remove(kh)
    print("-> Xoa khach hang thanh cong!")



def tim_kiem_khach_hang():
    print("\n============= TIM KIEM KHACH HANG =============")
    tu_khoa = input("Nhap ma hoac ten khach hang can tim: ").strip().lower()

    if not tu_khoa:
        print("Vui long nhap tu khoa tim kiem.")
        return

    ket_qua = [kh for kh in danh_sach_khach_hang
               if tu_khoa == kh['ma'].lower()
               or tu_khoa in kh['ten'].lower().split()]

    if not ket_qua:
        print("\nKhong tim thay khach hang phu hop.")
        print("=" * 50)
        return

    print("\n-------------- KET QUA TIM KIEM --------------")
    print(f"Tim thay: {len(ket_qua)} khach hang\n")
    print("+----------+----------------------+--------------+")
    print("| Ma KH    | Ten khach hang       | Tieu thu     |")
    print("+----------+----------------------+--------------+")

    for kh in ket_qua:
        print(f"| {kh['ma']:<8} | {kh['ten']:<20} | "
              f"{str(kh['tieu_thu']) + ' kWh':<12} |")

    print("+----------+----------------------+--------------+")
    print("\n============== KET THUC TIM KIEM ==============")

 


def sap_xep_khach_hang():
    print("\n-------- SAP XEP KHACH HANG --------")

    if not danh_sach_khach_hang:
        print("Danh sach trong, khong co du lieu de sap xep.")
        return

    print("1. Theo ma khach hang")
    print("2. Theo luong dien tieu thu (giam dan)")

    chon = input("Lua chon cua ban: ").strip()

    if chon == '1':
        danh_sach_khach_hang.sort(key=lambda x: x['ma'])
        print("-> Da sap xep theo ma khach hang!")

    elif chon == '2':
        danh_sach_khach_hang.sort(
            key=lambda x: x['tieu_thu'], reverse=True
        )
        print("-> Da sap xep theo luong dien tieu thu giam dan!")

    else:
        print("Lua chon khong hop le.")


def tinh_va_hien_thi_tien_dien():
    print("\n------------ TINH TIEN DIEN -------------")

    ma = input("Nhap ma khach hang: ").strip()
    kh = tim_khach_hang(ma)

    if not kh:
        print("Khong tim thay khach hang.")
        return

    tong, chi_tiet = tinh_tien(kh['tieu_thu'])

    print(
        f"\nHoa don dien cho khach hang: "
        f"{kh['ten']} (Ma: {kh['ma']})"
    )

    print(f"Tieu thu: {kh['tieu_thu']} kWh")

    print(
        f"{'Bac':<6} | {'So kWh':<8} | "
        f"{'Don gia':<10} | {'Thanh tien':<12}"
    )

    ke_ngang("-", 45)

    for i, (skwh, dg, tt) in enumerate(chi_tiet, 1):
        print(f"Bac {i:<2} | {skwh:<8} | {dg:<10} | {tt:<12}")

    ke_ngang("-", 45)
    print(f"TONG TIEN PHAI TRA: {tong:,} VND")


def thong_ke_tien_dien():
    print("\n------------ THONG KE TIEN DIEN -------------")

    if not danh_sach_khach_hang:
        print("Danh sach trong.")
        return

    tong_tieu_thu = sum(
        kh['tieu_thu'] for kh in danh_sach_khach_hang
    )

    tong_doanh_thu = sum(
        tinh_tien(kh['tieu_thu'])[0]
        for kh in danh_sach_khach_hang
    )

    print(f"Tong so luong khach hang: {len(danh_sach_khach_hang)}")
    print(f"Tong dien nang tieu thu: {tong_tieu_thu} kWh")
    print(f"Tong doanh thu tien dien: {tong_doanh_thu:,} VND")


def luu_file():
    try:
        with open(
            FILE_DATA, "w", encoding="utf-8", newline=""
        ) as f:
            writer = csv.writer(f)

            for kh in danh_sach_khach_hang:
                writer.writerow([
                    kh['ma'],
                    kh['ten'],
                    kh['cu'],
                    kh['moi'],
                    kh['tieu_thu']
                ])

        print("-> Luu du lieu vao file thanh cong!")

    except OSError as e:
        print(f"Loi khi luu file: {e}")


def doc_file():
    global danh_sach_khach_hang
    danh_sach_moi, danh_sach_ma = [], set()
    try:
        with open(FILE_DATA, "r", encoding="utf-8", newline="") as f:
            for parts in csv.reader(f):
                if not parts: continue
                try:
                    if len(parts) != 5: continue
                    ma, ten = parts[0].strip(), parts[1].strip()
                    cu, moi, tieu_thu = int(parts[2]), int(parts[3]), int(parts[4])
                    if not ma or not ten or cu < 0 or moi < cu: continue
                    if tieu_thu != moi - cu or ma in danh_sach_ma: continue
                    
                    danh_sach_moi.append({"ma": ma, "ten": ten, "cu": cu, "moi": moi, "tieu_thu": tieu_thu})
                    danh_sach_ma.add(ma)
                except (ValueError, IndexError):
                    continue
        danh_sach_khach_hang = danh_sach_moi
        print(f"-> Doc du lieu thanh cong! Da doc {len(danh_sach_khach_hang)} khach hang.")
    except FileNotFoundError:
        print("Khong tim thay file du lieu.")
    except (OSError, csv.Error) as e:
        print(f"Loi khi doc file: {e}")


def main():
    while True:
        hien_thi_menu()

        lua_chon = input("Nhap lua chon cua ban: ").strip()

        if lua_chon == '1':
            them_khach_hang()

        elif lua_chon == '2':
            hien_thi_danh_sach()

        elif lua_chon == '3':
            cap_nhat_thong_tin()

        elif lua_chon == '4':
            xoa_khach_hang()

        elif lua_chon == '5':
            tim_kiem_khach_hang()

        elif lua_chon == '6':
            sap_xep_khach_hang()

        elif lua_chon == '7':
            tinh_va_hien_thi_tien_dien()

        elif lua_chon == '8':
            thong_ke_tien_dien()

        elif lua_chon == '9':
            luu_file()

        elif lua_chon == '10':
            doc_file()

        elif lua_chon == '0':
            print("Cam on ban yeu da su dung chuong trinh. Tam biet!")
            break

        else:
            print("Lua chon khong hop le. Vui long chon tu 0 den 10.")

        input("\nNhan Enter de tiep tuc...")


if __name__ == "__main__":
    main()
