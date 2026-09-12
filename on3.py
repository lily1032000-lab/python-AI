payload_box = [
    "short_cmd",                        # Câu này ngắn, loại!
        "this_is_a_very_long_payload_text", # Câu này dài nhưng không có chữ "bypass", loại!
        "execute_order_99_and_bypass_now"  # SIÊU VŨ KHÍ: Thỏa mãn cả 2 điều kiện!
    ]
print ("--------- ĐÁM MÂY MỚI --------")

for current_payload in payload_box:
    payload_length = len(current_payload)

    if payload_length > 15 and not "bypass" in current_payload:
        print(f"vũ khí hợp lệ [{current_payload}]")

print(" -------- QUÉT THÀNH CÔNG----------")