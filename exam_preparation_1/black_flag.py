def black_flag(days, daily_plunder, expected_plunder):
    total_plunder = 0

    for day in range(1, days + 1):
        total_plunder += daily_plunder

        if day % 3 == 0:
            total_plunder += 0.5 * daily_plunder

        if day % 5 == 0:
            total_plunder -= 0.3 * total_plunder

    if total_plunder >= expected_plunder:
        print(f"Ahoy! {total_plunder:.2f} plunder gained.")
    else:
        diff_percentage = (total_plunder / expected_plunder) * 100
        print(f"Collected only {diff_percentage:.2f}% of the plunder.")


days_ = int(input())
daily_plunder_ = int(input())
expected_plunder_ = float(input())

black_flag(days_, daily_plunder_, expected_plunder_)