from services.event_logger import EventLogger


class ReportGenerator:
    def __init__(self):
        self.logger = EventLogger()

    def generate_attendance_report(self, attendance_records):
        """
        Генерирует отчет по посещаемости сотрудников.
        """
        self.logger.log_event("INFO", "Генерируется отчет по посещаемости сотрудников...")
        report = "\nОтчет о посещаемости:\n"
        for record in attendance_records:
            report += f"Сотрудник {record.employee_id} - Смарт-Карта {record.time_card_id} - Время {record.end_time - record.start_time if record.end_time is not None else record.start_time}\n"
        self.logger.log_event("INFO", "Отчет по посещаемости сгенерирован.")
        return report