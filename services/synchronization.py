from utils.patterns.singleton import SingletonMeta
from services.event_logger import EventLogger


class SynchronizationService(metaclass=SingletonMeta):
    def __init__(self):
        self.logger = EventLogger()
        self.is_connected = True  # Эмуляция статуса подключения

    def synchronize(self, data):
        """
        Синхронизирует данные с сервером.
        :param data: Данные для синхронизации
        """
        if self.is_connected:
            self.logger.log_event("INFO", "Синхронизация начата")
            # Эмуляция успешной синхронизации
            self.logger.log_event("INFO", f"Синхронизация окончена успешно: {data}")
        else:
            self.logger.log_event("ERROR", "Синхронизация не успешна: нет подключения к бд")
            raise ConnectionError("Нет подключения к бд")
