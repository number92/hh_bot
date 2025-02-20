

### Запуск в Docker
Создать и заполнить .env файл в корне приложения (.env.example )

#### Сборка образа
docker build -t my-telegram-bot .

#### Запуск контейнера
docker run -d --name my-telegram-bot-container my-telegram-bot
