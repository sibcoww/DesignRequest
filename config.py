"""
Configuration settings for DesignRequest application.
Centralized configuration for easy customization.
"""

# Database Configuration
DATABASE_FILE = "design_requests.db"
DATABASE_TIMEOUT = 30  # seconds

# GUI Configuration
WINDOW_TITLE = "DesignRequest - Система управления заявками на дизайн"
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
WINDOW_MIN_WIDTH = 1000
WINDOW_MIN_HEIGHT = 600

# Font Configuration
FONT_TITLE = ("Arial", 16, "bold")
FONT_NORMAL = ("Arial", 10)
FONT_SMALL = ("Arial", 9)

# Status Configuration
STATUS_OPTIONS = ["Новая", "В работе", "На проверке", "Завершена"]
STATUS_COLORS = {
    "Новая": "#FFE5E5",           # Light red
    "В работе": "#FFFACD",        # Light yellow
    "На проверке": "#E5F5FF",     # Light blue
    "Завершена": "#E5FFE5"        # Light green
}

# Project Types
PROJECT_TYPES = [
    "Дизайн логотипа",
    "Веб-дизайн",
    "Мобильное приложение",
    "UI/UX дизайн",
    "Другое"
]

# Table Configuration
TABLE_HEIGHT = 15
TABLE_COLUMNS = {
    "ИД": 40,
    "Имя клиента": 120,
    "Контакт": 120,
    "Тип проекта": 100,
    "Статус": 100,
    "Срок": 100,
    "Создано": 130
}

# Text Widget Configuration
DESCRIPTION_HEIGHT = 3
DESCRIPTION_WIDTH = 100

# Padding Configuration
PADDING_MAIN = "10"
PADDING_FRAME = "10"
PADDING_SMALL = "5"

# Date Format
DATE_FORMAT = "%Y-%m-%d"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

# Messages
MESSAGES = {
    "ADD_SUCCESS": "Заявка успешно добавлена!",
    "UPDATE_SUCCESS": "Заявка успешно обновлена!",
    "DELETE_SUCCESS": "Заявка успешно удалена!",
    "STATUS_SUCCESS": "Статус успешно изменён!",
    "VALIDATION_ERROR": "Ошибка валидации",
    "REQUIRED_FIELDS": "Требуются имя клиента и тип проекта.",
    "INVALID_DATE": "Срок должен быть в формате ГГГГ-ММ-ДД.",
    "SELECT_REQUEST": "Пожалуйста, выберите заявку.",
    "CONFIRM_DELETE": "Вы уверены, что хотите удалить эту заявку?",
    "SEARCH_EMPTY": "Введите текст для поиска.",
    "NO_RESULTS": "Заявки, соответствующие запросу, не найдены.",
    "ERROR": "Ошибка",
    "SUCCESS": "Успех",
    "WARNING": "Предупреждение",
    "INFO": "Информация"
}

# Error Messages
ERROR_MESSAGES = {
    "DB_ERROR": "Произошла ошибка базы данных.",
    "LOAD_ERROR": "Ошибка загрузки заявок:",
    "ADD_ERROR": "Ошибка добавления заявки:",
    "UPDATE_ERROR": "Ошибка обновления заявки:",
    "DELETE_ERROR": "Ошибка удаления заявки:",
    "SEARCH_ERROR": "Ошибка поиска заявок:",
    "FILTER_ERROR": "Ошибка фильтрации заявок:",
    "STATUS_ERROR": "Ошибка изменения статуса:"
}
