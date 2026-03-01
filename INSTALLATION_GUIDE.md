# DesignRequest - DEPLOYMENT & INSTALLATION GUIDE

## 🎯 ДЛЯ БЫСТРОГО СТАРТА

### Windows пользователи:
```
1. Откройте папку DesignRequest
2. Дважды кликните на run.bat
3. Приложение откроется!
```

### macOS/Linux пользователи:
```bash
cd DesignRequest
chmod +x run.sh
./run.sh
```

---

## 📋 ТРЕБОВАНИЯ

**Минимальные:**
- Python 3.7+
- 50 МБ свободного места
- Windows 7+, macOS 10.9+, или любой современный Linux

**Никаких дополнительных установок не требуется!**
Все зависимости встроены в Python.

---

## 🔍 ПРОВЕРКА УСТАНОВКИ

### Проверка Python:
```bash
python --version
# Должно быть 3.7 или выше
```

### Проверка Tkinter (на Linux может потребоваться установка):
```bash
python -c "import tkinter; print('Tkinter OK')"
```

Если Tkinter не установлен:
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# Fedora
sudo dnf install python3-tkinter

# Arch Linux
sudo pacman -S tk

# macOS (обычно уже установлено)
brew install python-tk
```

---

## 📁 СТРУКТУРА ФАЙЛОВ

Обязательные файлы:
```
✅ database.py          - Модуль БД (ОБЯЗАТЕЛЕН)
✅ main.py              - Основное приложение (ОБЯЗАТЕЛЕН)
✅ config.py            - Конфигурация (рекомендуется)
```

Дополнительные файлы:
```
📄 run.bat              - Для Windows запуска
📄 run.sh               - Для Linux/macOS запуска
📄 README.md            - Документация
📄 QUICK_START.md       - Быстрый старт
📄 USER_GUIDE.py        - Полное руководство
📄 PROJECT_SUMMARY.md   - Резюме проекта
📄 FILE_INDEX.md        - Индекс файлов
📄 examples.py          - Примеры использования
📄 test_database.py     - Тесты
📄 requirements.txt     - Информация о зависимостях
```

**Важно:** database.py и main.py ДОЛЖНЫ быть в одной папке!

---

## 🚀 СПОСОБЫ ЗАПУСКА

### Способ 1: Через Python (всемирно)
```bash
# Перейдите в папку приложения
cd /путь/к/DesignRequest

# Запустите:
python main.py
# или на macOS/Linux:
python3 main.py
```

### Способ 2: Через скрипт (Windows)
```
1. Откройте папку DesignRequest
2. Дважды кликните run.bat
```

### Способ 3: Через скрипт (Linux/macOS)
```bash
1. Откройте терминал
2. cd /путь/к/DesignRequest
3. chmod +x run.sh
4. ./run.sh
```

### Способ 4: Создать ярлык (Windows)
1. Правый клик на run.bat
2. Отправить → Рабочий стол (ярлык)
3. Двойной клик на ярлык для запуска

---

## 🔧 УСТАНОВКА ДЛЯ ОТДЕЛЬНЫХ ОС

### Windows 10/11

**Опция 1: Через Windows Store (рекомендуется)**
1. Откройте Microsoft Store
2. Поищите "Python"
3. Установите Python 3.11 или выше
4. Готово! Запустите run.bat

**Опция 2: Через python.org**
1. Перейдите на https://www.python.org/downloads/
2. Скачайте Python 3.11+
3. **Важно:** отметьте "Add Python to PATH"
4. Установите
5. Запустите run.bat

### macOS

**Опция 1: Через Homebrew**
```bash
brew install python@3.11
```

**Опция 2: Через python.org**
1. Скачайте Python с https://www.python.org/
2. Установите
3. Откройте терминал и перейдите в папку приложения
4. Запустите: ./run.sh

### Linux

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install python3 python3-tk
```

**Fedora:**
```bash
sudo dnf install python3 python3-tkinter
```

**Arch Linux:**
```bash
sudo pacman -S python tk
```

Затем откройте терминал в папке приложения и запустите:
```bash
./run.sh
```

---

## ⚙️ ДОПОЛНИТЕЛЬНАЯ КОНФИГУРАЦИЯ

### Изменение параметров приложения

Откройте файл `config.py` и измените:

```python
# Размер окна
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700

# Название приложения
WINDOW_TITLE = "DesignRequest - Project Request Management System"

# Типы проектов
PROJECT_TYPES = ["Logo Design", "Web Design", "Mobile App", "UI/UX Design", "Other"]

# Статусы
STATUS_OPTIONS = ["New", "In Progress", "On Review", "Completed"]
```

Сохраните и перезапустите приложение.

---

## 🗄️ ДАННЫЕ И РЕЗЕРВНЫЕ КОПИИ

### Расположение данных
- Файл: `design_requests.db` в папке приложения
- Формат: SQLite3
- Автоматически создается при первом запуске

### Резервная копия

**Создание:**
```bash
# Linux/macOS
cp design_requests.db design_requests_backup.db

# Windows (PowerShell)
Copy-Item design_requests.db design_requests_backup.db
```

**Восстановление:**
```bash
# Скопируйте backup обратно в папку
cp design_requests_backup.db design_requests.db
```

**Автоматическое резервное копирование:**

Создайте скрипт для периодического резервного копирования:

**Windows (backup.bat):**
```batch
@echo off
set SOURCE=design_requests.db
set DEST=backup\design_requests_%date:~-4,4%-%date:~-10,2%-%date:~-7,2%.db
if not exist backup mkdir backup
copy "%SOURCE%" "%DEST%"
echo Backup created: %DEST%
```

**Linux/macOS (backup.sh):**
```bash
#!/bin/bash
SOURCE="design_requests.db"
DEST="backup/design_requests_$(date +%Y-%m-%d_%H-%M-%S).db"
mkdir -p backup
cp "$SOURCE" "$DEST"
echo "Backup created: $DEST"
```

---

## 🔐 БЕЗОПАСНОСТЬ

### Защита данных

1. **Расположение базы данных:**
   - Храните design_requests.db в защищенной папке
   - Ограничьте доступ другим пользователям

2. **Резервные копии:**
   - Делайте регулярные резервные копии
   - Храните копии в нескольких местах
   - Используйте облачное хранилище (Google Drive, Dropbox)

3. **Шифрование (опционально):**
   ```bash
   # Зашифруйте базу данных с помощью 7-Zip
   7z a -tzip -p design_requests.7z design_requests.db
   ```

---

## 📊 ТЕСТИРОВАНИЕ УСТАНОВКИ

После установки запустите тесты:

```bash
python test_database.py
```

**Ожидаемый результат:**
```
Ran 15 tests in 0.164s
OK
```

Если все 15 тестов пройдены - установка успешна!

---

## ✅ КОНТРОЛЬНЫЙ СПИСОК

- [ ] Python 3.7+ установлен
- [ ] Tkinter установлен (проверено: `python -c "import tkinter"`)
- [ ] Все файлы скопированы в одну папку
- [ ] database.py и main.py в одной папке
- [ ] Приложение запускается: `python main.py`
- [ ] Окно приложения открывается
- [ ] Таблица видна и пуста (первый запуск)
- [ ] Можно добавить тестовую заявку
- [ ] Тесты проходят: `python test_database.py` → OK (15/15)

---

## 🐛 РЕШЕНИЕ ПРОБЛЕМ

### Ошибка: "Python not found"
**Решение:**
1. Установите Python с python.org
2. **Важно:** отметьте "Add Python to PATH"
3. Перезагрузитесь
4. Попробуйте снова

### Ошибка: "No module named tkinter"
**Windows:**
1. Откройте "Установка и удаление программ"
2. Найдите Python
3. Нажмите "Изменить"
4. Выберите "Modify"
5. Отметьте "tcl/tk and IDLE"
6. Нажмите "Next" и "Install"

**Linux:**
```bash
sudo apt-get install python3-tk  # Ubuntu/Debian
sudo dnf install python3-tkinter # Fedora
```

### Приложение не запускается
1. Проверьте что вы в правильной папке
2. Убедитесь что database.py рядом с main.py
3. Откройте командную строку/терминал
4. Запустите: `python main.py` (посмотрите сообщение об ошибке)
5. Покажите сообщение об ошибке в диагностике

### Ошибка "Database error"
1. Проверьте свободное место на диске
2. Проверьте права доступа на файл
3. Удалите design_requests.db (создастся заново при запуске)
4. Перезапустите приложение

### Приложение работает медленно
1. Закройте другие приложения
2. Проверьте место на жестком диске
3. Перезагрузитесь
4. Если в БД много записей, архивируйте старые

---

## 📞 ДИАГНОСТИКА

Если возникли проблемы, соберите следующую информацию:

```bash
# 1. Версия Python
python --version

# 2. Версия Tkinter
python -c "import tkinter; print(tkinter.TkVersion)"

# 3. ОС
# Windows: Откройте "Параметры" → "Система"
# Linux: uname -a
# macOS: system_profiler SPSoftwareDataType

# 4. Текст ошибки (полностью)
python main.py 2>&1 | tee error_log.txt
```

Отправьте эту информацию при поиске решения.

---

## 🚀 ГОТОВО К РАБОТЕ!

Если вы следовали этому руководству, приложение должно быть установлено и готово к использованию.

**Первый запуск:**
1. Откройте приложение
2. Прочитайте QUICK_START.md
3. Добавьте тестовую заявку
4. Начните использовать!

**Если возникли вопросы:**
- Смотрите README.md
- Смотрите USER_GUIDE.py
- Смотрите QUICK_START.md

---

**Удачи с DesignRequest! 🎉**
