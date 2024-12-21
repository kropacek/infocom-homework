from services.event_logger import EventLogger


class AdminController:
    def __init__(self, admin):
        self.admin = admin

    def add_employee(self, employee):
        EventLogger().log_event("DEBUG", f"Админ {self.admin.name} добавил сотрудника {employee.name}")