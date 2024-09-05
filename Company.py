import datetime as dt


class Company:
    def __init__(self,e):
        self.companyname = e
        self.email = ""
        self.date = None
    
    def SetDate(self, a):
        self.date = a
    def GetName(self):
        return(self.companyname)
    def GetDate(self):
        return(self.date)
    def GetEmail(self):
        return(self.email)
    

a = Company("Twitter")
b = Company("Nike")
c = Company("Sujay Enterprises")
d = Company("Interpol")
e = Company("Boeing")   

a.SetDate()
b.SetDate("02/12/2024")
c.SetDate("17/11/2026")
d.SetDate("22/09/2023")
e.SetDate("06/05/2020")
   
g = a.GetDate()
f = b.GetDate()
k = c.GetDate()
l = d.GetDate()
r = e.GetDate()

last = "1/1/1999"

if last < g:
    last = g
    print(last)

if last < f:
    last = f
    print(last)

if last < k:
    last = k
    print(last)

if last < l:
    last = l
    print(last)
if last < r:
    last = r
    print(last)
