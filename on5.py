import time

cmd_box = ["run_cmd", "admin_power_bypass_1", "user_login", "check_system_hack", "force_stop"]

for current_cmd in cmd_box:
    current_length = len(current_cmd)

    if current_length % 2 == 1:
        current_has_hack = "hack" in current_cmd
        current_has_system = "system" in current_cmd

        if current_has_hack or current_has_system:
            start_time = time.perf_counter()
            current_status = "ok"
            print(f"{current_status} new : {current_cmd}")

            current_time = time.perf_counter() - start_time
            print(f"time {current_time:.6f}")      