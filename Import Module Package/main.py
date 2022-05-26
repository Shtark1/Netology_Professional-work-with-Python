from datetime import datetime
from application.people import number_of_people
from application.salary import number_salary




if __name__ == '__main__':
    now = datetime.now()
    number_of_people(99,0.00123)
    number_salary(1230,43)
    print(now)