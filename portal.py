class Portal:
    def __init__(self, course_name):
        self.course_name = course_name
        self.__is_locked = False 
        self.submissions = []

    
    def lock_portal(self):
        self.__is_locked = True
        print(f"The portal for {self.course_name} is now locked.")

   
    def submit_assignment(self, student_name, work):
        if self.__is_locked:
            raise PermissionError("Submission failed: The deadline has passed and the portal is locked.")
        
        self.submissions.append({"student": student_name, "work": work})
        print(f"Success: {student_name}'s work has been submitted.")