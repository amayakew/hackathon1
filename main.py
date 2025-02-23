from db_connect import get_cursor
from users_manager import UsersManager
from registration import registration
from create_workout_plan import create_workout_plan
from display_menu import display_menu

def main():
    name = input('Hi! Please, enter your name: ')
    user_manager = UsersManager()
    user = user_manager.get_user(name)
    if user:
        print(f"\nHello, {user.name}")
    else:
        print(f"\nHello, {name}. Looks like you new here. Please answer few questions to create your workout plan: ")
        user = registration(name)
        create_workout_plan(user)
    display_menu(user)
main()