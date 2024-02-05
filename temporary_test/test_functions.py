import Timetable_Functions as Tf
import warnings
import numpy as np
import copy
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
    """
    Finding the initial solution for the problem
    Arguments:
        k: int
        ma_hps: dictionary that have keys as subject's ID and values as subject's classes
        _calendar: list that have weekdays from 2 to 8 and time from 0645 to 1800 (just use the default)
        _calendar_state: empty list to store calendar
        _initial_solution: empty list to store suitable classes
    Returns:
        Initial_solution: a list of suitable classes
    """
    key = list(ma_hps.keys())[k]  # Chọn mã học phần đã nhập (với k khác nhau thì là mã HP khác nhau)
    for maHP_items in ma_hps[key]:  # Với mỗi mã lớp của mã học phần đó
        if Check(dataframe, _calendar, maHP_items):
            # Kiểm tra xem lịch ở thời điểm đó có trống hay ko, trống thì true và điền vào lịch, đầy thì false
            _calendar_state.append(_calendar)  # Lưu lại lịch cũ để khi backtrack còn quay lại lịch cũ để tìm kqua mới
            _initial_solution.append(maHP_items)  # Biến chứa các mã lớp hợp lệ, dùng để return
            if k == len(list(ma_hps.keys()))-1:  # nếu k == số HP nhập thì ...
                if not _initial_solution:  # nếu lời giải rỗng => ...
                    print("There is no suitable timetable right now")
                else:  # nếu lời giải ko rỗng => ... (Cần phải exit chỗ này)
                    return _initial_solution
            else:  # nếu k != số HP nhập, tìm mã lớp HP tiếp theo
                result = Try(k + 1, dataframe, ma_hps, _calendar, _calendar_state, _initial_solution)
                if result:
                    return result
                _initial_solution.pop()  # Nếu duyệt hết mà ko thấy mã lớp do kín lịch, backtrack và xóa mã lớp đã điền
                _calendar_state.pop()  # Xóa lịch ko hợp lệ
                _calendar = copy.deepcopy(_calendar_state[-1])  # copy trạng thái cũ của lịch


def Check(dataframe, _calendar, class_id):
    """"
    Check if a class is suitable for the timetable
    Arguments:
        dataframe: filtered_data
        _calendar: list that have weekdays from 2 to 8 and time from 0645 to 1800 (just use the default)
        class_id: ID of classes. e.g: `151128`
    Returns:
        True if it is safe to fill in that class
        False if it is not
    """
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
