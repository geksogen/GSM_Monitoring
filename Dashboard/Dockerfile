# Используем официальный образ Python в качестве базового
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы requirements.txt и app.py в рабочую директорию
COPY requirements.txt .
COPY app.py .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт 8501 для Streamlit
EXPOSE 8501

# Команда для запуска приложения Streamlit
CMD ["streamlit", "run", "app.py"]
