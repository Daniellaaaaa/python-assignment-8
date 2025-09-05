class AttendanceRegister:
    def __init__(self):
        self.record={}
    

    def mark_present(self, name):
        self.record[name]="present"

    def mark_absent(self, name):
        self.record[name]="absent"   

    def get_status(self, name):
        if name in self.record:
            return self.record[name]
        else:
            return "Not Found"  

    def show_register(self):
        return self.record      

register = AttendanceRegister()
register.mark_present("John")
register.mark_absent("Mary")

print(register.get_status("John")) 
print(register.show_register()) 