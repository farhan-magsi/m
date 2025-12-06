# --- Step 1: Take temperature input from user ---

temperatures = []  # empty list

print("Enter temperature for 7 days:\n")

for i in range(1, 8):
    temp = float(input(f"Day {i} temperature: "))
    temperatures.append(temp)

# --- Step 2: Functions ---

def get_stats(temp_list):
    highest = max(temp_list)
    lowest = min(temp_list)
    average = sum(temp_list) / len(temp_list)
    return highest, lowest, average

def categorize_temp(t):
    if t >= 33:
        return "Hot"
    elif t >= 28:
        return "Normal"
    else:
        return "Cold"

def weather_trend(temp_list):
    trend = []
    for i in range(1, len(temp_list)):
        if temp_list[i] > temp_list[i-1]:
            trend.append(("Day "+str(i+1), "Warmer"))
        elif temp_list[i] < temp_list[i-1]:
            trend.append(("Day "+str(i+1), "Colder"))
        else:
            trend.append(("Day "+str(i+1), "Same"))
    return trend


# --- Step 3: Processing ---

highest, lowest, average = get_stats(temperatures)
categories = {temp: categorize_temp(temp) for temp in temperatures}
sorted_temps = sorted(temperatures)
trend = weather_trend(temperatures)


# --- Step 4: Output ---

print("\n--- Weather Report ---")
print("Temperatures of 7 Days:", temperatures)
print("Highest Temperature:", highest)
print("Lowest Temperature:", lowest)
print("Average Temperature:", round(average, 2))

print("\nDay Categories (Hot / Normal / Cold):")
for t, c in categories.items():
    print(t, "=>", c)

print("\nSorted Temperatures:", sorted_temps)

print("\nWeather Trend:")
for day, condition in trend:
    print(day, "=>", condition)