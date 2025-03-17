

### Запуск в Docker
Создать и заполнить .env файл в корне приложения (.env.example )

### Удаление предыдущей версии
`sudo docker rm -f hh-bot && sudo docker rmi -f hh-bot`


#### Сборка образа
`sudo docker build -t hh-bot .`

#### Запуск контейнера
`sudo docker run --env-file .env -d --name hh-bot hh-bot`
