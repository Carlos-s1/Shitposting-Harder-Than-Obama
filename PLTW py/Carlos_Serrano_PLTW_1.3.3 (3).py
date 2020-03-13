from __future__ import print_function # use Python 3.0 printing

def report_grade(grade):
    '''Step 6a if-else example'''
    GRADE_LIMIT = 80    # convention: use CAPS for constants
    if grade < GRADE_LIMIT:
      print (grade, '''A grade of 79 does not indicate mastery.
Seek extra practice or help.''')
    else:
      print(grade, '''A grade of 85 percent indicates mastery.
Keep up the good work!''')
    print(' Minimum grade is ', GRADE_LIMIT)