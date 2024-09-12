class Lesson:
    def __init__(self,Title,Min,r) -> None:
        self.__LessonTitle = Title
        self.__DurationMinutes = Min
        self.__RequiresLab = r
    def OutputLessonDetails(self):
        print(f"The Lesson Title is: {self.__LessonTitle}")
        print(f"The Duration is: {self.__DurationMinutes} minutes")
        print(f"Lab Required: {self.__RequiresLab}")
class Assessment:
    def __init__(self,Title,Max):
        self.__AssesmentTitle = Title
        self.__MaxMarks = Max
    def OutputAssessmentDetails(self):
        print(f"The Title of the assessment is : {self.__AssesmentTitle}")
        print(f"Max Marks : {self.__MaxMarks}")
class Course:
    def __init__(self,CourseTitle,MaxS,NoL):
        self.__CourseTitle = CourseTitle
        self.__MaxStudents = MaxS
        self.__NumberofLessons = NoL
        self.__CourseAssessment = Assessment
        self.__CourseLesson = [0 for x in range(50)]
    def AddLesson(self,T,M,R):
        self.__CourseLesson.append(Lesson(T,M,R))
    def AddAssessment(self,T,M):
        self.__CourseAssessment.append(Assessment(T,M))
    def OutputCourseDetails(self):
        print(self.__CourseTitle, "Maximum number: ", self.__MaxStudents)

First = Course("CS101", 399, 20)
First.AddLesson("OOP",90,False)
First.OutputCourseDetails()