import fastf1
import fastf1.plotting
from matplotlib import pyplot as plt

print("=" * 40)
print("     F1 Analysis Tool - Yosef KB")
print("=" * 40)

year         = int(input("Enter the year        : "))
track        = input("Enter the Grand Prix  : ")
session_type = input("Enter the session (FP1/FP2/FP3/Q/R) : ")
driver       = input("Enter the driver code : ")

session = fastf1.get_session(year, track, session_type)
session.load()

driver_info = session.get_driver(driver)

fastest_lap = session.laps.pick_driver(driver).pick_fastest()

weather = session.weather_data

print("\n" + "=" * 40)
print("          SESSION INFO")
print("=" * 40)
print(f"Track   : {session.event['EventName']}")
print(f"Date    : {session.date.strftime('%d %B %Y')}")
print(f"Session : {session.name}")

print("\n" + "=" * 40)
print("          DRIVER INFO")
print("=" * 40)
print(f"Full Name   : {driver_info['FullName']}")
print(f"Team        : {driver_info['TeamName']}")
print(f"Car Number  : {driver_info['DriverNumber']}")

print("\n" + "=" * 40)
print("          FASTEST LAP")
print("=" * 40)
print(f"Lap Number  : {fastest_lap['LapNumber']}")
print(f"Lap Time    : {fastest_lap['LapTime']}")
print(f"Sector 1    : {fastest_lap['Sector1Time']}")
print(f"Sector 2    : {fastest_lap['Sector2Time']}")
print(f"Sector 3    : {fastest_lap['Sector3Time']}")
print(f"Tyre        : {fastest_lap['Compound']}")
print(f"Tyre Life   : {fastest_lap['TyreLife']} laps")
print(f"Speed Trap  : {fastest_lap['SpeedST']} km/h")

print("\n" + "=" * 40)
print("          WEATHER (avg)")
print("=" * 40)
print(f"Air Temp    : {weather['AirTemp'].mean():.1f} °C")
print(f"Track Temp  : {weather['TrackTemp'].mean():.1f} °C")
print(f"Humidity    : {weather['Humidity'].mean():.1f} %")
print(f"Wind Speed  : {weather['WindSpeed'].mean():.1f} m/s")
print(f"Rainfall    : {'Yes' if weather['Rainfall'].any() else 'No'}")

print("\n" + "=" * 40)