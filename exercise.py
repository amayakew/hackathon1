class Exercise:
    def __init__(self,id,name,muscle,type,plan,instructions,user_id):
        self.id = id
        self.name = name
        self.muscle = muscle
        self.type = type
        self.plan = plan
        self.instructions = instructions
        self.user_id = user_id

    def print_summary(self):
        print(f"id: {self.id} - {self.name} - {self.muscle}")