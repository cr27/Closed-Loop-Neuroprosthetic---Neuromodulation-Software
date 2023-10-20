from Arduinotest import HopfieldNetwork
from Arduinotest import encoded_signal

import subprocess
details = []
# Run the .py file and capture its output
output = subprocess.check_output(['python', 'Arduinotest.py'], universal_newlines=True)

# Split the captured output into lines
lines = output.split('\n')

# Loop through the lines and find the one containing "1111002.510"
desired_output = None
for line in lines:
    if "T" in line or "F" in line:
        desired_output = line
        details.append(desired_output)
# loop through all db rows, put float at front of string
# Print the captured output or store it in a variable
if desired_output is not None:
    print("Captured output:", desired_output)
else:
    print("Pattern not found in the output.")

print(details)

class somethingsomething:
    def blah_output(self):
        # Initialize variables
        neural_stimulation_output = ""  # 0 excitate depolarize, A excitate, B inhibition, C do nothing
        ff = ""
        ans = 0
        neural_stimulation_identity = [0, 0, 0]
        visited =[]
        ret = []
        #add unique identifiers to visited to signal the end of encoding
        for f in details:  # create SQLite database to create array data for details, catch each encoded string using desired_output
            for c in f:
                if "~" in c:
                    visited.append("~")
                if "|" in c:
                    visited.append("|")
                if "," in c:
                    visited.append(",")
                if "/" in c:
                    visited.append("/")

                if "~" not in visited: # if condition while symbol is not present
                    ff += c
                    ans = ff
                    if ans == '-1-1-1':
                        print("has not converged to a stored pattern")
                        ff = ""
                    if ans == '111':
                        print("successfully converged to a stored pattern or a stable state")
                        ff = ""

                if "~" in visited:
                    if "|" not in visited and c != "~":
                        ff += c
                        ans = ff
                    if "|" in visited and "1" not in visited:
                        ans = float(ff)
                        print("Frequency is: ", ans)
                        if 50 < ans < 150:
                            print("Depolarization-Based Excitation")
                            neural_stimulation_identity[0] = 0

                        if 10 < ans < 50:
                            print("Non-Depolarization Excitation")
                            neural_stimulation_identity[0] = 'A'

                        if 0.5 < ans < 20:
                            print("Inhibition")
                            neural_stimulation_identity[0] = 'B'

                        ff = ""
                        visited.append("1")

                if "|" in visited:
                    if "," not in visited and c != "|":
                        ff += c
                        ans = ff
                    if "," in visited and "2" not in visited:
                        ans = float(ff)
                        print('Voltage is:', ans)

                        if 2 < ans < 5:
                            print("Depolarization-Based Excitation")
                            neural_stimulation_identity[1] = 0

                        if 1 < ans < 2:
                            print("Non-Depolarization Excitation")
                            neural_stimulation_identity[1] = 'A'

                        if 0.5 < ans < 1:
                            print("Inhibition")
                            neural_stimulation_identity[1] = 'B'

                        ff = ""
                        visited.append("2")

                if "," in visited:
                    if "/" not in visited and c != ",":
                        ff += c
                        ans = ff
                    if "/" in visited and "3" not in visited:
                        ans = int(ff)
                        print('Pulse Width is:', ans)
                        if 50 < ans < 300:
                            print("Depolarization-Based Excitation")
                            neural_stimulation_identity[2] = 0


                        if ans == 100:
                            print("Non-Depolarization Excitation")
                            neural_stimulation_identity[2] = 'A'


                        if ans < 100:
                            print("Inhibition")
                            neural_stimulation_identity[2] = 'B'
                        ff = ""
                        visited.append("3")

            if neural_stimulation_identity == [0, 0, 0]:
                print(" ")
                print('Elicit Depolarization-Based Excitation')
                neural_stimulation_output = "0"
                visited = []

            if neural_stimulation_identity == ['A', 'A', 'A']:
                print(" ")
                print('Elicit Non Depolarized Excitation')
                neural_stimulation_output  = "A"
                visited = []
                ret.append(neural_stimulation_output)

            if neural_stimulation_identity == ['B', 'B', 'B']:
                print(" ")
                print('Elicit Inhibition')
                neural_stimulation_output  = "B"
                visited = []
                ret.append(neural_stimulation_output)

            else:
                neural_stimulation_output  = "C"
                visited = []
                ret.append(neural_stimulation_output)
        return ret

# printsomething = somethingsomething()
# response = printsomething.blah_output()
# print(response)



