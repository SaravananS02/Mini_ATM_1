class a:
    def __init__(self,name,age,id_no):
        self.name=name
        self.age=age
        self.id_no=id_no
    def fun(self):
        print(f"Who are you?:{self.name}")
    def fun_1(self):
        print(f"Who are you?:{self.name}")
        print(f"Age is {self.age} old Man")
        print(f"Id number is {self.id_no}")
    def fun_2(self):
        print(f"Who are you?:{self.name}")

var=a("saravanan",23,1063)
var.fun()
var.fun_1()
var.fun_2()
