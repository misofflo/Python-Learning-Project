import pandas
import numpy

#variables
test_df = pandas.DataFrame(
    {"Column1": [1, 2, 3], "Column2": ["A", "B", "C"]}
)

#functions
def pow(int_base, int_exponent):
    return int_base ** int_exponent

#exectution
print(pow(2, 3))