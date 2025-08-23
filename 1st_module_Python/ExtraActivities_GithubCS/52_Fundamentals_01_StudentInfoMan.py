#Create a student information system

#Required features:
# 1. Add student - store name, age, and courses
# 2. View all students - display details for every student
# 3. Search student - find a student by name (case-sensitive)
# 4. Show statistics - display total students, unique courses 
# and counts per course
# 5. Exit - end program after user confirmation

#Framework:
# store each student as 'dictionary' with name, age and courses

# store all students in a 'list'
# keep a 'set' of all unique courses in the academy (no duplicates)
# there should be 5 menu options, requiring user input:
    # 1. add student
        # ask for full name - format with .title()                              OK
        # ask for age - validate with .isdigit() and 15-20                      OK
        # ask for course - list available+ input course name names (,), check typos/duplicates  OK
        # input correct = split into a tuple                                    ???
        # store data in student dictionary                                      OK
        # append copy of student dictionary to the all-student-list             OK
    # 2. view all students
        # for-loop through each student's details (name, age, courses)          OK
        # no student exists yet > input(No students added yet. Do you           OK
        # wish to add one now? (yes/no))                                        OK
            # if no, return to menu                                             OK
            # if yes, start(add student)                                        OK
    # 3. search student
        # ask full name (lowercase comparison), if found 'details'              OK
        # otherwise display 'not found', type 'enter' to go to menu             OK
    # 4. show statistics
        # print no. of students (len(list))
        # print set of unique courses
        # nested loop: print how many students are in each course
        # print courses with highest occupancy
        # print courses with lowest occupancy
        # print courses without student
        # type 'enter' to return to menu
    # 5. exit
        # 'Are you sure you want to exit? (yes/no)'                         OK
            # if yes, end program                                           OK
            # if no, return to menu; other inputs are 'no'                  OK

# - include error message/failsafes

global functions_active;
global input_name;
global age_is_ok;
global new_student
new_student= {};     #when adding student save data to this variable-dict first, then copy into list of all
global all_students
all_students = [];    #student list
all_students = ['Ben', 15, ['Python', 'AI'], 'John', 16, ['AI', 'Java'], 'Elise', 19, ['Java']] ### TESTING ONLY!!!

functions_active = "yes"                #fuse/unfuse actual function use (main menu)

def main_menu():
        if functions_active == "yes":
             
             ### MAIN MENU ###
             print("Variable functions active: ", functions_active)
             print("")
             print("### main menu ###")
             print("1. Add student")
             print("2. View all students")
             print("3. Search student")
             print("4. Show statistics")
             print("5. Exit")
             print("")
             print("please choose a menu option: ", input)
             input_value=input()     #assigns input to string
             input_value = int(input_value)  #cast to integer, for use in case statement below
             #print(type(input_value))

             ### main menu program structure ###
             input_value      #manual variable set to test below
             match input_value:
                 case 1:
                     #1. Add student
                     f01add_student()
                 case 2:
                     #2. View all students
                     f02view_students()
                     #print("2. View all students")
                 case 3:
                     ###3. Search student
                     #print("3. Search student")
                     f03search_student()
                 case 4:
                     #4. Show statistics
                     #print("4. Show statistics")
                     f04show_statistics()
                 case 5:
                     #5. Exit confirmation menu
                     input5_value=input("Are you sure you want to exit? (yes/no)")
                     print("Input5: ", input5_value)
                     print(type(input5_value))
                     if "yes" or "YES" or "y" or "Y" in input5_value: exit() #exit program
                     
                     ###############################
                     ####### CONTINUE HERE #########
                     ###############################
                     
                     elif  "yes" or  "YES" or  "y" or  "Y" not in input5_value: main_menu() #return to main menu
                     else: print("Error in inputs - check code for y/Y/yes/YES detection.")
                 case _:
                     print("Invalid input, please enter no. between 1 and 5")


def f01add_student():
     print("1. Add student")
     #ask for full name:
     global input_name
     input_name = input("Enter full name '>=3 chars': ").title()        #capitalize word beginning each name
     if len(input_name) < 3:
          print("Too short a name, please enter 3 letters or more")
          f01add_student()
     #ask for age:
     f01enter_age()
     #ask for courses, print available courses:
     f01enter_courses()
     global new_student
     new_student = {"name": input_name, "age": input_age, "courses":entry_courses}
     print("Student will be saved to database: ", new_student)
     confirmation = input("If your data is correct, please type 'y' and press 'enter' to confirm! Otherwise restart from main menu. ")
     #input("my text", test)
     if confirmation == "y":
          f01_save_new_student()     #save to all-students-list
     else:
          main_menu()
     
     print("")
     main_menu()    #return to main menu


def f01enter_age():
      #global input_age
      input_age2 = input("Enter the age (between 15-20): ") #if input().isdigit() else print("Age must be number!")
      if int(input_age2.isdigit()) == "False": 
         print("Entered age is wrong, no. number!")
         f01enter_age()   #call this function again, creating a loop until a number is given
      #global input_age
      input_age2 = int(input_age2)    #cast to int for numeric comparison below
      
      #check if age range is within allowed range:
      if input_age2 <14 or input_age2 >21: f01enter_age()
      
      #Set a flag for positive result of checked age input (optional for later use):
      global input_age
      input_age = input_age2

      age_is_ok = True


def f01enter_courses():
     available_courses = {"Computer Science", "Python", "Java", "AI", "Painting", "CAD"}
     print("Please type in courses which are available: ", list(available_courses))
     #available are courses from school, input are entered courses,  entry are identified courses from available ones
     global input_courses
     global entry_courses
     entry_courses = []
     input_courses = []
     
     input_courses = input("Enter your courses, separated by ',': ")
     list(input_courses)
     for item in available_courses:
               if item in input_courses:
                entry_courses.append(item)


def f01_save_new_student():
     global all_students
     global new_student
     #print(all_students)
     #if all_students == []: 
     #new_student_value = new_student.values
     #print(list(new_student_value))
     all_students.append(new_student["name"])
     all_students.append(new_student["age"])
     all_students.append(new_student["courses"])
     print("Student saved to database")  #make space
     #print("New student dict: ", new_student)
     #print("All students list:", all_students)
     

def f02view_students():
     print("2. View all students")
     global all_students
     if all_students == None:             #if no student was entered before,  no data:
          enter_student = input("No students in database, do you want to add student (y/n)?:")
          if enter_student == 'y':
               f01add_student()
          else:
               main_menu()
        
     for item in all_students:      #go through all entries, print text def. by detected datatype:
          if type(item) == str:
               print("Name: ", item)
          elif type(item) == int:
               print("Age: ", item)
          elif type(item) == list:
               print("Courses: ", item)
          else:
               print("Error datatype.....")
     
     main_menu()


def f03search_student():
     print("3. Search student")
     global all_students
     search_student = input("Please type in full name of student to look for: ")
     search_student = search_student.capitalize()   #if name is written lower, ValueError
     
     for item in all_students:
          if type(item) == str:
               #print(search_student.lower(), item.lower())
               if item.lower() == search_student.lower(): #or search_student.lower() in item.lower(): #allows for partial comparison, if only name is given but full name in database
                    position = all_students.index(search_student)
                    print("Found student at index: ", position)
                    details = input("Do you want to display all details of this student (y/n)?")
                    if details == 'y':
                         print("Name: ", all_students[position])
                         print("Age: ", all_students[position+1])
                         print("Courses: ", all_students[position+2])
               else:
                    input("not found, press 'enter' to return main menu")   #why 3 times? Python?
                    
     main_menu()


def f04show_statistics():
     print("4. Show statistics")
     # print no. of students (len(list))
     # print set of unique courses
     # nested loop: print how many students are in each course
     # print courses with highest occupancy
     # print courses with lowest occupancy
     # print courses without student
     # type 'enter' to return to menu
     global all_students
     no_of_students = len(all_students) /3      #every 3rd element is a student (name, age, course)
     print("No. of students: ", no_of_students)
     


                     
                   
def exit():
     #print("Exit function running")
     global functions_active
     functions_active = "no"    #assign variable inactive to jump over function-check to enter main menu, therefore run to end-of-program


### calling main_menu function if script functions active allowed:
#if functions_active == "yes": main_menu()




##### TESTING:
f04show_statistics()
