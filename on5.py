file_box=  ["cmd.exe", "safe_backup.txt", "hack_tool.exe","bypass_system.dat", "script_hack.py"]

# Tầng 1 (Vòng ngoài): Kiểm tra độ dài của tên file hiện tại phải lớn hơn 8 ký tự.

for current_file in file_box:
    current_length = len(current_file)

    if