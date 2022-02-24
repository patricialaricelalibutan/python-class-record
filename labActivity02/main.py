# use at least three (3) built-in data structures (List, Tuple, and Dictionary)
# used mixed container to store the given dataset
data_mixed = [
    ("20180001", "Joed", "Goh ", {"Quiz 1": float(90), "Quiz 2": float(88), "Quiz 3": float(100)}),
    ("20180002", "Clark", "Kent", {"Quiz 1": float(87), "Quiz 2": float(69)}),
    ("20180003", "Bruce", "Wayne", {"Quiz 1": float(67), "Quiz 2": float(67), "Quiz 3": float(68)}),
    ("20180004", "Peter", "Parker", {"Quiz 1": float(85), "Quiz 2": float(95), "Quiz 3": float(91), "Quiz 4": float(70)}),
    ("20180005", "Diana", "Prince", {"Quiz 1": float(65)})
]

# used dictionary to store the program options
options_dict = {
    1: "Display Record Summary",
    2: "Access Individual Student",
    3: "Passing Students",
    4: "Failing Students",
    0: "Quit"
}


# create user-defined function to organize codes into smaller code blocks
def average(a, b):  # compute for the average, require two (2) arguments
    avg = (a / b)  # divide the two (2) arguments
    return format(avg, '.2f')  # format '.2f' used to limit the float decimals to two (2)


def append_avg():  # add average key: value in the dictionary in the mixed container
    i = 0  # instantiate a value for the index
    while i < len(data_mixed):  # perform while index is within the length of the mixed container
        # apply tuple unpacking. declared a variable and assigned values to two (2) arguments
        # one (1) is the sum of the values in the dictionary in the mixed container
        # two (2) length of the dictionary in the mixed container
        data_args = (float(sum(data_mixed[i][3].values())), float(len(data_mixed[i][3])))
        # add another key-value pair to store the average grade in the dictionary in the mixed container
        # assign key of "Average" to the value of the average grade
        # computed by passing data_args variable to the average() function
        data_mixed[i][3]["Average"] = float(average(*data_args))
        i += 1  # increase index value by 1


def print_header():  # print header of dataset table
    print("ID" + "\t\t\tFirstname" + "\tLastname" + "\tGrade")


def display_one():  # display record summary
    print("AI_ML(section-1) Class Record Summary\n")
    print_header()
    # print id, firstname, lastname, and computed average grade of each student
    for student in data_mixed:
        print(student[0] + "\t" + student[1] + "\t\t" + student[2] + "\t\t" + str(student[3]["Average"]))


def display_two():  # access individual student
    studentId = input("\nStudent ID: ")  # user input an id
    # used comprehension to check if inputted id exists and store their records in the "record" list
    record = [record for record in data_mixed if record[0] == studentId]
    # if yes, display individual student records
    for record in record:
        print("Lastname: " + record[1] + "\nFirstname: " + record[2] + "\n")
        for key, value in record[3].items():
            if "Quiz" in key:
                print("\t" + key + " : " + str(value))
        print("\nAverage Grade: " + str(record[3]["Average"]))
    # else, display error message
    if studentId not in record:
        print("Please enter a valid ID.")


def display_three():  # display passing students
    print("AI_ML(section-1) List of PASSING Students\n")
    print_header()
    # used comprehension to check for students with averages greater than or equal to 70 and add them to "passed" list
    passed = [student for student in data_mixed if student[3]["Average"] >= 70]
    # print id, firstname, lastname, and computed average grade of each student in the "passed" list
    for student in passed:
        print(student[0] + "\t" + student[1] + "\t\t" + student[2] + "\t\t" + str(student[3]["Average"]))


def display_four():  # display failing students
    print("AI_ML(section-1) List of FAILING Students\n")
    print_header()
    # used comprehension to check for students with averages less than 70 and add them to "failed" list
    failed = [student for student in data_mixed if student[3]["Average"] < 70]
    # print id, firstname, lastname, and computed average grade of each student in the "failed" list
    for student in failed:
        print(student[0] + "\t" + student[1] + "\t\t" + student[2] + "\t\t" + str(student[3]["Average"]))


def quit_program():  # quit program
    print("Program Terminated...")
    exit()  # exit the program


def program():
    while True:  # execute loop while True
        # print program options stored in the options dictionary
        print("\nChoose from the following:")
        # from every key and value in the options dictionary
        for key, value in options_dict.items():
            print("[" + str(key) + "] - " + value)
        choice = input("\nChoice: ")  # user input choice of program option
        if choice == str(1):  # if, user choice is 1
            display_one()  # then, call display_one() function
        elif choice == str(2):  # else if, user choice is 2
            display_two()  # then, call display_two() function
        elif choice == str(3):  # else if, user choice is 3
            display_three()  # then, call display_three() function
        elif choice == str(4):  # else if, user choice is 4
            display_four()  # then, call display_four() function
        elif choice == str(0):  # else if, user choice is 0
            quit_program()  # then, call quit_program() function
        else:  # else, when option does not exist
            print("Please enter a valid choice.")  # print error message


# first, add average in the data set
append_avg()
# second, run the program
program()
