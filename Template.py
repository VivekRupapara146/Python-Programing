from datetime import datetime
from datetime import date

date1 = str(date.today)
date2 = date.today

letter = '''Dear, |Name|,
You are selected!,
|Date|'''

# letter.replace("|NAME|",input("Enter your name: "))
# letter.replace('|DATE|', str(date2))

# use above format and also impor date frome datetime package using variable

letter.replace("|Name|", "Vivek").replace("|Date|", "20-06-25")

print(letter)