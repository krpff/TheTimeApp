# TimeApp

TimeApp — это приложение, предоставляющее функциональность таймера обратного отсчета, секундомера и будильника. Приложение разработано с использованием библиотеки PyQt5 и баз данных SQLite. Приложение поддерживает настройку таймеров, сохранение будильников, а также запись промежуточных результатов секундомера.

## Особенности приложения

### Таймер обратного отсчета (Countdown)
- Установка времени обратного отсчета через интерфейс.
- Возможность паузы, сброса и возобновления таймера.
- Предустановленные значения таймера, настраиваемые через базу данных.
- Уведомление и воспроизведение звукового сигнала по окончании времени.

### Секундомер (Stopwatch)
- Старт, пауза и сброс времени.
- Запись промежуточных кругов (rounds) с сохранением времени каждого круга.
- Экспорт данных о кругах в файл CSV.

### Будильник (Alarm)
- Добавление и удаление будильников через графический интерфейс.
- Автоматическое воспроизведение звукового сигнала при срабатывании будильника.
- Удаление всех будильников одним нажатием.

## Технические детали
Приложение использует следующую архитектуру:
- **MainWindow**: Основное окно для управления всеми функциями.
- **CountDown**: Класс, отвечающий за логику таймера обратного отсчета.
- **StopWatch**: Класс для управления логикой секундомера.
- **Alarm**: Класс для работы с будильниками.

Приложение построено на библиотеке PyQt5 и использует базу данных SQLite для хранения настроек и данных будильников.

## Установка
1. Убедитесь, что у вас установлен Python версии 3.7 или выше.
2. Установите зависимости:
```bash
pip install PyQt5
```
4. Клонируйте репозиторий или скачайте исходный код.
Запустите приложение:
```bash
python main.py
```

## Использование

### 1. Таймер обратного отсчета
- Выберите время (часы, минуты, секунды) и нажмите кнопку "Старт".
- Для паузы или продолжения нажмите кнопку "Пауза".
- Для сброса времени нажмите кнопку "Сброс".
- Используйте предустановки для быстрого выбора времени.

### 2. Секундомер
- Нажмите кнопку "Старт" для запуска секундомера.
- Используйте кнопку "Круг" для записи промежуточных значений.
- Нажмите "Пауза" для остановки времени.
- Для сброса времени и списка кругов нажмите кнопку "Сброс".
- Сохраните результаты в CSV, нажав кнопку "Сохранить".

### 3. Будильник
- Установите время будильника и нажмите "Добавить".
- Удалите отдельный будильник, выбрав его и нажав "Удалить".
- Очистите весь список будильников кнопкой "Очистить".

## Структура проекта
- **main.py**: Главный файл для запуска приложения.
- **countdown.py**: Модуль логики таймера обратного отсчета.
- **stopwatch.py**: Модуль логики секундомера.
- **alarm.py**: Модуль работы с будильником.
- **data/**: Директория с ресурсами (иконки, звуки, интерфейс).
