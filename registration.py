from users_manager import UsersManager

def get_goal():
    while True:
        user_goal = input('Please, choose your goal(weight loss,strength,muscle mass): ')
        if user_goal in ['weight loss','strength','muscle mass']:
            return user_goal
        else:
            print('Invalid goal. Please, select one of: weight loss,strength,muscle mass.')

def get_level():
    while True:
        user_level = input('Please, choose your level(beginner,intermediate,expert): ')
        if user_level in ['beginner','intermediate','expert']:
            return user_level
        else:
            print('Invalid choice. Please, select one of: beginner,intermediate,expert.')

def get_type():
    while True:
        workout_type = input('Please, choose prefered workout type(full body or AB). Not sure what to choose? You may leave this blank: ')
        if workout_type in ['full body','AB']:
            return workout_type
        elif workout_type == '':
            return 'full body'
        else:
            print('Invalid choice. Please, select one of: full body or AB.')

def registration(name):
    goal = get_goal()
    level = get_level()
    workout_type = get_type()
    user_manager = UsersManager()
    user = user_manager.create_user(name,goal,level,workout_type)
    return user

