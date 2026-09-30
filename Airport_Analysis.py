from graphics import *
import csv

# --- Airports and AirLines Data ---
data_list = []   #  An empty list to load and hold data from csv file

VALID_AIRPORTS = {
    "LHR": "London Heathrow", "MAD": "Madrid Adolfo Suárez-Barajas",
    "CDG": "Charles De Gaulle International", "IST": "Istanbul Airport International",
    "AMS": "Amsterdam Schiphol", "LIS": "Lisbon Portela",
    "FRA": "Frankfurt Main", "FCO": "Rome Fiumicino",
    "MUC": "Munich International", "BCN": "Barcelona International"
}

VALID_AIRLINES = {
    "BA": "British Airways", "AF": "Air France", "AY": "Finnair",
    "KL": "KLM", "SK": "Scandinavian Airlines", "TP": "TAP Air Portugal",
    "TK": "Turkish Airlines", "W6": "Wizz Air", "U2": "easyJet",
    "FR": "Ryanair", "A3": "Aegean Airlines", "SN": "Brussels Airlines",
    "EK": "Emirates", "QR": "Qatar Airways", "IB": "Iberia", "LH": "Lufthansa"
}

def load_csv(CSV_chosen):
    """
    This function loads any csv file by name (set by the variable 'selected_data_file') into the list "data_list"
    YOU DO NOT NEED TO CHANGE THIS BLOCK OF CODE
    """
    global data_list
    data_list.clear() # Clearing list for Task E loop
    
    with open(CSV_chosen, 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            data_list.append(row)

# ************************************************************************************************************

# --- TASK A: INPUT VALIDATION ---
def get_user_inputs():
    "Task A: Validates City Code and Year input from the user."
    
    # 1. Validate City Code
    while True:
        city = input("Please enter a three-letter city code: ").strip().upper()
        if len(city) != 3:
            print("Wrong code length - please enter a three-letter city code")
        elif city not in VALID_AIRPORTS:
            print("Unavailable city code - please enter a valid city code")
        else:
            break

    # 2. Validate Year
    while True:
        year_str = input("Please enter the year required in the format YYYY: ").strip()
        if not year_str.isdigit() or len(year_str) != 4:
            print("Wrong data type - please enter a four-digit year value")
        else:
            year = int(year_str)
            if 2000 <= year <= 2025:
                break
            else:
                print("Out of range - please enter a value from 2000 to 2025")

    filename = f"{city}{year}.csv"
    airport_name = VALID_AIRPORTS[city]
    
    print("*" * 60)
    print(f"File {filename} selected - Planes departing {airport_name} {year}")
    print("*" * 60)
    
    return filename, airport_name, year

# --- TASK B: OUTCOMES & TASK C: SAVE RESULTS ---
def process_and_save(data_rows, filename, airport_name, year):
    """Calculates outcomes (Task B) and saves to file (Task C)."""
    
    # Initialize variables
    total_flights = 0
    term2_count = 0
    under_600 = 0
    af_flights = 0
    ba_flights = 0
    below_15 = 0
    af_delayed = 0
    rain_hours = []
    destinations = []

    # Loop to calculate stats
    for row in data_rows:
        total_flights += 1
        
        flight_num = row[1]
        sched_time = row[2]
        actual_time = row[3]
        dest = row[4]
        try: dist = int(row[5])
        except: dist = 0
        terminal = row[8]
        weather = row[10]

        # Task B Logic
        if terminal == "2": term2_count += 1
        if dist < 600: under_600 += 1
        
        if flight_num.startswith("AF"):
            af_flights += 1
            if sched_time != actual_time: af_delayed += 1
            
        if flight_num.startswith("BA"):
            ba_flights += 1
            
        temp_str = ''.join(filter(str.isdigit, weather))
        if temp_str and int(temp_str) < 15: below_15 += 1
            
        if "rain" in weather.lower():
            h = sched_time.split(":")[0]
            if h not in rain_hours: rain_hours.append(h)
            
        destinations.append(dest)

    # Calculations
    ba_avg = round(ba_flights / 12, 2)
    ba_pct = round((ba_flights/total_flights)*100, 2) if total_flights else 0
    af_delay_pct = round((af_delayed/af_flights)*100, 2) if af_flights else 0
    
    # Least Common Destination Logic
    counts = {}
    for d in destinations: counts[d] = counts.get(d, 0) + 1
    
    least_common = []
    if counts:
        min_val = min(counts.values())
        for code, count in counts.items():
            if count == min_val:
                least_common.append(VALID_AIRPORTS.get(code, code))

    # --- TASK B OUTPUT ---
    print(f"The total number of flights from this airport was {total_flights}")
    print(f"The total number of flights departing Terminal Two was {term2_count}")
    print(f"The total number of departures on flights under 600 miles was {under_600}")
    print(f"There were {af_flights} Air France flights from this airport")
    print(f"There were {below_15} flights departing in temperatures below 15 degrees")
    print(f"There was an average of {ba_avg} British Airways flights per hour from this airport")
    print(f"British Airways planes made up {ba_pct}% of all departures")
    print(f"{af_delay_pct}% of Air France departures were delayed")
    print(f"There were {len(rain_hours)} hours in which rain fell")
    print(f"The least common destinations are {least_common}")

    # --- TASK C: SAVE TO FILE ---
    try:
        with open("results.txt", "a") as f:
            f.write("*"*60 + "\n")
            f.write(f"File {filename} selected - {airport_name} {year}\n")
            f.write("*"*60 + "\n")
            f.write(f"Total flights: {total_flights}\n")
            f.write(f"Terminal 2 flights: {term2_count}\n")
            f.write(f"Flights under 600 miles: {under_600}\n")
            f.write(f"Air France flights: {af_flights}\n")
            f.write(f"Flights below 15 degrees: {below_15}\n")
            f.write(f"Avg BA flights per hour: {ba_avg}\n")
            f.write(f"BA percentage: {ba_pct}%\n")
            f.write(f"AF delayed percentage: {af_delay_pct}%\n")
            f.write(f"Rain hours: {len(rain_hours)}\n")
            f.write(f"Least common destinations: {least_common}\n\n")
    except:
        print("Error writing to results.txt")

# --- TASK D: HISTOGRAM ---
def draw_histogram(data_rows, airport, year):
    "Draws a horizontal histogram using graphics.py"
    
    # D1: Validate Airline
    while True:
        code = input("Enter a two-character Airline code to plot a histogram: ").strip().upper()
        if code in VALID_AIRLINES: break
        print("Unavailable Airline code please try again.")
    
    airline_name = VALID_AIRLINES[code]
    hourly_counts = [0] * 12
    
    for row in data_rows:
        if row[1].startswith(code):
            try:
                h = int(row[2].split(":")[0])
                if 0 <= h < 12: hourly_counts[h] += 1
            except: pass

    # Setup Graphics Window
    try:
        win = GraphWin("Histogram", 800, 600)
    except NameError:
        print("Error: graphics.py not found.")
        return

    win.setBackground("mint cream")
    
    # D2: Title
    Text(Point(400, 30), f"Departures by hour for {airline_name} from {airport} {year}").draw(win)
    # D3: Axis Labels
    Text(Point(40, 300), "Hours\n00:00\nto\n12:00").draw(win)
    
    max_count = max(hourly_counts)
    if max_count == 0: max_count = 1
    
    # D4 & D5: Draw Bars
    for i in range(12):
        count = hourly_counts[i]
        bar_len = (count / max_count) * 600
        
        # Horizontal Bar Coordinates
        x1 = 100
        y1 = 60 + (i * 40)
        x2 = 100 + bar_len
        y2 = 90 + (i * 40)
        
        bar = Rectangle(Point(x1, y1), Point(x2, y2))
        bar.setFill("pink")
        bar.draw(win)
        
        Text(Point(80, 75 + (i * 40)), f"{i:02d}").draw(win)
        if count > 0:
            Text(Point(x2 + 15, 75 + (i * 40)), str(count)).draw(win)
            
    try: win.getMouse(); win.close()
    except: pass

# --- TASK E: PROGRAM LOOP ---
def main():
    while True:
        # 1. Get Inputs
        filename, airport, year = get_user_inputs()
        
        # 2. Load CSV (Using Template Function)
        try:
            load_csv(filename)
        except FileNotFoundError:
            print("File not found in the folder. Please try again.")
            continue
            
        # Filter empty rows (Prevents IndexErrors)
        clean_data = [row for row in data_list if len(row) > 10]
        
        if not clean_data:
            print("File loaded but seems empty or invalid.")
        else:
            # 3. Process and Save
            process_and_save(clean_data, filename, airport, year)
            # 4. Draw Histogram
            draw_histogram(clean_data, airport, year)
        
        # 5. Loop Query
        if input("Do you want to select a new data file? Y/N: ").strip().upper() == "N":
            print("Thank you. End of run")
            break

if __name__ == "__main__":
    main()
