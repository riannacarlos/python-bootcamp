mission = "Orbiter Alpha"
distance_km = 1500000.4567
days = 92.5
speed = distance_km / (days * 24)
completion = 0.35123

text= ' Mission Log '
print(f"{text:=^25}")
print(f"Mission: {mission}")
print(f"Distance: {distance_km:,.1f} km")
print(f"Duration: {days:.2f} days")
print(f"Speed: {speed:.2f} km/h")
print(f"Completion: {completion:.3%}")

# TODO: Follow the given format:
"""
    ====== Mission Log ======
    Orbiter Alpha ===========
    Distance: 1,500,000.5 km
    Duration: 92.50 days
    Speed: 675.68 km/h
    Completion: 35.123%
    =========================
"""
