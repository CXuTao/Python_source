import calendar
"""
日历模块
"""

#使用
#返回指定某年某月的日历
print(calendar.month(2019,3))
#返回指定年的日历
print(calendar.calendar(2019))
#判断闰年返回Ture
print(calendar.isleap(2000))
#返回某个月的weekday的第一天和这个月的所有天数
print(calendar.monthrange(2019,3))
#返回某个月以每一周为元素的列表
print(calendar.monthcalendar(2019,3))