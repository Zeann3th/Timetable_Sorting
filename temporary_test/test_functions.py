import Timetable_Functions as Tf
import warnings
from tkinter.filedialog import askopenfilename
warnings.filterwarnings("ignore")


filename = askopenfilename()
unfiltered_data, filtered_data = Tf.Data_cleaning(filename)
# Function works!!!, uncomment to test it
# print(unfiltered_data)
# print(filtered_data)

maHPs = Tf.Subject_filtering(filtered_data)
# Function works!!!, uncomment to test it
# print(maHPs)

solution = Tf.Generate_population(0, filtered_data, maHPs)
print(solution)
