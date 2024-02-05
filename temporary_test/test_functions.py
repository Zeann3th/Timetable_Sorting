import Timetable_Functions as Tf
import warnings
import numpy as np
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


def Try(k: int, dataframe, ma_hps: dict, _calendar=np.zeros((9, 1801)), _calendar_state=[], _initial_solution=[]):
    key = list(ma_hps.keys())[k]
    for maHP_items in ma_hps[key]:
        if Check(dataframe, _calendar, maHP_items):
            _calendar_state.append(_calendar)
            _initial_solution.append(maHP_items)
            if k == len(list(ma_hps.keys()))-1:
                if not _initial_solution:
                    print("There is no suitable timetable right now")
                    return []
                else:
                    return _initial_solution
            else:
                Try(k + 1, dataframe, ma_hps, _calendar, _calendar_state, _initial_solution)
                _initial_solution.pop()
                _calendar_state.pop()
                _calendar = _calendar_state[-1]


def Check(dataframe, _calendar, class_id):
    row = dataframe[dataframe["Mã lớp"] == class_id]
    date = int(row["Thứ"].values[0])
    start = int(row["Bắt đầu"].values[0])
    end = int(row["Kết thúc"].values[0])
    for i in range(start, end + 1):
        if _calendar[date][i] == 1:
            return False
    for i in range(start, end+1):
        _calendar[date][i] = 1
    return True


solution = Try(0, filtered_data, maHPs)
print(solution)
