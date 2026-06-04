# --- DỮ LIỆU MẪU BAN ĐẦU ---
cart_items = [
    ["P001", "Dien thoai iPhone 15", 1, 25000000],
    ["P002", "Op lung Silicon", 2, 150000]
]

# --- VÒNG LẶP CHÍNH ĐIỀU KHIỂN MENU ---
while True:
    print("\n================ SHOPEE CART MANAGEMENT SYSTEM ================")
    print("[1] Xem chi tiết giỏ hàng & Tính tổng tiền")
    print("[2] Thêm sản phẩm mới / Cộng dồn số lượng")
    print("[3] Cập nhật số lượng của một sản phẩm")
    print("[4] Xóa sản phẩm khỏi giỏ hàng")
    print("[5] Thoát chương trình")
    print("===============================================================")
    
    luachon = input("Mời bạn chọn chức năng (1-5): ").strip()

    # ÁP DỤNG MATCH...CASE ĐỂ ĐIỀU HƯỚNG MENU
    match luachon:
        
        # ---------------------------------------------------------------------
        # CHỨC NĂNG 1: XEM CHI TIẾT GIỎ HÀNG & TÍNH TỔNG TIỀN
        # ---------------------------------------------------------------------
        case "1":
            print("\n--- CHI TIẾT GIỎ HÀNG ---")
            print(f"{'STT':<5} | {'Mã SP':<8} | {'Tên Sản Phẩm':<25} | {'SL':<5} | {'Đơn Giá':<12} | {'Thành Tiền':<15}")
            print("-" * 80)
            
            tong_so_luong = 0
            tong_tien_gio_hang = 0
            
            # Duyệt danh sách và dùng match...case để unpack (bóc tách) dữ liệu sản phẩm
            for i, sp in enumerate(cart_items, start=1):
                match sp:
                    case [ma_sp, ten_sp, so_luong, don_gia]:
                        thanh_tien = so_luong * don_gia
                        tong_so_luong += so_luong
                        tong_tien_gio_hang += thanh_tien
                        
                        print(f"{i:<5} | {ma_sp:<8} | {ten_sp:<25} | {so_luong:<5} | {don_gia:<12,}đ | {thanh_tien:<15,}đ")
                
            print("-" * 80)
            print(f"⇒ Tổng số lượng sản phẩm trong giỏ: {tong_so_luong}")
            print(f"⇒ TỔNG TIỀN THANH TOÁN: {tong_tien_gio_hang:,}đ")

        # ---------------------------------------------------------------------
        # CHỨC NĂNG 2: THÊM SẢN PHẨM MỚI HOẶC TĂNG SỐ LƯỢNG
        # ---------------------------------------------------------------------
        case "2":
            print("\n--- THÊM SẢN PHẨM MỚI / CỘNG DỒN SỐ LƯỢNG ---")
            ma_nhap = input("Nhập mã sản phẩm: ").strip()
            ten_nhap = input("Nhập tên sản phẩm: ").strip()
            so_luong_nhap = int(input("Nhập số lượng: "))
            don_gia_nhap = float(input("Nhập đơn giá: "))
            
            # Kiểm tra Edge Cases bằng cách gộp các điều kiện lỗi vào một cấu trúc match
            match (so_luong_nhap, don_gia_nhap):
                case (s, _) if s <= 0:
                    print("❌ Lỗi: Số lượng sản phẩm phải lớn hơn 0!")
                    continue
                case (_, d) if d < 0:
                    print("❌ Lỗi: Đơn giá không được nhỏ hơn 0!")
                    continue

            # Tiến hành kiểm tra trùng mã sản phẩm
            found = False
            for sp in cart_items:
                if sp[0] == ma_nhap:
                    sp[2] += so_luong_nhap  # Cộng dồn số lượng vào phần tử index 2
                    found = True
                    print(f" Thông báo: Đã cộng dồn {so_luong_nhap} sản phẩm vào mã {ma_nhap}.")
                    break
            
            if not found:
                cart_items.append([ma_nhap, ten_nhap, so_luong_nhap, don_gia_nhap])
                print(" Chúc mừng: Thêm sản phẩm mới vào giỏ hàng thành công!")

        # ---------------------------------------------------------------------
        # CHỨC NĂNG 3: CẬP NHẬT SỐ LƯỢNG SẢN PHẨM
        # ---------------------------------------------------------------------
        case "3":
            print("\n--- CẬP NHẬT SỐ LƯỢNG SẢN PHẨM ---")
            ma_can_sua = input("Nhập mã sản phẩm cần sửa: ").strip()
            
            found = False
            for sp in cart_items:
                if sp[0] == ma_can_sua:
                    found = True
                    so_luong_moi = int(input(f"Nhập số lượng mới cho sản phẩm '{sp[1]}': "))
                    
                    # Sử dụng match case kết hợp if guard để check số lượng hợp lệ
                    match so_luong_moi:
                        case s if s <= 0:
                            print("❌ Lỗi: Số lượng cập nhật phải lớn hơn 0!")
                        case _:
                            sp[2] = so_luong_moi
                            print(" Cập nhật số lượng thành công!")
                    break
                    
            if not found:
                print("❌ Lỗi: Mã sản phẩm không tồn tại trong giỏ hàng.")

        # ---------------------------------------------------------------------
        # CHỨC NĂNG 4: XÓA SẢN PHẨM KHỎI GIỎ HÀNG
        # ---------------------------------------------------------------------
        case "4":
            print("\n--- XÓA SẢN PHẨM KHỎI GIỎ HÀNG ---")
            ma_can_xoa = input("Nhập mã sản phẩm muốn xóa: ").strip()
            
            found = False
            for sp in cart_items:
                if sp[0] == ma_can_xoa:
                    cart_items.remove(sp)
                    found = True
                    print(f"🗑️ Đã xóa hoàn toàn sản phẩm có mã {ma_can_xoa} khỏi giỏ hàng.")
                    break
                    
            if not found:
                print("❌ Lỗi: Mã sản phẩm không tồn tại trong giỏ hàng.")

        # ---------------------------------------------------------------------
        # CHỨC NĂNG 5: THOÁT CHƯƠNG TRÌNH
        # ---------------------------------------------------------------------
        case "5":
            print("\n👋 Cảm ơn bạn đã sử dụng hệ thống quản lý Shopee Cart. Tạm biệt!")
            break

        # ---------------------------------------------------------------------
        # BẪY DỮ LIỆU (EDGE CASE 3): NGƯỜI DÙNG NHẬP SAI MENU (KÝ TỰ LẠ / CHỮ)
        # ---------------------------------------------------------------------
        case _:
            print("❌ Lỗi: Lựa chọn không hợp lệ! Vui lòng nhập số từ 1 đến 5.")
