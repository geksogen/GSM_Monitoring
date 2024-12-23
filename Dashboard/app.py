import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import random
import time
from datetime import datetime, timedelta

# Функция для генерации случайного значения температуры
def generate_temperature():
    return random.uniform(-5, 25)

# Функция для обновления данных
def update_data(data):
    current_time = datetime.now()
    temperature = generate_temperature()
    data.append({'time': current_time, 'temperature': temperature})
    return data

# Функция для создания индикатора температуры
def create_temperature_indicator(current_temperature, previous_temperature):
    delta = current_temperature - previous_temperature
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=current_temperature,
        delta={'reference': previous_temperature, 'increasing': {'color': 'red'}, 'decreasing': {'color': 'green'}},
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Текущая температура"},
        gauge={
            'axis': {'range': [-5, 25]},
            'bar': {'color': "darkblue"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [-5, 0], 'color': 'lightcoral'},
                {'range': [0, 20], 'color': 'lightgreen'},
                {'range': [20, 40], 'color': 'lightcoral'}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': -1
            }
        }
    ))
    return fig

# Основная функция Streamlit
def main():
    st.title("Дашборд температуры")

    # Инициализация данных
    if 'data' not in st.session_state:
        st.session_state.data = []

    # Placeholder для отображения текущей температуры
    current_temp_placeholder = st.empty()

    # Placeholder для отображения графика временного ряда
    chart_placeholder = st.empty()

    while True:
        # Обновление данных
        st.session_state.data = update_data(st.session_state.data)

        # Преобразование данных в DataFrame
        df = pd.DataFrame(st.session_state.data)

        # Отображение текущей температуры с помощью индикатора
        current_temperature = df.iloc[-1]['temperature']
        previous_temperature = df.iloc[-2]['temperature'] if len(df) > 1 else current_temperature
        temp_indicator = create_temperature_indicator(current_temperature, previous_temperature)
        current_temp_placeholder.plotly_chart(temp_indicator)

        # Создание графика временного ряда
        fig = px.line(df, x='time', y='temperature', title='История изменений', labels={'temperature': 'Температура (°C)'})
        chart_placeholder.plotly_chart(fig)

        # Пауза на 10 секунд
        time.sleep(3)

if __name__ == "__main__":
    main()
