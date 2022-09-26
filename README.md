# wttr_weather

 Это Python скрипт, который выводит в командную строку прогноз погоды на текущую дату и следующие два дня для трёх локаций: г. Лондон, Аэропорт в Шереметьево, г. Череповец. На каждую дату идёт прогноз на день и на ночь.

[Источник прогноза погоды](https://wttr.in).

## Установка

Скачать гит репозиторий.

## Требования к использованию

Требуется [Python](https://www.python.org/downloads/) версии 3.7 или выше и установленный [pip](https://pip.pypa.io/en/stable/getting-started/).
Для установки необходимых зависимостей используйте команду:
1. Для Unix/macOs: `python -m pip install -r ~/wttr_weather/requirements.txt`
2. Для Windows: `py -m pip download --destination-directory DIR -r requirements.txt`

## Использование

Запустить файл  weather.py как Python скрипт.

## Пример использования

Запуск:

`> python3 ~/wttr_weather/weather.py`

Вывод:

london

     \  /       Переменная облачность
   _ /"".-.     +15(13) °C     
     \_(   ).   ↘ 5 м/c        
     /(___(__)  10 км          
                0.3 мм         
                        ┌─────────────┐                        
┌───────────────────────┤ Пн. 26 сент.├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│      .-.      Слабая морось  │    \  /       Переменная обл…│
│     (   ).    15 °C          │  _ /"".-.     +11(9) °C      │
│    (___(__)   ↘ 6-7 м/c      │    \_(   ).   ↘ 3-5 м/c      │
│     ‘ ‘ ‘ ‘   2 км           │    /(___(__)  10 км          │
│    ‘ ‘ ‘ ‘    0.7 мм | 96%   │               0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤ Вт. 27 сент.├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│               Облачно        │  _`/"".-.     Местами дождь  │
│      .--.     16 °C          │   ,\_(   ).   +12(10) °C     │
│   .-(    ).   → 5-6 м/c      │    /(___(__)  → 3-5 м/c      │
│  (___.__)__)  10 км          │      ‘ ‘ ‘ ‘  10 км          │
│               0.0 мм | 0%    │     ‘ ‘ ‘ ‘   0.1 мм | 67%   │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤ Ср. 28 сент.├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│               Пасмурно       │    \  /       Переменная обл…│
│      .--.     +14(13) °C     │  _ /"".-.     +13(12) °C     │
│   .-(    ).   ↘ 4 м/c        │    \_(   ).   ↘ 2-3 м/c      │
│  (___.__)__)  10 км          │    /(___(__)  10 км          │
│               0.0 мм | 0%    │               0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘

Все новые фичи публикуются здесь: @igor_chubin

svo

                Пасмурно
       .--.     +9(7) °C       
    .-(    ).   → 4 м/c        
   (___.__)__)  10 км          
                0.1 мм         
                        ┌─────────────┐                        
┌───────────────────────┤ Пн. 26 сент.├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│      .-.      Слабая морось  │    \  /       Переменная обл…│
│     (   ).    +8(6) °C       │  _ /"".-.     +6(5) °C       │
│    (___(__)   → 3-4 м/c      │    \_(   ).   → 1-3 м/c      │
│     ‘ ‘ ‘ ‘   2 км           │    /(___(__)  10 км          │
│    ‘ ‘ ‘ ‘    0.5 мм | 56%   │               0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤ Вт. 27 сент.├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│    \  /       Переменная обл…│               Облачно        │
│  _ /"".-.     +11(9) °C      │      .--.     +10(8) °C      │
│    \_(   ).   ← 2-3 м/c      │   .-(    ).   ↙ 2-4 м/c      │
│    /(___(__)  10 км          │  (___.__)__)  10 км          │
│               0.0 мм | 0%    │               0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤ Ср. 28 сент.├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│      .-.      Небольшой дожд…│      .-.      Небольшой дожд…│
│     (   ).    +7(4) °C       │     (   ).    +8(7) °C       │
│    (___(__)   ↙ 4-5 м/c      │    (___(__)   ↓ 1-2 м/c      │
│     ‘ ‘ ‘ ‘   9 км           │     ‘ ‘ ‘ ‘   9 км           │
│    ‘ ‘ ‘ ‘    1.6 мм | 80%   │    ‘ ‘ ‘ ‘    0.8 мм | 53%   │
└──────────────────────────────┴──────────────────────────────┘

Все новые фичи публикуются здесь: @igor_chubin

Cherepovets

       .-.      Слабая морось
      (   ).    +8(7) °C       
     (___(__)   ↘ 2 м/c        
      ‘ ‘ ‘ ‘   2 км           
     ‘ ‘ ‘ ‘    0.4 мм         
                        ┌─────────────┐                        
┌───────────────────────┤ Пн. 26 сент.├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│      .-.      Небольшой дожд…│               Дымка          │
│     (   ).    +8(7) °C       │  _ - _ - _ -  +7(5) °C       │
│    (___(__)   ↘ 2-3 м/c      │   _ - _ - _   ↙ 2-3 м/c      │
│     ‘ ‘ ‘ ‘   9 км           │  _ - _ - _ -  2 км           │
│    ‘ ‘ ‘ ‘    1.8 мм | 95%   │               0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤ Вт. 27 сент.├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│      .-.      Слабая морось  │  _`/"".-.     Небольшой ливн…│
│     (   ).    +7(4) °C       │   ,\_(   ).   +8(5) °C       │
│    (___(__)   ← 3-4 м/c      │    /(___(__)  ← 4-6 м/c      │
│     ‘ ‘ ‘ ‘   2 км           │      ‘ ‘ ‘ ‘  10 км          │
│    ‘ ‘ ‘ ‘    0.3 мм | 70%   │     ‘ ‘ ‘ ‘   0.2 мм | 84%   │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤ Ср. 28 сент.├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│      .-.      Слабая морось  │               Пасмурно       │
│     (   ).    +8(5) °C       │      .--.     +4(0) °C       │
│    (___(__)   ← 7-10 м/c     │   .-(    ).   ↙ 6-9 м/c      │
│     ‘ ‘ ‘ ‘   2 км           │  (___.__)__)  10 км          │
│    ‘ ‘ ‘ ‘    0.2 мм | 83%   │               0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘

Все новые фичи публикуются здесь: @igor_chubin