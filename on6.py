# continue+ break
cmd_box = ["short", "force_bypass_run", "user_login_warn", "admin_power_bypass", "core_hack_safe"]

vaild_count=0
for current_cmd in cmd_box:

    current_length = len(current_cmd)
    if current_length <=5:
        continue

    current_has_bypass = "bypass" in current_cmd
    if not current_has_bypass:
        continue
    print(f"{current_cmd} length :{current_length}")
    vaild_count=vaild_count+1

    if vaild_count == 3:
        break