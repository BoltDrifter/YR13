
class Lesson:
  def __init__(self,t,d,r):
    self.__Title = t
    self.__Duration = d
    self.__RequiresLab = r
  def OutputLessonDetails(self):
    print("Title:",self.__Title)
    print("Duration:",self.__Duration)
    if self.__RequiresLab:
      print("Requires lab.")
    else:
      print("Does not require lab.")

class Assessment:
  def __init__(self,t,m):
    self.__Title = t
    self.__MaxMarks = m

  def OutputAssessmentDetais(self):
    print("Title:",self.__Title)
    print("Max Marks:",self.__MaxMarks)

class Course:
  def __init__(self,t,m):
    self.__CourseTitle = t
    self.__MaxStudents = m
    self.__NumberOfLessons = 0
    self.__CourseLesson = []
    self.__CourseAssessment = Assessment

  def AddLesson(self,t,d,r):
    self.__NumberOfLessons += 1
    self.__CourseLesson.append(Lesson(t,d,r))

  def AddAssessment(self,t,m):
    self.__CourseAssessment = Assessment(t,m)

  def OutputCourseDetails(self):
    print(self.__CourseTitle, "Maximum number:",self.__MaxStudents)
    for i in range(self.__NumberOfLessons):
      print(self.__CourseLesson[i].OutputLessonDetails())

Maths = Course("Math",120)
Maths.AddLesson("Algebra",60, True)
Maths.OutputCourseDetails()