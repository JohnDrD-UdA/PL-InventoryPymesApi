from config.config import session
from models.Unit.Unit_Table import Units
from models.Unit.Unit_DTO import UnitDTO

class UnitService():    
    def getUnits(self):
        try:
            result= session.query(Units).all()
            return result
        except Exception as e:
            print(e)
            return "fail"
    def createUnits(self,data: UnitDTO):
        try:
            new_unit= Units(name=data.name, state=data.state)
            session.add(new_unit)
            session.commit()
            return "OK"
        except Exception as e:
            print(e)
            return "fail"
    def updateUnits(self,id:int,data:UnitDTO):
        try:
            unit= session.query(Units).get(id)
            if unit:
                unit.name= data.name
                unit.state=data.state
                session.commit()
                return "ok"
            else:
                return "404"
        except Exception as e:
            print(e)
            return "fail"
    def deleteUnits(self,id:int):
        try:
            unit= session.query(Units).get(id)
            if unit:
                session.delete(unit)
                session.commit()
                return "ok"
            else:
                return "404"
        except Exception as e:
            print(e)
            return "fail"
    def getUnitById(seld,id:int):
        try:
            result= session.query(Units).get(id)
            if result:
                return result
            return "404"
        except Exception as e:
            print(e)
            return "fail"