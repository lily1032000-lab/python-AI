# dùng continue tiết kiệm và tốn ram
log_box = ["short", "admin_bypass_now", "execute_order_99"]

for current_log in log_box:
    current_length=len(current_log)

    if current_length <=10:
        continue

    if "bypass" in current_log:
        vaild_log= current_log
        print(f"[ok] {vaild_log}")
