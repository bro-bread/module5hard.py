class User:
    list_user = []
    list_user_pass = []
    def __init__(self, nickname, age, password):
        self.nickname = str(nickname)
        self.age = int(age)
        self.password = password
        User.list_user.append(nickname)
        User.list_user_pass.append(password)


rer0 = User("admin", 99,"*k*e*k*_*l*o*l*_*a*r*b*i*d*o*l*")
rer1 = User("gав", 1, "123456789")
rer2 = User("Вова2007", 21, "Vova_2007")












