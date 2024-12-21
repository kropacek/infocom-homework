from abc import ABC, abstractmethod

from models.user import Employee, FullTimeEmployee, FreelanceEmployee


class EmployeeFactory(ABC):
    """Фабрика для создания сотрудников."""

    @abstractmethod
    def create_employee(self, user_id, name, time_card_id, hourly_rate, status="Активный") -> Employee:
        raise NotImplementedError


class FullTimeEmployeeFactory(EmployeeFactory):
    def create_employee(self, user_id, name, time_card_id, hourly_rate, status="Активный"):
        return FullTimeEmployee(user_id, name, time_card_id, hourly_rate, status)


class FreelanceEmployeeFactory(EmployeeFactory):
    def create_employee(self, user_id, name, time_card_id, hourly_rate, status="Активный"):
        return FreelanceEmployee(user_id, name, time_card_id, hourly_rate, status)


class Client:
    def __init__(self, employee_factory, user_id, name, time_card_id, hourly_rate):
        self.employee = employee_factory.create_employee(user_id=user_id, name=name, time_card_id=time_card_id, hourly_rate=hourly_rate)
