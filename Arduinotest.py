import numpy as np

class HopfieldNetwork:
    def __init__(self, pattern_size):
        self.pattern_size = pattern_size
        self.weights = {}

    def train(self, patterns):
        for pattern in patterns:
            for i in range(self.pattern_size):
                for j in range(self.pattern_size):
                    if i != j:
                        if (i, j) not in self.weights:
                            self.weights[(i, j)] = 0
                        self.weights[(i, j)] += pattern[i] * pattern[j]

    def sign(self, value):
        return 1 if value >= 0 else -1

    def retrieve(self, input_pattern, max_iterations=10):
        current_pattern = input_pattern[:]  # Initialize with the input pattern
        for _ in range(max_iterations):
            new_pattern = current_pattern[:]  # Create a copy of the current pattern
            for i in range(self.pattern_size):
                activation = 0
                for j in range(self.pattern_size):
                    if i != j:
                        activation += self.weights.get((i, j), 0) * current_pattern[j]
                new_pattern[i] = self.sign(activation)
            if np.array_equal(new_pattern, current_pattern):
                return new_pattern  # If the pattern stabilizes, return it
            current_pattern = new_pattern  # Update the current pattern

        return current_pattern

# Define patterns to be stored in the associative memory
patterns = [
    [333333.34, 4.238, 3],  # Pattern 1: Frequency, Voltage, Pulse Width
    [142857, 1.026, 7],   # Pattern 2: Frequency, Voltage, Pulse Width
    [142857, 0.919, 7],    # Pattern 3: Frequency, Voltage, Pulse Width
    [142857,0.938,7] # Pattern 4: Frequency, Voltage, Pulse Width
]

# Create a Hopfield network with a pattern size of 3
hopfield_net = HopfieldNetwork(pattern_size=3)

# Train the network with the patterns
hopfield_net.train(patterns)

# Define a list of test patterns
import sqlite3

# Connect to the database
conn = sqlite3.connect('C:/Users/jbrow/OneDrive/Desktop/current study/arduinovoltfreqpulsedb.db')
cursor = conn.cursor()

# Retrieve a pattern from the database (replace 'pattern_id' with the actual ID of the pattern you want)
cursor.execute('SELECT frequency, voltage, pulse_width FROM bio_table')
all_patterns = cursor.fetchall()
conn.close()


for test_pattern_tuple in all_patterns:
    test_pattern = list(test_pattern_tuple)  # Convert the tuple to a list
    retrieved_pattern = hopfield_net.retrieve(test_pattern)


# Turn list into a string
hopfield_ans = ''
for i in retrieved_pattern:
    hopfield_ans = hopfield_ans + '' + str(i)
hopfield_ans += "~"
expected_patterns = [
    [333333.34, 4.238, 3],  # Pattern 1: Frequency, Voltage, Pulse Width
    [142857, 1.026, 7],  # Pattern 2: Frequency, Voltage, Pulse Width
    [142857, 0.919, 7],  # Pattern 3: Frequency, Voltage, Pulse Width
    [142857, 0.938, 7]  # Pattern 4: Frequency, Voltage, Pulse Width
]


class encoded_signal:
    def print_info_AMN(self, iterate_test_pattern):
        global hopfield_ans
        ans = ''
        for i in range(len(iterate_test_pattern)):
            ans += str(iterate_test_pattern[i])
            if i == 0:
                ans += '|'
            elif i == 1:
                ans += ','
            elif i == 2:
                ans += '/'

        if any(np.array_equal(iterate_test_pattern, pattern) for pattern in expected_patterns):
            print(f"Pattern found in memory: {ans}")
            f = hopfield_ans + ans + 'T'
            print(f)
        else:
            print(f"Pattern not found in memory: {ans}")
            f = hopfield_ans + ans + 'F'
            print(f)


encoded_signal = encoded_signal()

for test_pattern_tuple in all_patterns:
    test_pattern = list(test_pattern_tuple)  # Convert the tuple to a list
    retrieved_pattern = hopfield_net.retrieve(test_pattern)
    encoded_signal.print_info_AMN(iterate_test_pattern=test_pattern)




