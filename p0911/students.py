class Students:
    slist=[]

    def add(self,s):
        self.slist.append(s)

    def print(self):
        print()
        print("[학생 성적 출력]")
        print("번호","이름","국어","영어","수학","합계","평균","등수")
        print("-"*60)
        for s in self.slist:
            print(s)