class Student(object):
  
  def __init__(self, name, age, country='null'):
    
    self.name = name
    self.age = age
    self.country = country
    
  def info(self, show_all=True):
    
    if show_all:
      
      print(f'{self.name}, {self.age}, {self.country}')
      
    else:print(self.name)
           
student_1 = Student('muhammed', 21)
student_1.info()
student_1.info(False)
