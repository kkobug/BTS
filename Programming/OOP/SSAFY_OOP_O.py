class Student:

    def __init__(self, role):
        self.교육지원금 = False
        self.role = role
        if role == "반장":
            self.자치회_회의 = False
        elif role == "팀장":
            self.중간평가 = False
            self.최종평가 = False
        elif role == "팀원":
            pass
        else:
            self.role = "팀원"

    def 동의하기(self):
        self.교육지원금 = True

    def 회의참석(self):
        if self.role == "반장":
            self.자치회_회의 = True

    def 중간평가하기(self):
        if self.role == "팀장":
            self.중간평가 = True
        
    def 최종평가하기(self):
        if self.role == "팀장":
            self.최종평가 = True


# 반장님, 자치회 회의 참석해주세요
성아영 = Student("반장")
성아영.회의참석()
print(성아영.자치회_회의)

# 팀장님, 최종평가 해주세요
박준영 = Student("팀장")
박준영.최종평가하기()
print(박준영.최종평가)

# 동의서 제출해주세요
강동옥 = Student("팀원")
강동옥.동의하기()
print(강동옥.교육지원금)
