from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, user_id, name, role):
        self.user_id = user_id
        self.name = name
        self.role = role

    @abstractmethod
    def get_info(self):
        pass


class Administrator(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, "Администратор")
        self.privileges = ["Добавить сотрудника", "Сгенерировать отчет"]

    def get_info(self):
        return f"Администратор: {self.name}, ID: {self.user_id}"


class Employee(ABC):
    """Абстрактный класс сотрудника."""

    def __init__(self, user_id, name, time_card_id, hourly_rate=200, status="Активный"):
        self.user_id = user_id
        self.name = name
        self.time_card_id = time_card_id
        self.status = status
        self.hourly_rate = hourly_rate

    @abstractmethod
    def get_info(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, user_id, name, time_card_id, hourly_rate, status="Активный"):
        super().__init__(user_id, name, time_card_id, hourly_rate, status)

    def get_info(self):
        return f"Сотрудник: {self.name}, Статус: {self.status}"


class FreelanceEmployee(Employee):
    def __init__(self, user_id, name, time_card_id, hourly_rate, status="Активный"):
        super().__init__(user_id, name, time_card_id, hourly_rate, status)

    def get_info(self):
        return f"Удаленный сотрудник: {self.name}, Статус: {self.status}"