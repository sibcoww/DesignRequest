#!/bin/bash

# DesignRequest Application Launcher for Linux/macOS
# This script launches the DesignRequest desktop application

echo "========================================"
echo "DesignRequest Application Launcher"
echo "========================================"
echo ""
echo "Проверка установки Python..."

if ! command -v python3 &> /dev/null; then
    if ! command -v python &> /dev/null; then
        echo "ОШИБКА: Python не установлен"
        echo "Пожалуйста, установите Python 3.7 или выше"
        exit 1
    fi
    PYTHON_CMD="python"
else
    PYTHON_CMD="python3"
fi

echo "Starting DesignRequest application..."
echo ""

$PYTHON_CMD main.py

if [ $? -ne 0 ]; then
    echo "ОШИБКА: Приложение не удалось запустить"
    echo "Проверьте наличие необходимых файлов:"
    echo "- database.py"
    echo "- main.py"
    exit 1
fi
