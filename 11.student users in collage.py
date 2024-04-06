def calculate_student_users(total_users, staff_users):
    if total_users <= 0:
        print("Invalid input. Total users should be a positive number.")
        return None
    elif staff_users > total_users:
        print("Invalid input. Staff users should not exceed total users.")
        return None
    non_teaching_staff = staff_users // 3
    student_users = total_users - staff_users - non_teaching_staff
    return student_users
test_cases = [
    (0, 0),
    (-143, 0),
    (1026, 1026),
    (450, 540),
    (600, 450)
]
for total_users, staff_users in test_cases:
    print("Total Users:", total_users)
    print("Staff Users:", staff_users)
    student_users = calculate_student_users(total_users, staff_users)
    if student_users is not None:
        print("Student Users:", student_users)
    print()
