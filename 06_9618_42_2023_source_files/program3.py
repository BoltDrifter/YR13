class Employee:
    def __init__(self, Hourly, ENo, JT):
        self.__HourlyPay =  Hourly
        self.__EmployeeNumber = ENo
        self.__Jobtitle = JT
        self.__PayYear2022 = [0.0 for x in range(0,52)]
    def GetEmployeeNumber(self):
        return self.__EmployeeNumber
    def SetPay(self, week, NoH):
        Pay = NoH * self.__HourlyPay
        self.__PayYear2022[week] = Pay
    def GetTotalPay(self):
        for x in range(len(self.__PayYear2022)):
            return self.__PayYear2022[x]
        
class Manager(Employee):
    def __init__(self, Hourly, ENo, JT, BV):
        super().__init__(Hourly, ENo, JT)
        self.__BonusValue = BV
    def SetPay(self, week, NoH):
        super().SetPay(week, NoH)
        Pay = NoH * (1 + (self.__BonusValue/100))
        self.__PayYear2022[week] = Pay
        