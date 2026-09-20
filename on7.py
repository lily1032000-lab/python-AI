# dùng lower() chứ hoa -> chữ thường
cmd_box = ["init_run", "AdMiN_LoGiN", "stop_cmd", "SysTeM_HaCk"]

for current_cmd in cmd_box:
    cleand_cmd=current_cmd.lower()

    current_has_hack="hack" in cleand_cmd
    current_has_admin="admin" in cleand_cmd
    if not (current_has_hack or current_has_admin):
        continue

    print(f"{cleand_cmd}")