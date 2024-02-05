# importing
import numpy as np
import pandas as pd
import warnings
import tkinter as tk
from tkinter.filedialog import askopenfilename
root = tk.Tk()
root.withdraw()
filename = askopenfilename()
warnings.filterwarnings('ignore')  # Ignore warnings

# Data handling
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
# Group location together
df1["Phòng"] = df1["Phòng"].astype(str)
group_num = []


def grouping_location(_room):
    if any(substring in _room for substring in ["D3", "D5"]):
        return 0
    elif any(substring in _room for substring in ["D9"]):
        return 1
    elif any(substring in _room for substring in ["C3", "C4", "C5", "C6", "C7", "C8", "C10"]):
        return 2
    elif any(substring in _room for substring in ["C1", "C2", "C9"]):
        return 3
    elif any(substring in _room for substring in ["D4", "D6", "D8"]):
        return 4
    elif any(substring in _room for substring in ["B1", "B3", "B4", "B6", "B7", "B8", "B9", "B10", "B13"]):
        return 5
    elif any(substring in _room for substring in ["TC"]):
        return 6
    else:
        return 7


def new_grouping_location(_room):
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


for room in (df1["Phòng"].to_numpy().tolist()):
    group_num.append(new_grouping_location(room))

df1.insert(loc=11, column="Khu", value=group_num)
del df1["Phòng"]
# Dictionary of chosen classIDs
maHPs = {}
maHP = ""
# Need to move this to main.py
print("Hãy nhập vào mã học phần của môn học bạn định đăng ký, kết thúc bằng dấu *: ")
while maHP != "*":
    maHP = input()
    if maHP not in df1["Mã HP"].to_numpy().tolist():
        if maHP != "*":
            print(f"Không tồn tại mã học phần {maHP}")
        continue
    if maHP not in maHPs:
        dfx = df1[df1["Mã HP"] == maHP]
        dfx = dfx[dfx["Loại lớp"].isin(["BT", "LT+BT"])]
        filtered_classes_ID = dfx["Mã lớp"].to_numpy().tolist()
        # filtered_classes_ID = [int(class_id) for class_id in filtered_classes_ID]
        maHPs[maHP] = filtered_classes_ID
# Output will only have "BT" or "LT+BT" labeled classes
# TODO: Create new filters for classes labeled as "TN"
# Enter "*" to stop

# Distance matrix
Dist = np.array([[0, 5, 5, 10, 10, 5, 10],  # D3, D5, D3-5
                 [5, 0, 5, 10, 5, 10, 10],  # Library, D9, lake
                 [5, 5, 0, 10, 10, 10, 10],  # C6, C7, C8, C3, C4, C5, C10
                 [10, 10, 10, 0, 5, 10, 10],  # C1, C2, C9
                 [10, 5, 10, 5, 0, 10, 10],  # D4, D6, D8
                 [5, 10, 10, 10, 10, 0, 5],  # KTX, B1
                 [10, 10, 10, 10, 10, 5, 0]  # TC =)))
                ])
# Calculate initial solution
calendar = np.zeros((9, 3000))
initial_solution = []
# TODO Fix the `check` function so that if it backtracks, it reverts the `calendar` variable


def Check(class_id, _calendar):
    flag = 0
    row = df1["Mã lớp"] == str(class_id)
    date = int(df1.loc[row, "Thứ"])
    start = int(df1.loc[row, "Bắt đầu"])
    end = int(df1.loc[row, "Kết thúc"])
    for i in range(start, end+1):
        if _calendar[date][i] == 0:
            _calendar[date][i] = 1
            flag += 1
    if flag < end-start+1:
        return False
    return True


def Try(k, templist):
    global initial_solution
    initial_solution = []
    if k == len(maHPs):
        initial_solution = templist.copy()
        return
    key = list(maHPs.keys())[k]
    for maHP_loop in maHPs[key]:
        if Check(maHP_loop, calendar):
            templist.append(maHP_loop)
            Try(k+1, templist)
            if initial_solution:
                return initial_solution
            templist.pop()
# Output!!!


Try(0, [])
print("Initial Solution:", initial_solution)
