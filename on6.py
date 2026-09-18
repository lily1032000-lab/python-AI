# vd để hiểu continue
num_box = [1, 2, 3, 4, 5]

print("--------- BẮT ĐẦU QUÈT KIỂM TRA PHẦN CỨNG ---------")

for current_num in num_box:
    print(f"\n[Vòng lặp] Xét số hiện tại: {current_num}")
    
    # TẦNG 1: Bộ lọc tìm RÁC. Ở đây, số 3 chính là RÁC!
    if current_num == 3:
        print("⚡ Phát hiện SỐ 3 là RÁC! Lệnh continue kích hoạt -> VỨT LẬP TỨC!")
        continue  # Máy tính quay xe ngay tại đây, nhảy lên bốc số 4!
        
    # TẦNG 2: ĐÂY CHÍNH LÀ CÔNG VIỆC NẶNG NỀ (Sẽ bị vứt bỏ nếu gặp continue)
    print(f"   [RAM] -> Đang nạp dữ liệu số {current_num} vào bộ nhớ...")
    print(f"   [CPU] -> Đang tốn sức xử lý thuật toán cho số {current_num}...")

print("\n--------- KIỂM TRA KẾT THÚC ---------")
