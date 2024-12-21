from datetime import datetime

from services.event_logger import EventLogger
from models.work_session import WorkSession


class AttendanceService:
    def __init__(self):
        self.logger = EventLogger()
        self.attendance_records = []


    def end_session(self, work_session):
        work_session.end_time = datetime.now()

    def get_duration(self, work_session):
        if work_session.end_time:
            return (work_session.end_time - work_session.start_time).seconds / 3600
        return 0

    def record_attendance(self, employee_id, time_card_id):
        """
        Фиксирует посещаемость сотрудника.
        """
        record = WorkSession(
            employee_id=employee_id,
            time_card_id=time_card_id,
        )

        self.attendance_records.append(record)
        self.logger.log_event("INFO", f"Посещение записано: {record}")
        return record

    def end_attendance(self, employee_id, time_card_id):
        """
        Фиксирует завершение рабочего дня
        """
        record = None
        for attendance_record in reversed(self.attendance_records):
            if attendance_record.employee_id == employee_id and attendance_record.time_card_id == time_card_id:
                record = attendance_record
                break
        if record:
            self.end_session(record)
            self.logger.log_event("INFO", f"Завершение рабочего дня зафиксировано: {record}")
        else:
            self.logger.log_event("ERROR", f"Нет записи о начале рабочего дня: {employee_id}, {time_card_id}")
            raise Exception("Нет записи о начале рабочего дня")
        return record

    def get_attendances_duration(self, employee_id, time_card_id):
        records = []
        for attendance_record in self.attendance_records:
            if attendance_record.employee_id == employee_id and attendance_record.time_card_id == time_card_id:
                records.append(attendance_record)
        if records:
            sum_time = 0
            overtime = 0
            for record in records:
                time = self.get_duration(record)
                if time >= 8:
                    sum_time += time - time % 8
                    overtime += time % 8
                else:
                    sum_time += time
            return sum_time, overtime
        else:
            self.logger.log_event("ERROR", f"Нет записей о начале рабочего дня: {employee_id}, {time_card_id}")
            raise Exception("Нет записей о начале рабочего дня")

    def get_all_attendances(self):
        return self.attendance_records