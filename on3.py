payload_box = [
    "short",              # Ngắn hơn 10 -> Bị loại ngay ở Tầng 1
    "execute_order_99",   # Dài hơn 10, nhưng không có admin/bypass -> Bị loại ở Tầng 2
    "admin_login_code",   # Dài hơn 10 VÀ có chứa admin -> VƯỢT QUA!
    "bypass_all_firewall" # Dài hơn 10 VÀ có chứa bypass -> VƯỢT QUA!
]

print("=========BẮT ĐẦU THÔI ==============")
for current_payload in payload_box:
    # đđo độ dài của payload hiện tại 
    current_length = len(current_payload)

 # ─── TẦNG 1: KIỂM TRA ĐỘ DÀI ───

    if current_length >10:

       current_has_admin = "admin" in current_payload 
       current_has_bypass = "bypass" in current_payload

 # ─── TẦNG 2 (LỒNG BÊN TRONG): KIỂM TRA TỪ KHÓA ───
       if current_has_admin or current_has_bypass:

           current_status = "ok"
           print(f"[{current_status}]:[{current_payload}]")

           print ("======== ok ============")