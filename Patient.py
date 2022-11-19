class Patient:
    def __init__(self, name, age, bmi, illness):
        self._name = name
        self._age = age
        self._bmi = bmi
        self._illness = illness

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_bmi(self):
        return self._bmi

    def get_illness(self):
        return self._illness
