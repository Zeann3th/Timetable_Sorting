import pandas as pd
import numpy as np
import copy
from random import choices, randint
from typing import Tuple
desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 15)


def Group_location(_room: str) -> int:
    """
    Group study locations into bigger areas.

    Args:
        _room (str): A Room in school. e.g: 'D3-301'.

    Returns:
         int: The code area where the room is located.
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


def Sort_Session(_session: int, _time: str) -> int:
    """
    Sort sessions. e.g: 1 (morning) -> 1; 1 (afternoon) -> 7; PE classes have time periods so 15:30-16:30 -> 10-11.

    Args:
        _session (int): The original session
        _time (str): To check if it is past 1230 or not.

    Returns:
        int: The modified session.
    """
    time_to_session = {
        range(645, 731): 1,
        range(730, 816): 2,
        range(825, 911): 3,
        range(920, 1006): 4,
        range(1015, 1101): 5,
        range(1100, 1146): 6,
        range(1230, 1316): 7,
        range(1315, 1401): 8,
        range(1410, 1456): 9,
        range(1505, 1551): 10,
        range(1600, 1646): 11,
        range(1645, 1731): 12,
        range(1745, 1831): 13,
        range(1830, 1916): 14
    }

    if _session in range(1, 7):
        _session = (_session + 6) if int(_time) > 1230 else _session
    else:
        for time_range, session_number in time_to_session.items():
            if _session in time_range:
                _session = session_number
                break

    return _session


def Clean_data(filename: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Filter, process data from a dataframe.

    Args:
        filename (str): A string contains the name of an Excel file ('.xlsx' tail).

    Returns:
        (pd.DataFrame, pd.DataFrame): Unfiltered_data and Filtered_data
    """
    # Unfiltered_data
    cols = ["Kỳ", "Trường_Viện_Khoa", "Mã lớp", "Mã lớp kèm", "Mã HP", "Tên HP",
            "Tên HP Tiếng Anh", "Khối lượng", "Ghi chú", "Buổi số", "Thứ", "Thời gian",
            "Bắt đầu", "Kết thúc", "Kíp", "Tuần", "Phòng", "Cần thí nghiệm", "Số lượng đăng ký",
            "Số lượng max", "Trạng thái", "Loại lớp", "Đợt mở", "Mã quản lý"]
    df = pd.read_excel(filename, names=cols)
    df = df.iloc[2:]  # Delete title rows
    df.reset_index(inplace=True, drop=True)
    df.index += 1
    # Filtered_data
    df1 = df[["Mã lớp", "Mã lớp kèm", "Mã HP", "Tên HP", "Khối lượng", "Buổi số",
              "Thứ", "Thời gian", "Bắt đầu", "Kết thúc", "Tuần", "Phòng", "Cần thí nghiệm",
              "Số lượng max", "Trạng thái", "Loại lớp", "Đợt mở", "Mã quản lý"]]
    df1["Cần thí nghiệm"] = (df1["Cần thí nghiệm"] == "TN").astype(int)  # "TN" -> 1 and "NULL" -> 0
    df1 = df1[df1["Thứ"].notnull()]  # Eliminate classes with no date values
    df1["Bắt đầu"] = df1.apply(lambda row: Sort_Session(row["Bắt đầu"], row["Thời gian"][:4]), axis=1)
    df1["Kết thúc"] = df1.apply(lambda row: Sort_Session(row["Kết thúc"], row["Thời gian"][5:]), axis=1)
    del df1["Thời gian"]  # Delete after separation
    df1["Phòng"] = df1["Phòng"].astype(str)
    group_num = []
    for room in (df1["Phòng"].to_numpy().tolist()):
        group_num.append(Group_location(room))
    df1.insert(loc=11, column="Khu", value=group_num)
    del df1["Phòng"]
    return df, df1  # df, df1 = Data_cleaning("TKB20231-FULL-1809.xlsx")


def Filter_subject(dataframe: pd.DataFrame) -> dict:
    """
    Filter subjects into a dictionary.

    Args:
      dataframe (pd.DataFrame): Filtered_data.

    Returns:
       dict: A dictionary contains the subject IDs as keys and their corresponding classes IDs as values.
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


def Check(dataframe: pd.DataFrame, _calendar: np.ndarray, class_id: int) -> bool:
    """
    Check if a class is suitable for the timetable.

    Args:
        dataframe (pd.DataFrame): Filtered_data.
        _calendar (np.ndarray): Numpy array that have weekdays from 2 to 8 and time from 0645 to 1800.
        class_id (int): ID of classes. e.g: `151128`.

    Returns:
        bool: True if it is safe to fill in that class, False if it is not.
    """

    def Check_time_slot(_date: int, _start: int, _end: int) -> bool:
        """
        Check if that slot in calendar is safe/empty to fill in a subject.

        Args:
            _date (int): Weekdays from Mon to Sun (2-8).
            _start (int): The start time.
            _end (int): The end time.

        Returns:
            bool: True if it is empty/safe, False if it is occupied.
        """
        for i in range(_start, _end + 1):  # Nếu lướt qua mà có thấy có môn học ở thời gian này thì trả về False
            if _calendar[_date][i] == 1:
                return False
        for i in range(_start, _end + 1):  # Hơi cồng kềnh nma ko muốn điền vào vòng lặp trước đấy =))
            _calendar[_date][i] = 1
        return True
    # Kiểm tra lịch cho lớp `BT`/ `LT+BT`
    row = dataframe[dataframe["Mã lớp"] == class_id]  # Tìm hàng có "Mã lớp" == mã lớp bài tập đang chọn
    # week = int(row["Tuần"].values[0])  #TODO: Cần phải format tuần
    date = int(row["Thứ"].values[0])  # Tìm thứ
    start = int(row["Bắt đầu"].values[0])  # Tìm giờ bắt đầu
    end = int(row["Kết thúc"].values[0])  # Tìm giờ kết thúc
    if not Check_time_slot(date, start, end):
        return False
    # Kiểm tra lịch cho lớp `LT+BT` nếu nó có 2 buổi học
    if len(row["Thứ"].values) > 1:
        date = int(row["Thứ"].values[1])  # Tìm thứ
        start = int(row["Bắt đầu"].values[1])  # Tìm giờ bắt đầu
        end = int(row["Kết thúc"].values[1])  # Tìm giờ kết thúc
        if not Check_time_slot(date, start, end):
            return False
    # Kiểm tra lịch cho lớp `LT` đi kèm với lớp `BT` đã chọn
    if int(row["Mã lớp kèm"].values[0]) != class_id:
        row = dataframe[dataframe["Mã lớp"] == int(row["Mã lớp kèm"])]
        # week = int(row["Tuần"].values[0])  #TODO: Cần phải format tuần
        date = int(row["Thứ"].values[0])  # Tìm thứ
        start = int(row["Bắt đầu"].values[0])  # Tìm giờ bắt đầu
        end = int(row["Kết thúc"].values[0])  # Tìm giờ kết thúc
        if not Check_time_slot(date, start, end):
            return False

    return True


def Generate_population(k: int, dataframe, ma_hps: dict, _calendar=np.zeros((9, 15)), _calendar_state: list = [],
                        _solution: list = [], _population: list = [], _population_num: int = 10) -> list:
    """
    Finding the first generation for the problem.

    Args:
        k (int): The index of subjects.
        dataframe (pd.DataFrame): Filtered_data.
        ma_hps (dict): Dictionary that have keys as subject's ID and values as subject's classes.
        _calendar (np.ndarray): Numpy array that have weekdays from 2 to 8 and time from 0645 to 1800.
        _calendar_state (list): Empty list to store calendars.
        _solution (list): Empty list to store suitable classes.
        _population (list): Empty list to store solutions.
        _population_num (int): Number of solutions.

    Returns:
        list: a list of solutions.
    """
    key = list(ma_hps.keys())[k]  # Chọn mã học phần đã nhập (với k khác nhau thì là mã HP khác nhau)
    for maHP_items in ma_hps[key]:  # Với mỗi mã lớp của mã học phần đó
        if Check(dataframe, _calendar, maHP_items):
            # Kiểm tra xem lịch ở thời điểm đó có trống hay ko, trống thì true và điền vào lịch, đầy thì false
            _calendar_state.append(copy.deepcopy(_calendar))
            # Lưu lại lịch cũ để khi backtrack còn quay lại lịch cũ để tìm kqua mới
            _solution.append(maHP_items)  # Biến chứa các mã lớp hợp lệ, dùng để return
            if k == len(list(ma_hps.keys()))-1:  # nếu k == số HP nhập thì ...
                if not _solution:  # nếu lời giải rỗng => ...
                    print("There is no suitable timetable right now")
                    return []
                else:  # nếu lời giải ko rỗng => ... (Cần phải exit chỗ này)
                    if len(_population) < _population_num:
                        _population.append(copy.deepcopy(_solution))
                        _solution.pop()
                        _calendar_state.pop()
                        _calendar = _calendar_state[-1]
                    elif len(_population) == _population_num:
                        return _population
            else:  # nếu k != số HP nhập, tìm mã lớp HP tiếp theo
                Generate_population(k + 1, dataframe, ma_hps, _calendar, _calendar_state, _solution)
                _solution.pop()  # Nếu duyệt hết mà ko thấy mã lớp do kín lịch, backtrack và xóa mã lớp đã điền
                _calendar_state.pop()  # Xóa lịch ko hợp lệ
                if len(_calendar_state) != 0:
                    _calendar = _calendar_state[-1]
    return _population


def fitness(_solution: list) -> int:
    """
    Evaluate points to find the optimal solution.

    Args:
        _solution: The solution needed to evaluate.

    Returns:
        int: The point of the given solution, if it is high, it is likely to be the optimal solution.
    """
    return 0
# TODO: Cần phải nghĩ ra tiêu chí để xét điểm


def Selection_pair(population: list, fitness_func) -> list:
    """
    Choose 2 random solution from population.

    Args:
        population:
        fitness_func:

    Returns:

    """
    return choices(
        population=population,
        weights=[fitness_func(genome) for genome in population],
        k=2
    )
# TODO: Cần phải hoàn thiện hàm Selection_pair()


def Single_point_crossover(a: list, b: list) -> Tuple[list, list]:
    """
    Generate offsprings from given parents.

    Args:
        a (list): first parent.
        b (list): second parent.

    Returns:
        (list, list): 2 Offsprings
    """
    length = len(a)
    if length < 2:
        return a, b
    p = randint(1, length-1)
    return a[0:p] + b[p:], b[0:p] + a[p:]

# TODO: Cần phải làm hàm Mutation()


def Run_evolution(_population: list) -> list:
    """
    Runs the algorithm.

    Args:
        _population (list): Empty list to store solutions.

    Returns:

    """
    for i in range(50):
        _population = sorted(
            _population,
            key=lambda genome: fitness(genome),
            reverse=True
        )
        next_generation = _population[0:2]
        for j in range(int(len(_population) / 2) - 1):
            parents = Selection_pair(_population, fitness)
            offsprings = Single_point_crossover(parents[0], parents[1])
            next_generation += offsprings
        _population = next_generation
    _population = sorted(
        _population,
        key=lambda genome: fitness(genome),
        reverse=True
    )
    return _population
# TODO: Cần phải hoàn thiện hàm Run_evolution()
