#Import necessary modules
import os
import sys

# Define the function to convert time from 12-hour format to 24-hour format
def timeConversion(s):
    # Split the input time string into hours, minutes, and seconds
    time = s.split(":")

    # Check if the time is in PM
    if s[-2:] == "PM":
        # If it's not 12 PM, add 12 hours to the hour part
        if time[0] != "12":
            time[0] = str(int(time[0]) + 12)
    else:
        # If it's 12 AM, set the hour part to 00
        if time[0] == "12":
            time[0] = "00"

    # Join the modified time components back into a string
    ntime = ':'.join(time)
    
    # Remove the AM/PM part from the result, as it's now in 24-hour format
    return str(ntime[:-2])

# Main block to execute the code
if __name__ == '__main__':
    # Open a file for writing the output (this is specific to HackerRank environment)
    f = open(os.environ['OUTPUT_PATH'], 'w')

    # Take user input for the time in 12-hour format
    s = input()

    # Call the timeConversion function with the input and get the result
    result = timeConversion(s)

    # Write the result to the output file
    f.write(result + '\n')

    # Close the output file
    f.close()
