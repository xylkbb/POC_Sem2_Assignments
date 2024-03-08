class Doctor():        
    def __init__(self, first_name = 'John', last_name = 'Smith'):
        self.first_name = first_name
        self.last_name = last_name
        self.__format_names()
    
    def __format_names(self):
        self.first_name = self.first_name.title()
        self.last_name = self.last_name.title()
        
    def introduce(self):
        print('Hi, I am', self.first_name)
        
    def compare_name(self, name_to_compare):
        if self.first_name == name_to_compare:
            print('We have the same name!')
        else:
            print('Sorry, my name is different...')
    
    def get_first_last_name_together(self):
        return self.first_name + ' ' + self.last_name
    
    def __str__(self):
        return 'doctor=' + self.first_name + ' ' + self.last_name
        
doc_alex = Doctor('AleXandeR', 'SMith')
doc_alex.introduce()
doc_alex.compare_name('John')
print(doc_alex.__dict__)
print(Doctor.__dict__)