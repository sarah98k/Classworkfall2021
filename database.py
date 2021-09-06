#print("This is the database.py module")
#print("It's name is {}".format(__name__))


#import blood_calculator
import blood_calculator as bc
#from blood_calculator import hdl_analysis
#from blood_calculator import *
#from other_code import *
#from matplotlib import *

answer = hdl_analysis(55)
print("The analysis of 55 HDL is {}".format(answer))

answer2 = blood_calculator.ldl_analysis(200)

make_plot(3)