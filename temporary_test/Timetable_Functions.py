import numpy as np
import pandas as pd


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
    maHPs = {}
    maHP = ""
    while maHP != "*":
        maHP = input()
        if maHP not in dataframe["Mã HP"].to_numpy().tolist():
            if maHP != "*":
                print(f"Không tồn tại mã học phần {maHP}")
            continue
        if maHP not in maHPs:
            dfx = dataframe[dataframe["Mã HP"] == maHP]
            dfx = dfx[dfx["Loại lớp"].isin(["BT", "LT+BT"])]
            filtered_classes_ID = dfx["Mã lớp"].to_numpy().tolist()
            maHPs[maHP] = filtered_classes_ID
    return maHPs


def Check(dataframe, class_id, calendar):
    flag = 0
    row = dataframe["Mã lớp"] == str(class_id)
    date = int(dataframe.loc[row, "Thứ"])
    start = int(dataframe.loc[row, "Bắt đầu"])
    end = int(dataframe.loc[row, "Kết thúc"])
    for i in range(start, end + 1):
        if calendar[date][i] == 0:
            calendar[date][i] = 1
            flag += 1
    if flag < end - start + 1:
        return False
    return True


def Try(dataframe, maHPs, calendar, k, templist):
    initial_solution = []
    if k == len(maHPs):
        initial_solution = templist.copy()
        return
    key = list(maHPs.keys())[k]
    for maHP_items in maHPs[key]:
        if Check(dataframe, maHP_items, calendar):
            templist.append(maHP_items)
            Try(dataframe, maHPs, calendar, k + 1, templist)
            if initial_solution:
                return initial_solution
            templist.pop()
