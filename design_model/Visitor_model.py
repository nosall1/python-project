# -*- coding:utf-8 -*-
"""
 访问者模式
"""


class Medicine:
    name = ''
    price = 0.0

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def accept(self, visitor):
        pass


class Antibiotic(Medicine):
    def accept(self, visitor):
        visitor.visit(self)


class Coldrex(Medicine):
    def accept(self, visitor):
        visitor.visit(self)


class Visitor:
    name = ''

    def setName(self, name):
        self.name = name

    def visit(self, medicine):
        pass


class Charger(Visitor):
    def visit(self, medicine):
        print ('CHARGE:%s lists the Medicine %s.Price:%s' % (self.name, medicine.getName(), medicine.getPrice()))


class Pharmacy(Visitor):
    def visit(self, medicine):
        print ('PHARMACY:%s lists the Medicine %s.Price:%s' % (self.name, medicine.getName(), medicine.getPrice()))


class ObjectStructure:
    pass


class Prescription(ObjectStructure):
    medicines = []

    def addMedicine(self, medicine):
        self.medicines.append(medicine)

    def rmvMedicine(self, medicine):
        self.medicines.remove(medicine)

    def visit(self, visitor):
        for medc in self.medicines:
            medc.accept(visitor)


if __name__ == '__main__':
    yinqiao_pill = Coldrex('Yinqiao Pill', 2.0)
    penicillin = Antibiotic('Penicillin', 3.0)
    doctor_prsrp = Prescription()
    doctor_prsrp.addMedicine(yinqiao_pill)
    doctor_prsrp.addMedicine(penicillin)

    charge = Charger()
    charge.setName('Doctor Strage')
    pharmacy = Pharmacy()
    pharmacy.setName('Doctor Wei')
    doctor_prsrp.visit(charge)
    doctor_prsrp.visit(pharmacy)
