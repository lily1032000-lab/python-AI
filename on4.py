# giống với on3.py logic nhưng khác ở ngữ cảnh 
user_box = [
    "alex",               # Ngắn hơn 5 ký tự -> Bị loại ngay ở Tầng 1
    "member_2026",        # Dài hơn 5 ký tự, nhưng không có test/guest -> Bị loại ở Tầng 2
    "guest_account",      # Dài hơn 5 ký tự VÀ có chứa guest -> VƯỢT QUA!
    "test_user_vip"       # Dài hơn 5 ký tự VÀ có chứa test -> VƯỢT QUA!
]

print("-------bắt đầu lọc-------")

#for /if phải thụt vào cùng một mức code
for current_user in user_box :

       # ─── TẦNG 1: KIỂM TRA ĐỘ DÀI ───

    # Đo độ dài của tên người dùng hiện tại
    current_length=len(current_user)

    if current_length > 5 :

       # Tạo các biến logic
       current_has_test = "test" in current_user
       current_has_guest= "guest" in current_user

       # ─── TẦNG 2 (LỒNG BÊN TRONG): KIỂM TRA TỪ KHÓA ───
       if current_has_test or current_has_guest:
      # nếu lọc qua nó sẽ thực hiện lệnh ok
        current_status="ok"
        print(f"[{current_status}] : [{current_user}]")

print("---hoàn thành---------")