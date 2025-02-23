from db_connect import get_cursor,commit
from exercise import Exercise

def save_exercises(user,exercise_list,plan):
    cursor = get_cursor()
    for exercise in exercise_list:
        name = exercise['name'].replace("'", '"')
        instructions = exercise['instructions'].replace("'", '"')
        cursor.execute(f"""INSERT INTO exercises(name,muscle,type,plan,instructions,user_id) VALUES ('{name}',
                       '{exercise['muscle']}','{exercise['type']}','{plan}','{instructions}',{user.id});""")
    commit()

def get_exercises_for_user(user):
    cursor = get_cursor()
    cursor.execute(f"SELECT * FROM exercises WHERE user_id = {user.id}")
    results = cursor.fetchall()
    exercise_list = []
    for result in results:
        exercise_list.append(Exercise(result[0],result[1],result[2],result[3],result[4],result[5],result[6]))
    return exercise_list

def delete_plan(user):
    cursor = get_cursor()
    cursor.execute(f"DELETE FROM exercises WHERE user_id = {user.id}")
    commit()
    print('Previous workout plan has been deleted.')