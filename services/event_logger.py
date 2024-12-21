from datetime import datetime

from utils.patterns.singleton import SingletonMeta


class EventLogger(metaclass=SingletonMeta):
    """Логгер событий в системе."""
    def __init__(self):
        self.logs = []

    def log_event(self, level, message):
        """
        Записывает лог с указанным уровнем и сообщением.
        """
        log = f"[{level}] - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {message}"
        self.logs.append(log)
        print(log)

    def get_logs(self):
        """
        Возвращает все записанные логи.
        """
        return self.logs