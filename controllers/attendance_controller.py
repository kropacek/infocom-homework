from services.attendance_service import AttendanceService
from services.overtime_calculator import TimeCalculator, RegularTimeStrategy, OvertimeStrategy
from models.time_card import TimeCard


class AttendanceController:
    def __init__(self):
        self.attendance_service = AttendanceService()

    def check_in(self, employee):
        """
        Осуществляет чек-ин сотрудника.
        """
        time_card = TimeCard(employee.time_card_id)
        return self.attendance_service.record_attendance(employee.user_id, time_card.card_id)


    def check_out(self, employee):
        """
        Осуществляет чек-аут сотрудника.
        """
        time_card = TimeCard(employee.time_card_id)
        return self.attendance_service.end_attendance(employee.user_id, time_card.card_id)


    def calculate_work_time(self, employee):
        """
        Осуществляет расчет рабочего времени сотрудника
        """
        time_card = TimeCard(employee.time_card_id)
        work_time, over_work_time = self.attendance_service.get_attendances_duration(employee.user_id, time_card.card_id)

        payment = 0
        if over_work_time != 0:
            time_calc = TimeCalculator(OvertimeStrategy())
            payment += time_calc.calculate_time(over_work_time, employee.hourly_rate)
        time_calc = TimeCalculator(RegularTimeStrategy())
        payment += time_calc.calculate_time(work_time, employee.hourly_rate)

        return round(payment, 2)


    def get_all_work_sessions(self):
        return self.attendance_service.get_all_attendances()


