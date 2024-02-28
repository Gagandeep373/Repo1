class func:
 def __init__(self,fullname,age):
  self.name=fullname
  self.a=age
 def showname(self):
  return self.name
 def showage(self):
  return self.age
 def setname(self,fullname):
  self.name=fullname
 def setage(self,age):
  self.a=age

data=func("Gagan",29)

data.showname()
data.showage()

data.setname("GaGz")
data.setage(30)

data.showname()
data.showage()
