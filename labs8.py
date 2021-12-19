class Mahasiswa():
    def __init__(self,inputnama,inputkelas,inputnim,inputnilai):
        self.Nama= inputnama
        self.Kelas= inputkelas
        self.Nim= inputnim
        self.Nilai=inputnilai


mhs1= Mahasiswa("Daniel","TI.21.A.1",312110490,95)
mhs2= Mahasiswa("Justin","TI.21.A.1",312110435,40)
mhs3= Mahasiswa("Gabriel","TI.21.A.1",312110765,65)
mhs4= Mahasiswa("Lucas","TI.21.A.1",312110420,70)
mhs5= Mahasiswa("Mbappe","TI.21.A.1",312110790,80)

print(mhs1.__dict__)
print(mhs2.__dict__)
print(mhs3.__dict__)
print(mhs4.__dict__)
print(mhs5.__dict__)
