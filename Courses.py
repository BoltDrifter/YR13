class Lesson:
    def __init__(self,Title,Min,r):
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
    def __init__(self,CourseTitle,MaxS,NoL,L,M,R,T,MS):
        Lesson.__init__(self,L,M,R)
        Assessment.__init__(self,T,MS)
        self.__CourseTitle = CourseTitle
        self.__MaxStudents = MaxS
        self.__NumberofLessons = NoL
        self.__CourseAssessment = Assessment
        self.__CourseLesson = [0 for x in range(2)]
    def AddLesson(self,T,M,R):
        self.__CourseLesson.append(Lesson(T,M,R))
    def AddAssessment(self,T,M):
        self.__CourseAssessment.append(Assessment(T,M))
    def OutputCourseDetails(self):
        print(f"Course Title : {self.__CourseTitle}")
        print(f"Max Number of Students: {self.__MaxStudents}") 
        print(f"Number of Lessons: {self.__NumberofLessons}")
        Lesson.OutputLessonDetails(self)
        Assessment.OutputAssessmentDetails(self)

First = Course("CS101", 399, 20, "OOP", 30, False, "OOP Basics", 300)

First.OutputCourseDetails(  )