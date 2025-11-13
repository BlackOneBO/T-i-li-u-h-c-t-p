print("Chương trình tính Chỉ số gió lạnh (WCI)")

try:
    # 1. Đọc nhiệt độ và tốc độ gió từ người dùng
    Ta = float(input("Nhập nhiệt độ không khí (độ C): "))
    V = float(input("Nhập tốc độ gió (km/giờ): "))

    if V < 0:
        print("Lỗi: Tốc độ gió không thể là số âm.")
    else:
        # 2. Tính toán WCI theo công thức
        # WCI = 13.12 + 0.6215*Ta - 11.37*V**0.16 + 0.3965*Ta*V**0.16

        V_pow_016 = V ** 0.16

        # Áp dụng công thức chính xác (dùng ** cho lũy thừa)
        wci = 13.12 + 0.6215 * Ta - 11.37 * V_pow_016 + 0.3965 * Ta * V_pow_016

        # 3. Làm tròn kết quả đến số nguyên gần nhất
        wci_rounded = round(wci)

        # 4. Hiển thị kết quả
        print("\n--- KẾT QUẢ ---")
        print(f"Giá trị WCI (chưa làm tròn): {wci:.2f}")
        print(f"Chỉ số gió lạnh (làm tròn): {wci_rounded}")

except ValueError:
    print("\nLỗi: Bạn phải nhập vào là SỐ. Vui lòng chạy lại chương trình.")