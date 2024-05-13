class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name
        
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    

class Driver(Person):
    def __init__(self, age, name):
        super().__init__(age, name)
        
    def get_driver(self):
        return self.name
    

class Mp(Person):
    def __init__(self, age, name, constituency, spending_limit):
        super().__init__(age, name)
        self.constituency = constituency
        self.spending_limit = spending_limit
        self.expenses = 0
        
    def get_constituency(self):
        return self.constituency
    
    def get_spending_limit(self):
        return self.spending_limit
    
    def spend_money(self, money):
        self.expenses += money


class Minister(Mp):
    def __init__(self, age, name, constituency, spending_limit, ministry):
        super().__init__(age, name, constituency, spending_limit)
        self.ministry = ministry


class Pm(Minister):
    def __init__(self, age, name, constituency, spending_limit, ministry, permission_to_arrest):
        super().__init__(age, name, constituency, spending_limit, ministry)
        self.have_plane = True
        self.is_permission_to_arrest = permission_to_arrest
        
    def get_ministry(self):
        return self.ministry


class Commissioner(Person):
    def __init__(self, age, name):
        super().__init__(age, name)
        
    def can_arrest(self, mp):
        if mp.expenses > mp.spending_limit:
            return True
        else:
            return False
    
    def can_arrest_pm(self, pm, minister):
        if minister.expenses > minister.spending_limit and pm.is_permission_to_arrest:
            return True
        else:
            return False


if __name__ == "__main__":
    Anmol = Minister(55, "Anmol Srivastava", "Vanarasi", 100000, "Roadway")
    Anmol.spend_money(200000)
    print(Anmol.get_constituency())
    
    Ojesh = Pm(60, "Ojesh", "Ghaziabad", 100000000, "prime", True)
    dsp = Commissioner(35, "Ishu")
    
    if dsp.can_arrest_pm(Anmol, Ojesh):
        print("Minister Arrested")
    else:
        print("Can't arrest")
