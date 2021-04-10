class person:
    def __init__(self,n):
        self.sinhvien = n
        self.age = []
        self.name = []
        self.gender = []
    def hoten(self):
        for i in range (0,self.sinhvien):
            hoten=str(input("Nhap ten sinh vien:".format(i)))
            self.name.append(hoten)
        return self.name
    def tuoi(self):
        for i in range(0,self.sinhvien):
            tuoi=int(random.randrange(17,25))
            self.age.append(tuoi)
        return self.age
    def gioitinh(self):
        for i in range(0,self.sinhvien):
            gioitinh=str(input("gioi tinh:".format(i))
            self.gender.append(gioitinh)
        return self.gender