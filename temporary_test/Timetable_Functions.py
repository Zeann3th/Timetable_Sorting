import pandas as pd
import numpy as np
import copy


def Grouping_location(_room: str):
    """
    Grouping study locations into bigger areas
    Arguments:
        _room: a string. e.g: 'D3-301'
    Returns:
         The code for the area where the room is located
    """
    building = _room[:2] if _room[2] == "-" else _room[:3]
    if building in ["D3", "D5"]:
        return 0
    if building in ["D9", "D7"]:
        return 1
    if building in ["C3", "C4", "C5", "C6", "C7", "C8", "C10"]:
        return 2
    if building in ["C1", "C2", "C9"]:
        return 3
    if building in ["D4", "D6", "D8"]:
        return 4
    if building in ["B1", "B3", "B4", "B6", "B7", "B8", "B9", "B10", "B13"]:
        return 5
    if building in ["TC"]:
        return 6
    return 7


def Data_cleaning(filename: str):
    """
    Clean data from a dataframe
    Arguments:
        filename: a string contains the name of an Excel file ('.xlsx' tail)
    Returns:
        Unfiltered_data: full data of the table, without no cuts.
        Filtered_data: A shorter version of Unfiltered_data, contains necessary information for the algorithm to work.
    """
    cols = ["Kỳ", "Trường_Viện_Khoa", "Mã lớp", "Mã lớp kèm", "Mã HP", "Tên HP",
            "Tên HP Tiếng Anh", "Khối lượng", "Ghi chú", "Buổi số", "Thứ", "Thời gian",
            "Bắt đầu", "Kết thúc", "Kíp", "Tuần", "Phòng", "Cần thí nghiệm", "Số lượng đăng ký",
            "Số lượng max", "Trạng thái", "Loại lớp", "Đợt mở", "Mã quản lý"]
    df = pd.read_excel(filename, names=cols)
    df = df.iloc[2:]  # Delete title rows
    df.reset_index(inplace=True, drop=True)
    df.index += 1  # indexes start at 1
    # filter columns
    df1 = df[["Mã lớp", "Mã lớp kèm", "Mã HP", "Tên HP", "Khối lượng", "Buổi số", "Thứ", "Thời gian", "Tuần", "Phòng",
              "Cần thí nghiệm", "Số lượng max", "Trạng thái", "Loại lớp", "Đợt mở", "Mã quản lý"]]
    df1["Cần thí nghiệm"] = (df1["Cần thí nghiệm"] == "TN").astype(int)  # "TN" -> 1 and "NULL" -> 0
    df1 = df1[df1["Thứ"].notnull()]  # Eliminate classes with no date values
    # Manipulate time -> start_time, end_time
    start_time = []
    end_time = []
    for time in (df1["Thời gian"].to_numpy().tolist()):
        start_time.append(time[:4])
        end_time.append(time[5:])
    df1.insert(loc=7, column="Bắt đầu", value=start_time)
    df1.insert(loc=8, column="Kết thúc", value=end_time)
    del df1["Thời gian"]
    df1["Phòng"] = df1["Phòng"].astype(str)
    group_num = []
    for room in (df1["Phòng"].to_numpy().tolist()):
        group_num.append(Grouping_location(room))
    df1.insert(loc=11, column="Khu", value=group_num)
    del df1["Phòng"]
    return df, df1  # df, df1 = data_cleaning("TKB20231-FULL-1809.xlsx")


def Subject_filtering(dataframe):
    """
    Filter subjects into a dictionary
    Arguments:
      dataframe: a dataframe. To be precise, please use the Filtered_data.
    Returns:
       A dictionary contains the subject IDs as keys and their corresponding classes IDs as values
    """
    ma_hps = {}
    ma_hp = ""
    while ma_hp != "*":
        ma_hp = input("Nhập mã học phần của bạn: ")
        if ma_hp not in dataframe["Mã HP"].to_numpy().tolist():
            if ma_hp != "*":
                print(f"Không tồn tại mã học phần {ma_hp}")
            continue
        if ma_hp not in ma_hps:
            dfx = dataframe[dataframe["Mã HP"] == ma_hp]
            dfx = dfx[dfx["Loại lớp"].isin(["BT", "LT+BT"])]
            filtered_classes_id = dfx["Mã lớp"].to_numpy().tolist()
            ma_hps[ma_hp] = filtered_classes_id
    return ma_hps


def Check(dataframe, _calendar, class_id):
    """
    Check if a class is suitable for the timetable
    Arguments:
        dataframe: filtered_data
        _calendar: list that have weekdays from 2 to 8 and time from 0645 to 1800 (just use the default)
        class_id: ID of classes. e.g: `151128`
    Returns:
        True if it is safe to fill in that class
        False if it is not
    """
    row = dataframe[dataframe["Mã lớp"] == class_id]  # Tìm hàng có "Mã lớp" == mã lớp bài tập đang chọn
    # week = int(row["Tuần"].values[0])  #TODO: Cần phải format tuần
    date = int(row["Thứ"].values[0])  # Tìm thứ
    start = int(row["Bắt đầu"].values[0])  # Tìm giờ bắt đầu
    end = int(row["Kết thúc"].values[0])  # Tìm giờ kết thúc
    for i in range(start, end + 1):  # Nếu lướt qua mà có thấy có môn học ở thời gian này thì trả về False
        if _calendar[date][i] == 1:
            return False
    for i in range(start, end+1):  # Hơi cồng kềnh nma ko muốn điền vào vòng lặp trước đấy =))
        _calendar[date][i] = 1
    if int(row["Mã lớp kèm"].values[0]) != class_id:
        # Nếu mã lớp kèm != mã lớp (tránh phải duyệt hết, tuy nhiên vẫn vướng mấy lớp có tuần chẵn, tuần lẻ. e.g: SSH1131)
        row = dataframe[dataframe["Mã lớp"] == int(row["Mã lớp kèm"])]
        # week = int(row["Tuần"].values[0])  #TODO: Cần phải format tuần
        date = int(row["Thứ"].values[0])  # Tìm thứ
        start = int(row["Bắt đầu"].values[0])  # Tìm giờ bắt đầu
        end = int(row["Kết thúc"].values[0])  # Tìm giờ kết thúc
        for i in range(start, end + 1):  # Nếu lướt qua mà có thấy có môn học ở thời gian này thì trả về False
            if _calendar[date][i] == 1:
                return False
        for i in range(start, end + 1):  # Hơi cồng kềnh nma ko muốn điền vào vòng lặp trước đấy =))
            _calendar[date][i] = 1
    return True


def Generate_population(k: int, dataframe, ma_hps: dict, _calendar=np.zeros((9, 1801)), _calendar_state=[], _solution=[], _population=[], _population_num=20):
    """
    Finding the initial solution for the problem
    Arguments:
        k: int
        dataframe: filtered_data
        ma_hps: dictionary that have keys as subject's ID and values as subject's classes
        _calendar: list that have weekdays from 2 to 8 and time from 0645 to 1800 (just use the default)
        _calendar_state: empty list to store calendar
        _solution: empty list to store suitable classes
        _population: empty list to store solutions
        _population_num: number of solutions
    Returns:
        Initial_solution: a list of suitable classes
    """
    key = list(ma_hps.keys())[k]  # Chọn mã học phần đã nhập (với k khác nhau thì là mã HP khác nhau)
    for maHP_items in ma_hps[key]:  # Với mỗi mã lớp của mã học phần đó
        if Check(dataframe, _calendar, maHP_items):
            # Kiểm tra xem lịch ở thời điểm đó có trống hay ko, trống thì true và điền vào lịch, đầy thì false
            _calendar_state.append(_calendar)  # Lưu lại lịch cũ để khi backtrack còn quay lại lịch cũ để tìm kqua mới
            _solution.append(maHP_items)  # Biến chứa các mã lớp hợp lệ, dùng để return
            if k == len(list(ma_hps.keys()))-1:  # nếu k == số HP nhập thì ...
                if not _solution:  # nếu lời giải rỗng => ...
                    print("There is no suitable timetable right now")
                    return []
                else:  # nếu lời giải ko rỗng => ... (Cần phải exit chỗ này)
                    return _solution
            else:  # nếu k != số HP nhập, tìm mã lớp HP tiếp theo
                result = Generate_population(k + 1, dataframe, ma_hps, _calendar, _calendar_state, _solution)
                if result:
                    return result
                _solution.pop()  # Nếu duyệt hết mà ko thấy mã lớp do kín lịch, backtrack và xóa mã lớp đã điền
                _calendar_state.pop()  # Xóa lịch ko hợp lệ
                _calendar = _calendar_state[-1]
