from datetime import datetime


class WorkSession:
    """Рабочая сессия"""
    def __init__(self, employee_id, time_card_id):
        self.employee_id = employee_id
        self.time_card_id = time_card_id
        self.start_time = datetime.now()
        self.end_time = None


    def __str__(self):
        return f"Рабочая сессия для сотрудника: {self.employee_id}. Начало: {self.start_time}, Конец: {self.end_time if self.end_time is not None else '---'}"

    def __repr__(self):
        return f"Рабочая сессия для сотрудника: {self.employee_id}. Начало: {self.start_time}, Конец: {self.end_time if self.end_time is not None else '---'}"