# Форма Бэкуса-Наура календаря

календарь = событие ";" календарь | событие


![image](media/1.png)


событие = дата ":" время описание


![image](media/2.png)


дата = день месяц год


![image](media/3.png)

день = цифра цифра


![image](media/4.png)

месяц = "января" | "февраля" | "марта" | "апреля" | "мая" |
"июня" | "июля" | "августа" | "сентября" | "октября" | "ноября" |
"декабря"

год = цифра цифра цифра цифра

![image](media/6.png)

время = час ":" минута

![image](media/7.png)

час = цифра цифра

![image](media/8.png)

минута = цифра цифра

![image](media/9.png)

описание = текст

![image](media/10.png)


цифра = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"

![image](media/11.png)

текст = [буква | цифра]...[буква | цифра]

![image](media/12.png)

буква = "А" | "Б" | "В" | ... | "Я" | "а" | "б" | "в" | ... | "я" | "a" | "b" | "c" | ... | "z"

![image](media/13.png)

# Примеры программ

## Программа 1

    07 мая 2023: 14:20 обед

### Результат работы синтаксического анализатора:

![image](media/14-1.png)

![image](media/14.png)

## Программа 2

    14 марта 2023: 01:59 День числа Пи;
    01 января 2023: 00:00 Новый Год;
    02 мая 2023: 18:00 Семинар

### Результат работы синтаксического анализатора:

![image](media/15-1.png)

![image](media/15.png)

## Программа 3

        02 мая 2023: 14:20 Лекция;
        09 мая 2023: 10:00 Парад победы    

### Результат работы синтаксического анализатора:

![image](media/16-1.png)

![image](media/16.png)