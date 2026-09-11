    payload_length = len(current_payload)
    
    # =====================================================================
    # NÚT THẮT LOGIC CHIẾN THUẬT: SỬ DỤNG TỪ KHÓA 'and'
    # =====================================================================
    # Máy tính bắt buộc phải thỏa mãn 2 điều kiện: Dài trên 15 chữ VÀ phải chứa từ "bypass"
    if payload_length > 15 and "bypass" in current_payload:
        
        # Cấp độ 2: Con của IF -> BẮT BUỘC lùi vào 2 lần Tab
        print(f"[+] VŨ KHÍ HỢP LỆ: [{current_payload}]")
        print(f"    -> Đo đạc: Thỏa mãn {payload_length} ký tự và chứa từ khóa bí mật.")

print("---------- VÒNG QUÈT KẾT THÚC ----------")
