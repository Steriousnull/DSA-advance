caps = 1667

for i in range(0, 50):
    percent = 20 * caps / 100  # Percent of the current value of caps
    capsmain = caps + percent
    print(capsmain)
    caps = capsmain  # Update caps to the new value
