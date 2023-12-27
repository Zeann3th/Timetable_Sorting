from icalendar import Calendar, Event
from TimeTable_Query import TimeTable as Tt
import datetime as dt

cal = Calendar()


def export_to_ics(solution: list):
    year = int(Tt.df["Kỳ"].iloc[0][:4])
    for class_id in solution:
        event = Event()
        event.add("summary", Tt.df.loc[Tt.df["Mã lớp"] == class_id, "Tên HP"].to_string(index=False))
        start_hms = Tt.df1.loc[Tt.df1["Mã lớp"] == class_id, "Bắt đầu"].to_string(index=False)
        start_hour = int(start_hms[:2])
        start_min = int(start_hms[2:])
        end_hms = Tt.df1.loc[Tt.df1["Mã lớp"] == class_id, "Kết thúc"].to_string(index=False)
        end_hour = int(end_hms[:2])
        end_min = int(end_hms[2:])
        event.add("dtstart", dt.datetime(year, 1, 1, start_hour, start_min, 0))
        event.add("dtend", dt.datetime(year, 1, 1, end_hour, end_min, 0))
        event.add("location", Tt.df.loc[Tt.df["Mã lớp"] == class_id, "Phòng"].to_string(index=False))
        event.add("rrule", {"freq": "weekly", "count": 10})
        cal.add_component(event)


export_to_ics(Tt.initial_solution)
with open("google_calendar.ics", "w", encoding="utf-8") as f:
    f.write(cal.to_ical().decode("utf-8"))
