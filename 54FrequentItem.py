from collections import Counter

text = "In order to better manage many different business calendars, hue-scheduler should store the business unit and the calendarId, etc. " \
       "Every time, when other hue products want to create calendar or event, they will always include (business_code, subsystem) insides their record. "
words = text.split()
counter = Counter(words)
top_three = counter.most_common(3)
print(top_three)