Project Name: "Workout Manager"
My 'Workout Manager' helps users to plan gym workouts, track them and update. User also has an ability to set the goal, experience level and workout frequency.
To run this project on your computer, first make sure all the packages from requirements.txt file are installed.
Then create .env file in the root of the project with the following variables:
    DATABASE = <database_name>
    NAME = <db_username>
    PASSWORD = <db_password>
    HOSTNAME = <db_host>
    PORT = <db_port>
    NINJA_API_KEY = <you can ask me for mine or sign in to https://www.api-ninjas.com/api/exercises>
After setting your .env file, execute init_db.py file to set up necessary tables.
Now you can run the main.py file :)