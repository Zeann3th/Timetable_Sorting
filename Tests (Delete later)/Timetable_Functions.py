import numpy as np
import pandas as pd


def grouping_location(_room):
    """
    Grouping study locations into bigger areas
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


def data_cleaning(filename: str):
    """
    Input Excel files and return unfiltered dataframe and filtered dataframe
    correct syntax: df, df1 = data_cleaning(**filename**)
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
        group_num.append(grouping_location(room))
    df1.insert(loc=11, column="Khu", value=group_num)
    del df1["Phòng"]
    return df, df1  # df, df1 = data_cleaning("TKB20231-FULL-1809.xlsx")


def subject_filtering(dataframe):
    # Output will only have "BT" or "LT+BT" labeled classes
    # TODO: Create new filters for classes labeled as "TN" or "LT"
    # Enter "*" to stop
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
