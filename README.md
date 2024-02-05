# Timetable_Sorting
Sorting timetables using Genetic Algorithms

## Purposes
This project is our attempt to help students (at Hanoi University of
Science and Technology) find the best optimized timetable(s) for their next semester.

## Features
- Reading and processing the list of available classes downloaded 
from the university's official website (see the Excel file in the Examples folder), then show the optimal solution(s).
- Export the timetable to an iCalendar file (.ics) for calendar apps like
Google Calendar, Outlook or Apple Calendar.

## Installation
### <em>System requirements (important!)</em>

As the GUI are written in [Qt6](https://doc.qt.io/qt-6/supported-platforms.html), so newest version of your OS is recommended

| OS      | Version                   | Notes                  |
|---------|---------------------------|------------------------|
| Windows | 10 (build 1809) or higher |                        |
| macOS   | macOS Big Sur or higher   | Build from source only |
| Ubuntu  | 22.04 or higher           |                        |


### From source code (only solution until now, testing only)
1. Clone this repository
```
git clone https://github.com/Zeann3th/Timetable_Sorting.git
cd TimeTable_Sorting
```

2. Create virtual environment (recommended)
```
python -m venv venv
```

3. Install required libraries
```
./venv/Scripts/activate
pip install -r requirements.txt
```

4. Run `main.py`

```
python main.py
```

### From executable files (coming soon)
Check the releases tags for executable files, if available

## Disclaimer
We can't be 100% sure about the optimization, because there are too many factors to
consider. At this moment, the program may return the result in which:
- The location for adjacent classes are not too far away
- Only one optimal solution are shown, which is not the best outcome for the app

## What will we do next
- Bind the GUI components with the core functions
- Complete the timetable preview (like schedules on calendar apps)
- New algorithms for better and more flexible optimization (details unknown)

If you have any problems, please go to the `Issues` tab or contact us via e-mail address
