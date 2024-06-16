from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)
    


def find_employee_by_name():
    name = input("Please enter name of employee: ")
    employee = Employee.find_by_name(name)
    print(name) if employee else print(f"Employee {name} doesn't exist")
    


def find_employee_by_id():
    id_ = input("Please enter in employee id: ")
    employee = Employee.find_by_id(id_)
    print(employee) if employee else print(f"id: {id_} is invalid.")
    


def create_employee():
    name = input("Please enter employee name: ")
    job_title = input("Please enter employee job title: ")
    department_id = int(input("Please enter id: "))
    try:
        employee = Employee.create(name, job_title, department_id)
        print(f"Employee {name} has been created!")
    except Exception as exc:
        print("Employee creation error ", exc)



    pass


def update_employee():
    id_ = input("Please enter employee id: ")
    if employee := Employee.find_by_id(id_):
        try:
            name = input("Please enter correct name: ")
            employee.name = name
            job_title = input("Please enter correct job_title: ")
            employee.job_title = job_title
            employee.update()
            print("Update successful!")
        except Exception as exc:
            print("Error, update unsuccessful ", exc)
    else:
        print(f"Employee id: {id_} not found")
        
    pass


def delete_employee():
    id_ = input("Please enter employee id")
    if employee:= Employee.find_by_id(id_):
        employee.delete()
        print("Deletion was successful.")
    else:
        print(f"Employee id:{id_} was invalid.")
    


def list_department_employees():
    dep_id = input("Please enter department id: ")
    departments = Department.find_by_id(dep_id)
    if department := departments:
        employees = department.employees()
        for employee in employees:
            print(employee)
    else:
        print(f"The Department id: {dep_id} was not valid.")