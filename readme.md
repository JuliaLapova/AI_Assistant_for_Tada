![image](https://github.com/user-attachments/assets/d553ab23-de56-48cd-a28a-876c001a2f78)

# Видео с награждением
Мы на 33 минуте - https://www.youtube.com/watch?v=lajwW6AF274

[![License][license-shield]][license-url]
[![Github][github-shield]][github-url]



# Описание проекта
![image](https://github.com/user-attachments/assets/0cc5abe3-5a14-46e4-8924-258bb0c745bb)



Умный корпоративный ассистент, который помогает быстро находить специализированную информацию по заранее определенным тематикам.

Пример взаимодействи с нашим АПИ можно посмотреть [здесь][demo-url-front].

## Основные возможности
АПИ чат-бота для корпоративного чата, который позволяет:
* Получать ответы на определенную тематику
* Добавлять источники информации
* Добавлять ответы на часто задаваемые вопросы
* Управлять доступом к боту и базой знаний

## Структура проекта
![image](https://github.com/user-attachments/assets/2a92279c-8396-4430-8372-2a7cf75335d8)


Проект состоит из 3-х частей:

<details>
  <summary><b><strong>АПИ</strong></b></summary>
  
  FastAPI приложение, которое предоставляет доступ к боту и базе знаний. 
    Приложение состоит из 3-х частей:

* АПИ чат-бота (простой и расширенный)
* АПИ базы знаний (добавление индексов)
* АПИ для администрирования проекта

</details>
<details>
  <summary><b><strong>База данных</strong></b></summary>
  
PostgreSQL база данных, которая хранит:
  * Информацию о компаниях
  * Информацию о ключах к АПИ
  * Информацию о запросах пользователей
  * Правила фильтрации запросов

</details>

<details>
  <summary><b><strong>База знаний</strong></b></summary>
  
  В базе знаний хранятся индексы:
  * Индекс для поиска ответов на вопросы, связанные с ТК
  * Индекс для поиска ответов на общие вопросы по бизнесу
  * Индекс для поиска ответов на вопросы, связанные с уплатой налогов
  * Индекс для поиска ответов на вопросы, связанные с бухучетом

</details>

Сборка проекта осуществляется с помощью `docker-compose`.

## Используемые технологии

В проекте используются следующие технологии:

* [![Python][python]][python-url]
* [![Fastapi][Fastapi]][Fastapi-url]
* [![Docker][Docker]][Docker-url]


## Веб-интерфейс пользователя

Пример интерфейса пользователя:


<details>
  <summary>Примечание</summary>
  
  В данный момент веб-интерфейс находится в разработке.
</details>


## Работа с API

<details>
  <summary>Интерфейс</summary>

  АПИ доступно по адресу `http://localhost:8000/docs`

  ![img][product-screenshot2]
</details>

<details>
  <summary>Документация</summary>

  Документация доступна по адресу `http://localhost:8000/redoc`
  
  ![img][product-screenshot3]
</details>

<details>
  <summary>Примеры запросов</summary>

1. HTTP запрос

    ```bash
    http://localhost:8000/api/chatbot_simple/1
    ```
   Параметры:
    * `user_input` - вопрос пользователя
    * `params` - параметры запроса
    * `api_key` - ключ для доступа к АПИ

    ```json
    {
      "user_input": "Что такое НДФЛ?",
      "question": {
        "api_key": "API_KEY"
      }
    }
   ```
2. CURL запрос

    ```bash
        curl -X 'POST' \
          'http://localhost:8000/api/chatbot_simple/1' \
          -H 'accept: application/json' \
          -H 'Content-Type: application/json' \
          -d '{
          "user_input": "Что такое НДФЛ?",
          "question": {
            "api_key": "API_KEY"
          }
        }'
    ```

</details>

## Запуск проекта

Для запуска проекта необходимо:
1. Склонировать репозиторий
2. Перейти в папку проекта
3. Создать переменную окружения `OPENAI_API_KEY`
4. Создать папку для логов `sudo mkdir -m777 -p logs/fastapi`
5. Запустить проект с помощью команды `docker-compose up --build`
6. Перейти на `localhost:8000` для входа в веб-интерфейс

## Запуск АПИ без базы знаний и базы данных
```bash
docker run -d -p 8000:8000 -e OPENAI_API_KEY={your_key} --name smart_assistant smart_assistant
```

## Запуск без докера
1. Установить зависимости
```bash
pip install -r fastapi_app/requirements.txt
```
2. Запустить проект
```bash
cd fastapi_app
uvicorn fastapi_app.fastapp:app --reload --port 9000 --env-file config.env
```
где `config.env` - файл с переменными окружения:
```bash
OPENAI_API_KEY={your_key}
DEBUG=True
```

## Лицензия

Распространяется под лицензией [APACHE][license-url].

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[license-shield]: https://img.shields.io/badge/License-APACHE-yellow.svg?style=for-the-badge
[license-url]: https://github.com/CyberMaryVer/ai_assistant/blob/main/LICENSE
[product-logo]: images/logo.jpg
[demo-url]: http://178.170.196.101:8080/
[product-screenshot1]: images/landing.jpg
[product-screenshot2]: images/api.jpg
[product-screenshot3]: images/docs.jpg
[product-screenshot4]: images/front.jpg
[product-schema]: images/architecture.png
[Fastapi]: https://img.shields.io/badge/Fastapi-0.68.1-blue?style=for-the-badge
[Fastapi-url]: https://fastapi.tiangolo.com/
[PostgreSQL]: https://img.shields.io/badge/PostgreSQL-13.3-blue?style=for-the-badge
[PostgreSQL-url]: https://www.postgresql.org/
[Docker]: https://img.shields.io/badge/Docker-20.10.7-blue?style=for-the-badge
[Docker-url]: https://www.docker.com/
[python]: https://img.shields.io/badge/Python-3.9.6-blue?style=for-the-badge
[python-url]: https://www.python.org/
[github-shield]: https://img.shields.io/badge/Github-000000?style=for-the-badge&logo=github&logoColor=white
[github-url]: https://github.com/CyberMaryVer/ai_assistant
[linkedin-shield]: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
[linkedin-url]: https://www.linkedin.com/in/maria-startseva/
[demo-url-front]: https://cybermaryver-simple-front-for-chatbot-app-0tqyzf.streamlit.app/

## Презентация

![image](https://github.com/user-attachments/assets/2be7e3f5-de7c-4ee5-9eaa-8f18dd51e053)
![image](https://github.com/user-attachments/assets/5d8c47dd-1a2b-4c08-80df-8e7aae2ae97a)
![image](https://github.com/user-attachments/assets/134de769-8808-453b-97b7-8df8c6145ae3)
![image](https://github.com/user-attachments/assets/1d4bef05-4826-4e1a-8a02-384f97dfd168)
![image](https://github.com/user-attachments/assets/22d3c880-40b7-4e2c-b83c-dee787be29dc)
![image](https://github.com/user-attachments/assets/87efdc14-f03c-4095-b6b4-035e03a34220)
![image](https://github.com/user-attachments/assets/606461f6-739a-495f-9680-6a77552fe3ce)
![image](https://github.com/user-attachments/assets/a495b4d0-2a0b-4971-8177-9c5cedb4fe9c)
![image](https://github.com/user-attachments/assets/9cc3e62f-d785-4bb4-9e96-5d1c46df5137)
![image](https://github.com/user-attachments/assets/e55d6cf6-1dfe-4bbe-8837-926f73560630)
![image](https://github.com/user-attachments/assets/aad58b6a-dc0c-45cf-9883-ab4418a42194)
![image](https://github.com/user-attachments/assets/d70caf06-90ca-4b1d-b859-f5d24b794b01)
![image](https://github.com/user-attachments/assets/153b9106-91be-434d-8f21-c2f4cedaad15)
![image](https://github.com/user-attachments/assets/65ad8a47-6483-4bd3-930a-ecbac4c3480f)
![image](https://github.com/user-attachments/assets/b6cbe7fc-5f56-4a73-bb10-dcd6c10e93b5)
![image](https://github.com/user-attachments/assets/ce4c3842-5eae-4fcb-b562-c8469dae98a8)
![image](https://github.com/user-attachments/assets/ec9e656f-063e-4589-b770-2f8af6d3ed26)
![image](https://github.com/user-attachments/assets/ad43ea87-6adc-4a03-911d-b8fd88834702)
![image](https://github.com/user-attachments/assets/68f95c0b-4013-4a30-aeaf-5903b8e000e7)
![image](https://github.com/user-attachments/assets/34bbde24-d3fc-4c40-8f11-069150c2182c)






