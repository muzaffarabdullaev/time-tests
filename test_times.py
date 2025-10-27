# To run pytest, 'pytest ./test_times.py'

from times import time_range, compute_overlap_time
import datetime

# Homework test
def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected
   
   
# two time ranges that do not overlap
def test_non_overlap():
    time1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    time2 = time_range("2010-01-12 13:00:00", "2010-01-12 14:00:00")
    result = compute_overlap_time(time1, time2)
    expected = "No overlap found."
    assert result == expected

# two time ranges that both contain several intervals each
# NOT WORKING!
def several_intervals_per_time():
    time1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 3, 0)
    time2 = time_range("2010-01-12 11:00:00", "2010-01-12 13:00:00", 3, 0)
    result = compute_overlap_time(time1, time2)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]


