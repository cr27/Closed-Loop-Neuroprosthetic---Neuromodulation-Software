import sqlite3


with open('arduino_data.txt', 'r') as file:
    lines = file.readlines()

# Initialize variables to store the extracted values
frequency = voltage = pulse_width = None

for line in lines:
    if 'Frequency (Hz):' in line:
        frequency = line.split(': ')[1].strip()
    elif 'Voltage (V):' in line:
        voltage = line.split(': ')[1].strip()
    elif 'Pulse Width (microseconds):' in line:
        pulse_width = line.split(': ')[1].strip()

    # When you encounter 'DATA:', insert the values into the database
    if 'DATA:' in line and frequency is not None and voltage is not None and pulse_width is not None:
        conn = sqlite3.connect('')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO bio_table (frequency, voltage, pulse_width) VALUES (?, ?, ?)",
                       (frequency, voltage, pulse_width))
        conn.commit()

# Close the database connection
conn.close()
