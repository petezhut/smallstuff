from pymongo import Connection

class Database:
    conn = Connection()
    
    def DbInit(self):
        db = self.conn.smallstuff
        db.workouts.drop()
        db.exercises.drop()
        workouts = db.workouts
        exercises = db.exercises

