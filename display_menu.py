from create_workout_plan import create_workout_plan
from exercises_manager import get_exercises_for_user, delete_plan
from registration import get_goal, get_level, get_type
from users_manager import UsersManager

def display_menu(user):
    print('\nSelect an option: ')
    print('1. Display my workout plan')
    print('2. View exercise instruction')
    print('3. Create a new plan')
    print('4. Update user details')
    print('5. Exit')
    user_choice = input('-> ')

    if user_choice == '1':
        display_workout_plan(user)
    elif user_choice == '2':
        view_exercise_instruction(user)
    elif user_choice == '3':
        change_workout_plan(user)
    elif user_choice == '4':
        update_user_details(user)
    elif user_choice == '5':
        print('\nBye! Stay strong and healthy, have a good day;)')
    else:
        print('\nInvalid choice. Choose number from 1 to 4.')
        display_menu(user)

def update_user_details(user):
    goal = None
    level = None
    workout_type = None

    user_input = input(f'To update your current goal ({user.goal}) press y. Press anything else to continue ')
    if user_input == 'y':
        goal = get_goal()

    user_input = input(f'To update your current expertise level ({user.level}) press y. Press anything else to continue ')
    if user_input == 'y':
        level = get_level()

    user_input = input(f'To update your workout plan ({user.workout_type}) press y. Press anything else to continue ')
    if user_input == 'y':
        workout_type = get_type()

    if not goal and not level and not workout_type:
        print('Nothing was selected to update')
        return display_menu(user)
    user_manager = UsersManager()
    new_user = user_manager.update_user(user.id, goal, level, workout_type)
    print(f'User was updated sucesfully, creating a new plan according to the changes')
    return change_workout_plan(new_user)
    



def workout_instructions(user):
    print(f'\nHere is your wotkout plan according to your expertice level: {user.level}:\n')
    if user.goal == 'weight loss':
        print('Perform 3-4 sets with 10-15 reps for each exercise.')
    elif user.goal == 'strength':
        print('Perform 5 sets with 5-7 reps for each exercise.')
    else:
        print('Perform 3-4 sets with 8-12 reps for each exercise.')
    
    if user.workout_type == 'full body':
        print('Perform the workout 2-3 times a week.') 
    else:
        print('Alternate those workouts 3-4 times a week.')

def display_workout_plan(user):
    workout_instructions(user)
    exercises = get_exercises_for_user(user)
    plan_to_exercises = {}
    for exercise in exercises:
        if exercise.plan in plan_to_exercises:
            plan_to_exercises[exercise.plan].append(exercise)
        else:
            plan_to_exercises[exercise.plan] = [exercise]
    for plan,exercises_list in plan_to_exercises.items():
        print(f"\nExercises for workout: {plan}")
        for exercise in exercises_list:
            exercise.print_summary()
    user_input = input("\nWant to see instructions? Press (y). To go back to menu press any other button. ")
    if user_input == 'y':
        return view_exercise_instruction(user)
    return display_menu(user)

def view_exercise_instruction(user):
    exercises = get_exercises_for_user(user)
    print('\nList of available exercises: ')
    for exercise in exercises:
        exercise.print_summary()
    exercise_number = input("\nEnter exercise id or name to see the instruction: ")
    found = False
    
    for exercise in exercises:
        if exercise_number == str(exercise.id) or exercise_number == exercise.name:
            print(f"\nExercise: {exercise.name}")
            print(f"\n{exercise.instructions}\n")
            found = True
            break
    if not found:
        print("Exercise not found")
    user_input = input("Want to see other instructions? Press (y). To go back to menu press any other button. ")
    if user_input == 'y':
        return view_exercise_instruction(user)
    return display_menu(user)

def change_workout_plan(user):
    delete_plan(user)
    create_workout_plan(user)
    user_input = input("\nWant to see new plan? Press 1. To go back to menu press any other button. ")
    if user_input == '1':
        return display_workout_plan(user)
    return display_menu(user)