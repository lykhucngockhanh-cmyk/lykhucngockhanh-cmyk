from datetime import date
import os


# Duong dan file du lieu
DUONG_DAN_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "don_giat.txt"
)


# Bang gia dich vu giat la
BANG_GIA = {
    "1": {"ten": "Giat thuong", "don_gia": 15000},
    "2": {"ten": "Giat nhanh", "don_gia": 20000},
    "3": {"ten": "Giat say", "don_gia": 25000}
}


# Hien thi menu chinh
def hien_thi_menu():
    print("\n========== QUAN LY TIEM GIAT LA ==========")
    print("1. Tiep nhan don giat la")
    print("2. Hien thi danh sach don")
    print("3. Cap nhat don giat la")
    print("4. Xoa don giat la")
    print("5. Tim kiem don giat la")
    print("6. Sap xep don giat la")
    print("7. Hoan thanh don va tra do")
    print("8. Thong ke")
    print("9. Luu du lieu")
    print("10. Doc du lieu")
    print("11. Thoat")
    print("==========================================")


# Dinh dang tien
def dinh_dang_tien(tien):
    return f"{tien:,.0f}".replace(",", ".") + " VND"


# Nhap khoi luong va kiem tra
def nhap_khoi_luong():
    while True:
        try:
            khoi_luong = float(input("Nhap khoi luong (kg): "))

            if khoi_luong <= 0:
                print("Khoi luong phai lon hon 0!")
            else:
                return khoi_luong

        except ValueError:
            print("Loi: Vui long nhap mot con so!")


# Tim don theo ma
def tim_don_theo_ma(danh_sach_don, ma_can_tim):
    for don in danh_sach_don:
        if don["ma_don"].lower() == ma_can_tim.lower():
            return don

    return None


# Tiep nhan don giat la
def tiep_nhan_don(danh_sach_don):
    print("\n========== TIEP NHAN DON GIAT LA ==========")

    # Nhap ma don
    while True:
        ma_don = input("Nhap ma don: ").strip()

        if ma_don == "":
            print("Ma don khong duoc de trong!")
        elif tim_don_theo_ma(danh_sach_don, ma_don) is not None:
            print("Ma don da ton tai!")
        else:
            break

    # Nhap ten khach hang
    while True:
        ten_khach = input("Nhap ten khach hang: ").strip()

        if ten_khach == "":
            print("Ten khach hang khong duoc de trong!")
        else:
            break

    # Nhap so dien thoai
    while True:
        sdt = input("Nhap so dien thoai: ").strip()

        if sdt == "":
            print("So dien thoai khong duoc de trong!")
        else:
            break

    # Chon dich vu
    print("\nDanh sach dich vu:")

    for ma, dich_vu in BANG_GIA.items():
        print(
            ma + ". " + dich_vu["ten"]
            + " - " + dinh_dang_tien(dich_vu["don_gia"]) + "/kg"
        )

    while True:
        lua_chon = input("Chon dich vu (1-3): ").strip()

        if lua_chon in BANG_GIA:
            break
        else:
            print("Dich vu khong hop le!")

    dich_vu = BANG_GIA[lua_chon]["ten"]
    don_gia = BANG_GIA[lua_chon]["don_gia"]

    # Nhap khoi luong
    khoi_luong = nhap_khoi_luong()

    # Tinh thanh tien
    thanh_tien = khoi_luong * don_gia

    # Lay ngay nhan hien tai
    ngay_nhan = date.today().strftime("%d/%m/%Y")

    # Tao don giat
    don_giat = {
        "ma_don": ma_don,
        "ten_khach": ten_khach,
        "sdt": sdt,
        "dich_vu": dich_vu,
        "khoi_luong": khoi_luong,
        "don_gia": don_gia,
        "ngay_nhan": ngay_nhan,
        "ngay_tra": "",
        "trang_thai": "Dang xu ly",
        "thanh_tien": thanh_tien
    }

    danh_sach_don.append(don_giat)

    print("\nTiep nhan don thanh cong!")
    print("Ma don:", ma_don)
    print("Thanh tien:", dinh_dang_tien(thanh_tien))


# Hien thi thong tin mot don
def hien_thi_mot_don(don):
    print("------------------------------------------")
    print("Ma don:", don["ma_don"])
    print("Ten khach:", don["ten_khach"])
    print("So dien thoai:", don["sdt"])
    print("Dich vu:", don["dich_vu"])
    print("Khoi luong:", don["khoi_luong"], "kg")
    print("Don gia:", dinh_dang_tien(don["don_gia"]))
    print("Ngay nhan:", don["ngay_nhan"])

    if don["ngay_tra"] == "":
        print("Ngay tra: Chua tra")
    else:
        print("Ngay tra:", don["ngay_tra"])

    print("Trang thai:", don["trang_thai"])
    print("Thanh tien:", dinh_dang_tien(don["thanh_tien"]))


# Hien thi danh sach don
def hien_thi_danh_sach(danh_sach_don):
    print("\n========== DANH SACH DON GIAT LA ==========")

    if len(danh_sach_don) == 0:
        print("Chua co don giat la nao!")
        return

    for don in danh_sach_don:
        hien_thi_mot_don(don)

    print("------------------------------------------")
    print("Tong so don:", len(danh_sach_don))


# Cap nhat don giat la
def cap_nhat_don(danh_sach_don):
    print("\n========== CAP NHAT DON GIAT LA ==========")

    ma_don = input("Nhap ma don can cap nhat: ").strip()

    if ma_don == "":
        print("Ma don khong duoc de trong!")
        return

    don = tim_don_theo_ma(danh_sach_don, ma_don)

    if don is None:
        print("Khong tim thay don giat la!")
        return

    print("\nThong tin don hien tai:")
    hien_thi_mot_don(don)

    while True:
        print("\nChon thong tin can cap nhat:")
        print("1. Ten khach hang")
        print("2. So dien thoai")
        print("3. Loai dich vu")
        print("4. Khoi luong")
        print("0. Quay lai menu chinh")

        lua_chon = input("Nhap lua chon: ").strip()

        if lua_chon == "1":
            ten_khach = input("Nhap ten khach hang moi: ").strip()

            if ten_khach == "":
                print("Ten khach hang khong duoc de trong!")
            else:
                don["ten_khach"] = ten_khach
                print("Cap nhat ten khach thanh cong!")

        elif lua_chon == "2":
            sdt = input("Nhap so dien thoai moi: ").strip()

            if sdt == "":
                print("So dien thoai khong duoc de trong!")
            else:
                don["sdt"] = sdt
                print("Cap nhat so dien thoai thanh cong!")

        elif lua_chon == "3":
            print("\nDanh sach dich vu:")

            for ma, dich_vu in BANG_GIA.items():
                print(
                    ma + ". " + dich_vu["ten"]
                    + " - " + dinh_dang_tien(dich_vu["don_gia"]) + "/kg"
                )

            chon_dich_vu = input("Chon dich vu moi (1-3): ").strip()

            if chon_dich_vu in BANG_GIA:
                don["dich_vu"] = BANG_GIA[chon_dich_vu]["ten"]
                don["don_gia"] = BANG_GIA[chon_dich_vu]["don_gia"]

                don["thanh_tien"] = (
                    don["khoi_luong"] * don["don_gia"]
                )

                print("Cap nhat dich vu thanh cong!")
                print("Thanh tien moi:", dinh_dang_tien(
                    don["thanh_tien"]
                ))
            else:
                print("Dich vu khong hop le!")

        elif lua_chon == "4":
            khoi_luong = nhap_khoi_luong()

            don["khoi_luong"] = khoi_luong

            don["thanh_tien"] = (
                don["khoi_luong"] * don["don_gia"]
            )

            print("Cap nhat khoi luong thanh cong!")
            print("Thanh tien moi:", dinh_dang_tien(
                don["thanh_tien"]
            ))

        elif lua_chon == "0":
            break

        else:
            print("Lua chon khong hop le!")

    print("\nThong tin don sau khi cap nhat:")
    hien_thi_mot_don(don)


# Xoa don giat la
def xoa_don(danh_sach_don):
    print("\n========== XOA DON GIAT LA ==========")

    ma_don = input("Nhap ma don can xoa: ").strip()

    if ma_don == "":
        print("Ma don khong duoc de trong!")
        return

    don = tim_don_theo_ma(danh_sach_don, ma_don)

    if don is None:
        print("Khong tim thay don giat la!")
        return

    print("\nDon giat la can xoa:")
    hien_thi_mot_don(don)

    xac_nhan = input("Ban co chac chan muon xoa? (y/n): ")
    xac_nhan = xac_nhan.strip().lower()

    if xac_nhan == "y":
        danh_sach_don.remove(don)
        print("Da xoa don giat la thanh cong!")
    else:
        print("Da huy thao tac xoa!")

# Tim kiem don giat la
def tim_kiem_don(danh_sach_don):
    print("\n========== TIM KIEM DON GIAT LA ==========")

    if len(danh_sach_don) == 0:
        print("Chua co don giat la nao!")
        return

    print("1. Tim theo ma don")
    print("2. Tim theo ten khach hang")
    print("3. Tim theo so dien thoai")
    print("4. Tim theo trang thai")

    lua_chon = input("Chon cach tim kiem: ").strip()

    if lua_chon == "1":
        truong = "ma_don"

    elif lua_chon == "2":
        truong = "ten_khach"

    elif lua_chon == "3":
        truong = "sdt"

    elif lua_chon == "4":
        truong = "trang_thai"

    else:
        print("Lua chon khong hop le!")
        return

    tu_khoa = input("Nhap tu khoa can tim: ").strip().lower()

    if tu_khoa == "":
        print("Tu khoa khong duoc de trong!")
        return

    ket_qua = []

    for don in danh_sach_don:
        gia_tri = str(don[truong]).lower()

        if tu_khoa in gia_tri:
            ket_qua.append(don)

    if len(ket_qua) == 0:
        print("Khong tim thay don giat la!")

    else:
        print("\nTim thay", len(ket_qua), "don giat la:")

        for don in ket_qua:
            hien_thi_mot_don(don)

# Sap xep don giat la
def sap_xep_don(danh_sach_don):
    print("\n========== SAP XEP DON GIAT LA ==========")

    if len(danh_sach_don) == 0:
        print("Chua co don giat la nao!")
        return

    print("1. Sap xep theo ngay nhan")
    print("2. Sap xep theo thanh tien")
    print("3. Sap xep theo trang thai")

    lua_chon = input("Chon tieu chi sap xep: ").strip()

    if lua_chon not in ["1", "2", "3"]:
        print("Lua chon khong hop le!")
        return

    print("\n1. Tang dan")
    print("2. Giam dan")

    thu_tu = input("Chon thu tu sap xep: ").strip()

    if thu_tu not in ["1", "2"]:
        print("Thu tu sap xep khong hop le!")
        return

    if lua_chon == "1":
        # Sap xep theo ngay nhan
        from datetime import datetime

        danh_sach_sap_xep = sorted(
            danh_sach_don,
            key=lambda don: datetime.strptime(
                don["ngay_nhan"], "%d/%m/%Y"
            ),
            reverse=(thu_tu == "2")
        )

    elif lua_chon == "2":
        # Sap xep theo thanh tien
        danh_sach_sap_xep = sorted(
            danh_sach_don,
            key=lambda don: don["thanh_tien"],
            reverse=(thu_tu == "2")
        )

    else:
        # Sap xep theo trang thai
        danh_sach_sap_xep = sorted(
            danh_sach_don,
            key=lambda don: don["trang_thai"].lower(),
            reverse=(thu_tu == "2")
        )

    print("\n========== KET QUA SAP XEP ==========")

    for don in danh_sach_sap_xep:
        hien_thi_mot_don(don)

# Hoan thanh don va tra do
def xu_ly_tra_do(danh_sach_don):
    print("\n========== HOAN THANH DON VA TRA DO ==========")

    if len(danh_sach_don) == 0:
        print("Chua co don giat la nao!")
        return

    print("1. Danh dau don da hoan thanh")
    print("2. Tra do cho khach")
    print("0. Quay lai menu chinh")

    lua_chon = input("Nhap lua chon: ").strip()

    if lua_chon == "0":
        return

    if lua_chon not in ["1", "2"]:
        print("Lua chon khong hop le!")
        return

    ma_don = input("Nhap ma don: ").strip()

    if ma_don == "":
        print("Ma don khong duoc de trong!")
        return

    don = tim_don_theo_ma(danh_sach_don, ma_don)

    if don is None:
        print("Khong tim thay don giat la!")
        return

    if lua_chon == "1":
        if don["trang_thai"] == "Dang xu ly":
            don["trang_thai"] = "Hoan thanh"
            print("Don da duoc danh dau hoan thanh!")

        elif don["trang_thai"] == "Hoan thanh":
            print("Don nay da hoan thanh roi!")

        else:
            print("Don nay da duoc tra cho khach!")

    elif lua_chon == "2":
        if don["trang_thai"] == "Dang xu ly":
            print("Don chua hoan thanh, chua the tra do!")

        elif don["trang_thai"] == "Hoan thanh":
            from datetime import date

            don["trang_thai"] = "Da tra"
            don["ngay_tra"] = date.today().strftime("%d/%m/%Y")

            print("Tra do cho khach thanh cong!")
            print("Ngay tra:", don["ngay_tra"])

        else:
            print("Don nay da duoc tra truoc do!")

    print("\nThong tin don sau khi xu ly:")
    hien_thi_mot_don(don)

# Thong ke don giat la
def thong_ke(danh_sach_don):
    print("\n========== THONG KE TIEM GIAT LA ==========")

    tong_so_don = len(danh_sach_don)
    so_dang_xu_ly = 0
    so_da_tra = 0
    tong_doanh_thu = 0

    doanh_thu_theo_dich_vu = {}

    for don in danh_sach_don:

        if don["trang_thai"] == "Dang xu ly":
            so_dang_xu_ly += 1

        if don["trang_thai"] == "Da tra":
            so_da_tra += 1

            # Chi tinh doanh thu tu don da tra
            tong_doanh_thu += don["thanh_tien"]

            dich_vu = don["dich_vu"]

            if dich_vu not in doanh_thu_theo_dich_vu:
                doanh_thu_theo_dich_vu[dich_vu] = 0

            doanh_thu_theo_dich_vu[dich_vu] += don["thanh_tien"]

    print("Tong so don:", tong_so_don)
    print("So don dang xu ly:", so_dang_xu_ly)
    print("So don da tra:", so_da_tra)

    print("Tong doanh thu:", dinh_dang_tien(tong_doanh_thu))

    print("\nDOANH THU THEO DICH VU:")

    if len(doanh_thu_theo_dich_vu) == 0:
        print("Chua co doanh thu tu don da tra!")
    else:
        for dich_vu, doanh_thu in doanh_thu_theo_dich_vu.items():
            print(dich_vu + ":", dinh_dang_tien(doanh_thu))

    print("==========================================")

# Luu du lieu vao file TXT
def luu_du_lieu(danh_sach_don):
    if len(danh_sach_don) == 0:
        print("Danh sach dang rong, khong co du lieu de luu!")
        return

    try:
        with open(DUONG_DAN_FILE, "w", encoding="utf-8") as f:
            for don in danh_sach_don:
                cac_truong = [
                    str(don["ma_don"]).replace("|", "/"),
                    str(don["ten_khach"]).replace("|", "/"),
                    str(don["sdt"]).replace("|", "/"),
                    str(don["dich_vu"]).replace("|", "/"),
                    str(don["khoi_luong"]),
                    str(don["don_gia"]),
                    str(don["ngay_nhan"]).replace("|", "/"),
                    str(don["ngay_tra"]).replace("|", "/"),
                    str(don["trang_thai"]).replace("|", "/"),
                    str(don["thanh_tien"])
                ]

                f.write("|".join(cac_truong) + "\n")

        print(
            "Da luu", len(danh_sach_don),
            "don vao file don_giat.txt"
        )

    except OSError:
        print("Khong the ghi file don_giat.txt!")

# Doc du lieu tu file TXT
def doc_du_lieu(danh_sach_don):
    try:
        with open(DUONG_DAN_FILE, "r", encoding="utf-8") as f:
            danh_sach_moi = []

            for so_dong, dong in enumerate(f, start=1):
                cac_truong = dong.rstrip("\n").split("|")

                if dong.rstrip("\n") == "":
                    continue

                if len(cac_truong) != 10:
                    print(
                        "Bo qua dong", so_dong,
                        "vi du lieu khong hop le."
                    )
                    continue

                try:
                    don = {
                        "ma_don": cac_truong[0],
                        "ten_khach": cac_truong[1],
                        "sdt": cac_truong[2],
                        "dich_vu": cac_truong[3],
                        "khoi_luong": float(cac_truong[4]),
                        "don_gia": int(cac_truong[5]),
                        "ngay_nhan": cac_truong[6],
                        "ngay_tra": cac_truong[7],
                        "trang_thai": cac_truong[8],
                        "thanh_tien": float(cac_truong[9])
                    }

                except ValueError:
                    print(
                        "Bo qua dong", so_dong,
                        "vi du lieu so khong hop le."
                    )
                    continue

                # Kiem tra ma don trung
                if tim_don_theo_ma(
                    danh_sach_moi, don["ma_don"]
                ) is None:
                    danh_sach_moi.append(don)
                else:
                    print("Bo qua ma don trung:", don["ma_don"])

            danh_sach_don.clear()
            danh_sach_don.extend(danh_sach_moi)

            print(
                "Da doc", len(danh_sach_don),
                "don tu file don_giat.txt"
            )

    except FileNotFoundError:
        print("Chua co file don_giat.txt. Hay luu du lieu truoc!")

    except OSError:
        print("Khong the doc file don_giat.txt!")

# Chuong trinh chinh
def main():
    danh_sach_don = []

    while True:
        hien_thi_menu()
        lua_chon = input("Nhap lua chon: ").strip()

        if lua_chon == "1":
            tiep_nhan_don(danh_sach_don)
        elif lua_chon == "2":
            hien_thi_danh_sach(danh_sach_don)
        elif lua_chon == "3":
            cap_nhat_don(danh_sach_don)
        elif lua_chon == "4":
            xoa_don(danh_sach_don)
        elif lua_chon == "5":
            tim_kiem_don(danh_sach_don)
        elif lua_chon == "6":
            sap_xep_don(danh_sach_don)
        elif lua_chon == "7":
            xu_ly_tra_do(danh_sach_don)
        elif lua_chon == "8":
            thong_ke(danh_sach_don)
        elif lua_chon == "9":
            luu_du_lieu(danh_sach_don)
        elif lua_chon == "10":
            doc_du_lieu(danh_sach_don)
        elif lua_chon == "11":
            print("Da thoat chuong trinh.")
            break
        else:
            print("Lua chon khong hop le!")


if __name__ == "__main__":
    main()
