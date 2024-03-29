from src import timetable_functions as tf
import warnings
from tkinter.filedialog import askopenfilename
warnings.filterwarnings("ignore")


filename = askopenfilename()
unfiltered_data, filtered_data = tf.Clean_data(filename)
# # Function works!!!, uncomment to test it
# # print(unfiltered_data)
# print(filtered_data)

maHPs = tf.Filter_subject(filtered_data)
# # Function works!!!, uncomment to test it
# # print(maHPs)

population = tf.Generate_population(0, filtered_data, maHPs)
print(population)
