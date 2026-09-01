class Employee:
    # Add the constructor
    def __init__(self, name):
        self.name = name



class Developer(Employee):
    # Add the constructor and display_profile()
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

    def display_profile(self):
        print(f"Employee: {self.name}\nLanguage: {self.language}")


name = input().strip()
language = input().strip()
# Create a Developer object and display its profile

developer = Developer(name, language)

developer.display_profile()