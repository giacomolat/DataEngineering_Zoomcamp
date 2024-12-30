import sys
import pandas as pd 

# sys.argv allow to pass arguments to the script from the commandline
print(sys.argv)

# sys.argv[0] > name of the file
# sys.argv[1] > first argument passed
day = sys.argv[1]

# Here is the Pandas code

# print("Pandas installation was successful! Yeah!")
print(f"job finished successfully for the day = {day}")