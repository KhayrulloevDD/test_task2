Инструкции по разворачиванию:

- Клонируйте репозиторию https://github.com/KhayrulloevDD/test_task2.git;
- Создайте виртуальное окружение и активируйте его (необъязательно);
- Установить зависимости из файла requirements.txt (pip install -r requirements.txt);
- Запустите сервер (uvicorn main:app --reload).

Инструкции по использованию:
 - GET: http://127.0.0.1:8000/check_inn/{inn}
   
   Примеры:
   
       Запрос(GET): http://127.0.0.1:8000/check_inn/123
       Ответ:
       {
            "inn":"123",
            "inn_is_valid":false
       }
       
       Запрос(GET): http://127.0.0.1:8000/check_inn/0000000000
       Ответ:
       {
            "inn":"0000000000",
            "inn_is_valid":true
       }