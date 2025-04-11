# Анализ журнала логирования

## Описание: 
Приложение, анализирует логи django-приложения и формирует отчеты. 
Отчет выводится в консоль. 

## Интерфейс приложения:
1. можно передать пути к логам, файлов может быть несколько
2. можно указать аргумент --report c названием отчета который нужно сформировать


## Использование:
### Пример:
1. В терминале введите команду формирования отчёта:
```commandline
python main.py logs/app1.log logs/app2.log logs/app3.log --report handlers
```
    Ожидаемый результат:

    HANDLERS            DEBUG               INFO                WARNING             ERROR               CRITICAL            
    /admin/dashboard/   0                   13                  0                   4                   0
    /admin/login/       0                   12                  0                   4                   0
    /api/v1/auth/login/ 0                   12                  0                   2                   0
    /api/v1/cart/       0                   9                   0                   1                   0
    /api/v1/checkout/   0                   15                  0                   4                   0
    /api/v1/orders/     0                   10                  0                   4                   0
    /api/v1/payments/   0                   12                  0                   2                   0
    /api/v1/products/   0                   12                  0                   5                   0
    /api/v1/reviews/    0                   20                  0                   4                   0
    /api/v1/shipping/   0                   8                   0                   3                   0
    /api/v1/support/    0                   16                  0                   4                   0
    /api/v1/users/      0                   9                   0                   3                   0
    ________________________________________________________________________________________________________________________
                        0                   148                 0                   40                  0
    Total requests: 188


## Создание нового отчёта:
Необходимо создать новый метод в классе ``` class AnalyzeLogs ``` [analyze_logs.py](log_analysis%2Fanalyze_logs.py)
В самом методе необходимо наследовать метод ``` def report_generation(path_file, pattern_filter, pattern_sorted) ``` 
родительского класса ``` class ParentAnalyzeLogs ``` [parent_analyze_logs.py](log_analysis%2Fparent_analyze_logs.py)
### Параметры
1. path_file (путь до файла с логами)
2. pattern_filter (указываем строку, по которой мы отфильтруем нужные логи)
3. pattern_sorted (указываем строку, для сортировки и группировки отфильтрованных логов)