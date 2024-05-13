class Inverter:
    def __init__(self, type, power_rating):
        self.type = type
        self.power_rating = power_rating

    def display_info(self):
        print("Type:", self.type)
        print("Power Rating:", self.power_rating)


class SolarInverter(Inverter):
    def __init__(self, type, power_rating, has_solar_panels, has_battery, has_grid):
        super().__init__(type, power_rating)
        self.has_solar_panels = has_solar_panels
        self.has_battery = has_battery
        self.has_grid = has_grid

    def display_info(self):
        super().display_info()
        print("Solar Panels:", "Yes" if self.has_solar_panels else "No")
        print("Battery:", "Yes" if self.has_battery else "No")
        print("Grid:", "Yes" if self.has_grid else "No")


class PCU(SolarInverter):
    def __init__(self, power_rating, has_solar_panels, has_battery, has_grid):
        super().__init__("PCU", power_rating, has_solar_panels, has_battery, has_grid)


class GTI(SolarInverter):
    def __init__(self, power_rating, has_solar_panels, has_grid):
        super().__init__("GTI", power_rating, has_solar_panels, False, has_grid)


class Regalia(SolarInverter):
    def __init__(self, power_rating, has_solar_panels, has_battery, has_grid):
        super().__init__("Regalia", power_rating, has_solar_panels, has_battery, has_grid)


if __name__ == "__main__":
    pcu = PCU(5000, True, True, False)
    pcu.display_info()

    print()

    gti = GTI(4000, True, True)
    gti.display_info()

    print()

    regalia = Regalia(6000, True, False, False)
    regalia.display_info()
