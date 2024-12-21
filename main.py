import time

from models.user import Administrator, Employee
from models.time_card import TimeCard
from controllers.attendance_controller import AttendanceController
from controllers.admin_controller import AdminController
from services.event_logger import EventLogger
from services.report_generator import ReportGenerator
from services.synchronization import SynchronizationService
from utils.patterns.abstract_factory import Client, FreelanceEmployeeFactory, FullTimeEmployeeFactory


if __name__ == "__main__":
    # Инициализация
    logger = EventLogger()
    admin = Administrator(user_id=1, name="Алиса")
    admin_controller = AdminController(admin)
    report_generator = ReportGenerator()
    sync_service = SynchronizationService()
    attendance_controller = AttendanceController()

    # Добавление смарт-карты
    card = TimeCard(312412)
    card2 = TimeCard(312413)

    # Добавление сотрудников
    employee_1 = Client(FullTimeEmployeeFactory(), user_id=2, name="Никита", time_card_id=312412, hourly_rate=2000).employee
    admin_controller.add_employee(employee_1)

    employee_2 = Client(FreelanceEmployeeFactory(), user_id=3, name="Алёна", time_card_id=312413, hourly_rate=2500).employee
    admin_controller.add_employee(employee_2)

    # Запуск рабочей сессии
    attendance_controller.check_in(employee_1)
    attendance_controller.check_in(employee_2)

    time.sleep(5)

    attendance_controller.check_out(employee_1)

    attendance_controller.check_in(employee_1)
    time.sleep(1)
    attendance_controller.check_out(employee_1)


    payment = attendance_controller.calculate_work_time(employee_1)

    logger.log_event("DEBUG", f"Сотрудник {employee_1.user_id} заработал {payment} рублей")

    # Получим все рабочие сессии
    all_work_sessions = attendance_controller.get_all_work_sessions()

    # Генерация отчета
    report = report_generator.generate_attendance_report(all_work_sessions)
    print(report)

    # Синхронизация данных
    try:
        sync_service.synchronize(all_work_sessions)
    except ConnectionError:
        logger.log_event("ERROR", "Failed to synchronize data.")

    # Вывод логов
    print("\nСистемные логи:")
    for log in logger.get_logs():
        print(log)
