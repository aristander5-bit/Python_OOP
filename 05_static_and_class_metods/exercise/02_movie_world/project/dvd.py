import calendar

class DVD:
    def __init__(self, name: str, _id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = _id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented: bool = False

    @classmethod
    def from_date(cls, dvd_id: int, name: str, date: str, age_restriction: int):
        _, month, year = date.split(".")
        month_name = calendar.month_name[int(month)]
        return cls(name, dvd_id, int(year), month_name, age_restriction)

    def __repr__(self) -> str:
        return (f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction "
                f"{self.age_restriction}. Status: {'' if self.is_rented else 'not '}rented")


