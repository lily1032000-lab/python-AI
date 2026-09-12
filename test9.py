payload_box = [
    "short_cmd",                        # Câu này ngắn, loại!
    "this_is_a_very_long_payload_text", # Câu này dài nhưng không có chữ "bypass", loại!
    "execute_order_99_and_bypass_now"  # SIÊU VŨ KHÍ: Thỏa mãn cả 2 điều kiện!
]

print("------ ĐÁM MÂY KHỞI ĐỘNG ------")

for current_payload in payload_box:
    payload_length = len(current_payload)

    # Dùng and để gộp hai điều kiện kiểm tra.

    if payload_length > 15 or "bypass" in current_payload:
        print(f"Vũ khí hợp lệ: [{current_payload}]")

print("-> đã quét xong.")