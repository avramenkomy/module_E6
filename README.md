1. Проект доступен по публиному IP-адресу http://146.185.243.15
2. При запросе по данной ссылке увидите приветственное "Hello"
    3. Для расчета числа Фиббоначчи через слэш передаем параметр - k-oe число: http://146.185.243.15/<int:k> (например, http://146.185.243.15/25 и страница вернет 121393)
4. Клонировать проект
5. Из папки с проектом запустить docker-compose build
6. Здесь же запустить docker-compose up
7. Теперь на локальном сервере 0.0.0.0:8081 доступно приветственное "Hello", а при передаче через слэш (0.0.0.0:8081/\<int:k\>) числа k - страница вернет значение числа Фиббоначчи
