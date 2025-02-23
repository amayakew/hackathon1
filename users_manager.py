from db_connect import get_cursor, commit
from user import User

class UsersManager:
    def get_user(self,name):
        cursor = get_cursor()
        cursor.execute(f"SELECT * FROM users WHERE name = '{name}'")
        user_info = cursor.fetchone()
        if user_info:
            return User(user_info[0],user_info[1],user_info[2],user_info[3],user_info[4])
        else:
            return None
        
    def get_user_by_id(self,id):
        cursor = get_cursor()
        cursor.execute(f"SELECT * FROM users WHERE id = {id}")
        user_info = cursor.fetchone()
        if user_info:
            return User(user_info[0],user_info[1],user_info[2],user_info[3],user_info[4])
        else:
            return None
    
    def create_user(self,name,goal,level,workout_type):
        cursor = get_cursor()
        cursor.execute(f"INSERT INTO users(name,goal,level,workout_type) VALUES ('{name}','{goal}','{level}','{workout_type}')")
        commit()
        return self.get_user(name)
    
    def update_user(self, id: int, goal = None, level = None, workout_type = None):
        cursor = get_cursor()
        if goal:
            cursor.execute(f"UPDATE users SET goal = '{goal}' WHERE id = {id};")
        if level:
            cursor.execute(f"UPDATE users SET level = '{level}' WHERE id = {id};")
        if workout_type:
            cursor.execute(f"UPDATE users SET workout_type = '{workout_type}' WHERE id = {id};")
        commit()
        return self.get_user_by_id(id)
