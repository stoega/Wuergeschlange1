def grade_calculator(assignments: list, bonus_assignment: int, exam: int):
    passed = True
    grade = 0

    if bonus_assignment is None:
        bonus_assignment = 0
    if exam is None:
        exam = 0

    assignment_failed = 0
    sum_points = bonus_assignment
    for assignment in assignments:
        if assignment is None:
            assignment = 0
        sum_points += assignment

        # point A
        if assignment < 25:
            assignment_failed += 1

        if assignment_failed > 2 and bonus_assignment < 25:
            passed = False
            break

    # point B
    if sum_points < 500:
        passed = False
    
    # point C
    if exam < 50 and passed:
        passed = False

    if not passed:
        return(passed, 5)

    grade_percent = (sum_points + exam) / 1100.0 * 100
    if grade_percent < 50:
        passed = False
        grade = 5
    elif grade_percent < 62.5:
        grade = 4
    elif grade_percent < 75:
        grade = 3
    elif grade_percent < 87.5:
        grade = 2
    else:
        grade = 1

    return (passed, grade)

# print(grade_calculator([95,100,39,13,86,71,20,100,83,100], None, 82))
# print(grade_calculator([95,100,39,13,86,71,20,100,83,100], 51, 82))
# print(grade_calculator([0,100,100,13,100,100,20,100,100,100], 0, 100))
# print(grade_calculator([0,100,100,13,100,100,20,100,100,100], 100, 100))
# print(grade_calculator([0,100,100,13,100,100,None,100,100,100], 100, 100))
# print(grade_calculator([100,100,100,100,100,100,100,100,100,100], 100, 49))