from pymongo import Connection

class Database:
    conn = Connection()
    workouts = conn.smallstuff.workouts
    exercises = conn.smallstuff.exercises
    
    def __init__(self):
        self.db = self.conn.smallstuff
        
    def DbInit(self):
        db = self.conn.smallstuff
        db.workouts.drop()
        db.exercises.drop()
