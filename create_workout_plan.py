from user import User
from api_connect import get_from_api
import random
from exercises_manager import save_exercises

a_muscle_group = ['lats','middle_back','lower_back','traps','biceps','forearms','neck','abdominals']
b_muscle_group = ['glutes','hamstrings','quadriceps','abductors','adductors','calves','chest','triceps']
muscle_groups = a_muscle_group + b_muscle_group
    

def create_exercise(user: User,muscle):
    result = get_from_api(muscle, user.level)
    if not result:
        result = get_from_api(muscle)
    return random.choice(result)

def create_fullbody_plan(user):
    exercise_list = []
    for muscle in muscle_groups:
        exercise = create_exercise(user,muscle)
        exercise_list.append(exercise)
    save_exercises(user,exercise_list,'full body')

def create_AB_plan(user):
    a_exercise_list = []
    for muscle in a_muscle_group:
        for _ in range(2):
            exercise = create_exercise(user,muscle)
            a_exercise_list.append(exercise)
    save_exercises(user,a_exercise_list,'a')
    
    b_exercise_list = []
    for muscle in b_muscle_group:
        for _ in range(2):
            exercise = create_exercise(user,muscle)
            b_exercise_list.append(exercise)
    save_exercises(user,b_exercise_list,'b')

def create_workout_plan(user: User):
    if user.workout_type == 'full body':
        create_fullbody_plan(user)
    else:
        create_AB_plan(user)
    print('Your workout plan has been created.')

