# Define the Student class
class Student:
    def hello(self):
        print("Hey there! I'm so excited to learn stuff.")

    def raise_hand(self):
        print("Pick me!")

# Define the ChattyStudent class, which inherits from Student
class ChattyStudent(Student):
    def hello(self):
        super().hello()  # Inherit and print the parent's hello message
        print("How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...")

    def raise_hand(self):
        for _ in range(10):
            super().raise_hand()  # Call the parent's raise_hand method 10 times

# Test the classes and methods
student = Student()
chatty_student = ChattyStudent()

# Test the hello method for both student types
student.hello()  # Output: "Hey there! I'm so excited to learn stuff."
chatty_student.hello()  # Output: Parent's message + chatty message

# Test the raise_hand method for both student types
student.raise_hand()  # Output: "Pick me!"
chatty_student.raise_hand()  # Output: "Pick me!" repeated 10 times
