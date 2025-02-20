

### Запуск в Docker
Создать и заполнить .env файл в корне приложения (.env.example )

#### Сборка образа
docker build -t hh-bot .

#### Запуск контейнера
docker run -d --name hh-bot hh-bot
