payload_box = [
    "short_cmd",                                # Ngắn -> Loại!
    "execute_order_99_and_bypass_now",          # Dài trên 15 chữ VÀ KHÔNG chứa chữ shutdown -> HỢP LỆ!
    "dangerous_command_to_shutdown_the_system"
]
print ("--------- hệ thống nâng cấp độ khó ----------")

for current_payload in payload_box:
    payload_length = len(current_payload)

    if payload_length > 15 and not ("shutdown" in current_payload):
        print (f" vũ khí tốt bắn :[{current_payload}]")

print("------------ quét xong---------------") 