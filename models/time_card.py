from services.event_logger import EventLogger


class TimeCard:
    """Смарт-карта для учета времени."""
    def __init__(self, card_id):
        self.card_id = card_id

    def scan_card(self):
        return f"Карта {self.card_id} отсканирована"


class AttendanceDeviceAdapter:
    """Адаптер для преобразования смарт-карты в запись посещаемости."""
    def __init__(self, time_card: TimeCard):
        self.time_card = time_card

    def record_attendance(self):
        card_info = self.time_card.scan_card()
        EventLogger().log_event("DEBUG", f"Посещение записано: {card_info}")
        return card_info