class Student:

    def __init__(self):
        self.교육지원금 = False
        self.자치회_회의 = False

    def 동의하기(self):
        self.교육지원금 = True

    def 회의참석(self):
        self.자치회_회의 = True


class 반장(Student):

    def __init__(self):
        super(반장, self).__init__()


class 팀장(Student):

    def __init__(self):
        super(팀장, self).__init__()
        self.중간평가 = False
        self.최종평가 = False

    def 중간평가하기(self):
        self.중간평가 = True
        
    def 최종평가하기(self):
        self.최종평가 = True

    def 회의참석(self):
        pass


class 팀원(Student):

    def __init__(self):
        super().__init__()

    def 회의참석(self):
        pass

# 반장님, 자치회 회의 참석해주세요
성아영 = 반장()
성아영.회의참석()
print(성아영.자치회_회의)

# 팀장님, 최종평가 해주세요
박준영 = 팀장()
박준영.최종평가하기()
print(박준영.최종평가)

# 동의서 제출해주세요
강동옥 = 팀원()
강동옥.동의하기()
print(강동옥.교육지원금)
