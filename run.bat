@echo off
REM Приложение DesignRequest для Windows
REM Этот скрипт запускает настольное приложение DesignRequest

echo ========================================
echo Запуск приложения DesignRequest
echo ========================================
echo.
echo Проверка установки Python...

python --version >nul 2>&1
if errorlevel 1 (
    echo ОШИБКА: Python не установлен или не добавлен в PATH
    echo Установите Python 3.7 или выше
    pause
    exit /b 1
)

echo Запуск приложения DesignRequest...
echo.

python main.py

if errorlevel 1 (
    echo ОШИБКА: Приложение не запустилось
    echo Проверьте наличие всех необходимых файлов:
    echo - database.py
    echo - main.py
    pause
    exit /b 1
)
