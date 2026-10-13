# ============================================================
# EMPLOYEE ATTENDANCE & PERFORMANCE SYSTEM
# ============================================================

# ------------------------------------------------------------
# INITIAL DATA
# ------------------------------------------------------------

employees = {
    "E101": {
        "name": "Rahul",
        "department": "IT",
        "attendance": [22, 20, 21, 23],
        "rating": 4
    },

    "E102": {
        "name": "Priya",
        "department": "HR",
        "attendance": [24, 23, 22, 24],
        "rating": 5
    },

    "E103": {
        "name": "Amit",
        "department": "IT",
        "attendance": [18, 20, 19, 21],
        "rating": 3
    },

    "E104": {
        "name": "Sneha",
        "department": "Finance",
        "attendance": [23, 22, 24, 23],
        "rating": 4
    }
}


# ============================================================
# 1. DISPLAY EMPLOYEE DETAILS
# ============================================================

def display_all_employees():

    print("\n========== ALL EMPLOYEES ==========")

    for employee_id, employee in employees.items():

        print("\nEmployee ID :", employee_id)
        print("Name        :", employee["name"])
        print("Department  :", employee["department"])
        print("Attendance  :", employee["attendance"])
        print("Rating      :", employee["rating"])


# ============================================================
# 2. CALCULATE TOTAL ATTENDANCE
# ============================================================

def calculate_total_attendance():

    print("\n========== TOTAL ATTENDANCE ==========")

    for employee_id, employee in employees.items():

        total = sum(employee["attendance"])

        print(employee["name"], ":", total)


# ============================================================
# 3. CALCULATE AVERAGE ATTENDANCE
# ============================================================

def calculate_average_attendance():

    print("\n========== AVERAGE ATTENDANCE ==========")

    for employee_id, employee in employees.items():

        total = sum(employee["attendance"])

        average = total / len(employee["attendance"])

        print(employee["name"], ":", round(average, 2))


# ============================================================
# 4. FIND BEST EMPLOYEE
# ============================================================

def find_best_employee():

    best_id = None

    for employee_id, employee in employees.items():

        if best_id is None:

            best_id = employee_id

        else:

            current_rating = employee["rating"]
            best_rating = employees[best_id]["rating"]

            # First compare rating
            if current_rating > best_rating:

                best_id = employee_id

            # If rating is same, compare average attendance
            elif current_rating == best_rating:

                current_average = (
                    sum(employee["attendance"])
                    / len(employee["attendance"])
                )

                best_average = (
                    sum(employees[best_id]["attendance"])
                    / len(employees[best_id]["attendance"])
                )

                if current_average > best_average:

                    best_id = employee_id

    print("\n========== BEST EMPLOYEE ==========")
    print("Employee ID :", best_id)
    print("Name        :", employees[best_id]["name"])
    print("Rating      :", employees[best_id]["rating"])

    average = (
        sum(employees[best_id]["attendance"])
        / len(employees[best_id]["attendance"])
    )

    print("Average Attendance :", round(average, 2))


# ============================================================
# 5. IDENTIFY EMPLOYEES AT RISK
# ============================================================

def show_at_risk_employees():

    print("\n========== EMPLOYEES AT RISK ==========")

    found = False

    for employee_id, employee in employees.items():

        average = (
            sum(employee["attendance"])
            / len(employee["attendance"])
        )

        rating = employee["rating"]

        # At risk if:
        # Average attendance < 20
        # OR rating <= 2

        if average < 20 or rating <= 2:

            print(
                employee_id,
                "-",
                employee["name"],
                "| Average Attendance:",
                round(average, 2),
                "| Rating:",
                rating
            )

            found = True

    if found == False:

        print("No employees are at risk.")


# ============================================================
# 6. DEPARTMENT-WISE EMPLOYEE COUNT
# ============================================================

def department_employee_count():

    department_count = {}

    for employee_id, employee in employees.items():

        department = employee["department"]

        if department in department_count:

            department_count[department] += 1

        else:

            department_count[department] = 1

    print("\n========== DEPARTMENT EMPLOYEE COUNT ==========")

    for department, count in department_count.items():

        print(department, ":", count, "employees")

    return department_count


# ============================================================
# 7. DEPARTMENT-WISE AVERAGE ATTENDANCE
# ============================================================

def department_average_attendance():

    department_data = {}

    for employee_id, employee in employees.items():

        department = employee["department"]

        attendance_total = sum(employee["attendance"])

        attendance_count = len(employee["attendance"])

        if department not in department_data:

            department_data[department] = {
                "total_attendance": 0,
                "total_months": 0
            }

        department_data[department]["total_attendance"] += attendance_total

        department_data[department]["total_months"] += attendance_count

    print("\n========== DEPARTMENT AVERAGE ATTENDANCE ==========")

    for department, data in department_data.items():

        average = (
            data["total_attendance"]
            / data["total_months"]
        )

        print(department, ":", round(average, 2))


# ============================================================
# 8. PERFORMANCE CATEGORIES
# ============================================================

def get_performance_category(rating):

    if rating == 5:

        return "Outstanding"

    elif rating == 4:

        return "Excellent"

    elif rating == 3:

        return "Good"

    elif rating == 2:

        return "Needs Improvement"

    elif rating == 1:

        return "Poor"

    else:

        return "Invalid Rating"


def show_performance_categories():

    print("\n========== PERFORMANCE CATEGORIES ==========")

    for employee_id, employee in employees.items():

        rating = employee["rating"]

        category = get_performance_category(rating)

        print(
            employee["name"],
            "| Rating:",
            rating,
            "| Category:",
            category
        )


# ============================================================
# 9. ADD A NEW EMPLOYEE
# ============================================================

def add_employee():

    print("\n========== ADD NEW EMPLOYEE ==========")

    employee_id = input("Enter Employee ID: ")

    # Check duplicate ID

    if employee_id in employees:

        print("Employee ID already exists.")

        return

    name = input("Enter Employee Name: ")

    department = input("Enter Department: ")

    attendance = []

    print("\nEnter attendance for 4 months:")

    for month in range(1, 5):

        value = int(
            input(
                "Enter attendance for month "
                + str(month)
                + ": "
            )
        )

        attendance.append(value)

    rating = int(input("Enter Rating (1-5): "))

    # Validate rating

    if rating < 1 or rating > 5:

        print("Invalid rating. Rating must be between 1 and 5.")

        return

    # Add employee

    employees[employee_id] = {
        "name": name,
        "department": department,
        "attendance": attendance,
        "rating": rating
    }

    print("\nEmployee added successfully.")


# ============================================================
# 10. UPDATE ATTENDANCE
# ============================================================

def update_attendance():

    print("\n========== UPDATE ATTENDANCE ==========")

    employee_id = input("Enter Employee ID: ")

    if employee_id not in employees:

        print("Employee not found.")

        return

    month = int(input("Enter month number (1-4): "))

    if month < 1 or month > 4:

        print("Invalid month number.")

        return

    new_attendance = int(
        input("Enter new attendance value: ")
    )

    # Convert month number to list index
    index = month - 1

    employees[employee_id]["attendance"][index] = new_attendance

    print("Attendance updated successfully.")

    print(
        "Updated Attendance:",
        employees[employee_id]["attendance"]
    )


# ============================================================
# 11. SEARCH EMPLOYEE
# ============================================================

def search_employee():

    print("\n========== SEARCH EMPLOYEE ==========")

    employee_id = input("Enter Employee ID: ")

    if employee_id in employees:

        employee = employees[employee_id]

        print("\nEmployee Found!")

        print("Employee ID :", employee_id)
        print("Name        :", employee["name"])
        print("Department  :", employee["department"])
        print("Attendance  :", employee["attendance"])
        print("Rating      :", employee["rating"])

        average = (
            sum(employee["attendance"])
            / len(employee["attendance"])
        )

        print("Average Attendance :", round(average, 2))

        print(
            "Performance Category :",
            get_performance_category(employee["rating"])
        )

    else:

        print("Employee not found.")


# ============================================================
# 12. GENERATE FINAL REPORT
# ============================================================

def generate_final_report():

    print("\n")
    print("========== EMPLOYEE REPORT ==========")

    # --------------------------------------------------------
    # Total Employees
    # --------------------------------------------------------

    total_employees = len(employees)

    print("Total Employees :", total_employees)

    # --------------------------------------------------------
    # Total Departments
    # --------------------------------------------------------

    departments = set()

    for employee_id, employee in employees.items():

        departments.add(employee["department"])

    total_departments = len(departments)

    print("Total Departments :", total_departments)

    # --------------------------------------------------------
    # Highest Performer
    # --------------------------------------------------------

    best_id = None

    for employee_id, employee in employees.items():

        if best_id is None:

            best_id = employee_id

        else:

            current_rating = employee["rating"]
            best_rating = employees[best_id]["rating"]

            if current_rating > best_rating:

                best_id = employee_id

            elif current_rating == best_rating:

                current_average = (
                    sum(employee["attendance"])
                    / len(employee["attendance"])
                )

                best_average = (
                    sum(employees[best_id]["attendance"])
                    / len(employees[best_id]["attendance"])
                )

                if current_average > best_average:

                    best_id = employee_id

    print(
        "Highest Performer :",
        employees[best_id]["name"]
    )

    # --------------------------------------------------------
    # Lowest Attendance Employee
    # --------------------------------------------------------

    lowest_id = None
    lowest_average = None

    for employee_id, employee in employees.items():

        average = (
            sum(employee["attendance"])
            / len(employee["attendance"])
        )

        if lowest_average is None or average < lowest_average:

            lowest_average = average
            lowest_id = employee_id

    print(
        "Lowest Attendance :",
        employees[lowest_id]["name"]
    )

    # --------------------------------------------------------
    # At-Risk Employees
    # --------------------------------------------------------

    at_risk = []

    for employee_id, employee in employees.items():

        average = (
            sum(employee["attendance"])
            / len(employee["attendance"])
        )

        rating = employee["rating"]

        if average < 20 or rating <= 2:

            at_risk.append(employee["name"])

    print(
        "Employees At Risk :",
        ", ".join(at_risk)
    )

    # --------------------------------------------------------
    # Department Summary
    # --------------------------------------------------------

    department_count = {}

    for employee_id, employee in employees.items():

        department = employee["department"]

        if department in department_count:

            department_count[department] += 1

        else:

            department_count[department] = 1

    print("\nDepartment Summary:")

    for department, count in department_count.items():

        print(
            department,
            ":",
            count,
            "employees"
        )


# ============================================================
# BONUS — DEPARTMENT STATISTICS
# ============================================================

def department_statistics():

    print("\n========== DEPARTMENT STATISTICS ==========")

    department_employee_count()

    department_average_attendance()


# ============================================================
# MENU-DRIVEN PROGRAM
# ============================================================

while True:

    print("\n")
    print("==============================================")
    print(" EMPLOYEE ATTENDANCE & PERFORMANCE SYSTEM")
    print("==============================================")

    print("1. Display All Employees")
    print("2. Search Employee")
    print("3. Add Employee")
    print("4. Update Attendance")
    print("5. Show Performance Categories")
    print("6. Show At-Risk Employees")
    print("7. Department Statistics")
    print("8. Generate Final Report")
    print("9. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        display_all_employees()

    elif choice == "2":

        search_employee()

    elif choice == "3":

        add_employee()

    elif choice == "4":

        update_attendance()

    elif choice == "5":

        show_performance_categories()

    elif choice == "6":

        show_at_risk_employees()

    elif choice == "7":

        department_statistics()

    elif choice == "8":

        generate_final_report()

    elif choice == "9":

        print("\nThank you for using the system.")

        break

    else:

        print("\nInvalid choice. Please enter 1-9.")