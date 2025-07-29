class User:
    def __init__(self,name,age,gender,id_number):
        self.name = name
        self.age = age
        self.gender = gender
        self.id_number = id_number

    def show_infos(self):
        print('*' * 30)
        print('名字%s' % self.name)
        print('年龄%d' % self.age)
        print('性别%s' % self.gender)
        print('学（工）号%s' % self.id_number)

class Student(User):

    def __init__(self,name,age,gender,id_number):
        super().__init__(name,age,gender,id_number)
        self.course = []

    def show_infos(self):
        super().show_infos()
        print('所选课程:')
        for course in self.course:
            print(course.name)
        print('*' * 30)

    def add_course(self,course):
        self.course.append(course)

    def jian_course(self,course):
        if course not in self.course:
            raise Exception('课程不在学生列表')
        self.course.remove(course)
        return True


class Teacher(User):
    def __init__(self,name,age,gender,id_number,dao,cla):
        super().__init__(name,age,gender,id_number)
        self.dao = dao
        self.cla = cla

    def show_infos(self):
        super().show_infos()
        print('是否是导员:%s' %['否','是'][self.dao])
        print('管理的班级：')
        if not self.cla:
            print('空')
        else:
            for i in self.cla:
                print(i)
        print('*' * 30)

class Cla:
    def __init__(self,name,id_number,teacher,students):
        self.name = name
        self.id_number = id_number
        self.teacher = teacher
        self.students = students

    # 展示班级信息
    def show_infos(self):
        print('*' * 15 +'班级信息'+ '*' * 15)
        print('班级名称:%s' % self.name)
        print('班级号码:%d' % self.id_number)
        print('老师名称:%s' % self.teacher.name)
        print('班级学生:')
        if not self.students:
            print('空')
        else:
            for i in self.students:
                print(i.name)

    def add_infos(self,student):
        if student in self.students:
            raise Exception('学生已经存在')
        else:
            self.students.append(student)
            return True

    def remove_infos(self,student):
        if student in self.students:
            self.students.remove(student)
            return True
        else:
            raise Exception('要删除的学生不存在')

class Cursor:
    def __init__(self,name,id_number,teacher,students,type,num):
        self._name = name
        self.id_number = id_number
        self.teacher = teacher
        self.students = students
        self.type = type
        self.num = num
        self.numd = len(self.students)
        self.unnum = num - len(self.students)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = name

    def show_infos(self):
        print('*' * 15 + '课程信息' + '*' * 15)
        print('课程名称%s' % self._name)
        print('课程编号%d' % self.id_number)
        print('课程老师%s' % self.teacher.name)
        print(self.type)
        print('课程容量%d' % self.num)
        print('已选人数%d' % self.numd)
        print('剩余名额%d' % self.unnum)
        print('课程学生：')
        if not self.students:
            print('空')
        else:
            for i in self.students:
                print(i.name)
        print('*' * 30)

    def add_student(self,student):
        if student in self.students:
            print('已学习')
        if self.unnum <=0:
            print('课程已满')
        else:
            self.students.append(student)
            self.unnum -= 1
            self.numd += 1
            student.add_course(self)
            return True

    def remove_student(self,student):
        if student in self.students:
            self.students.remove(student)
            student.jian_course(self)
            self.unnum += 1
            self.numd -= 1
            return True
        else:
            raise Exception('学生未选此课程')


mia = Student('mia',19,'男',1)
tom = Student('tom',19,'女',2)
tom1 = Student('tom',19,'女',2)
tom2 = Student('tom',19,'女',2)
tom3 = Student('tom',19,'女',2)
tom4 = Student('tom',19,'女',2)
mia.show_infos()

dao1 = Teacher('dao1',19,'男',1, False,['python','java'])
dao2 = Teacher('dao2',35,'男',2, True,['c','java'])
dao1.show_infos()
dao2.show_infos()

one_cls = Cla('计算机一班',1001,dao1,[mia,tom])
one_cls.show_infos()
one_cls.remove_infos(tom)
one_cls.show_infos()

one_course = Cursor('java',1001,dao2,[mia,tom],'必修',5)
one_course.show_infos()
one_course.add_student(tom1)
one_course.add_student(tom2)
one_course.add_student(tom3)
one_course.add_student(tom4)
one_course.show_infos()

one_course.remove_student(tom1)
one_course.show_infos()

tom2.show_infos()