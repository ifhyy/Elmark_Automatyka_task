# Elmark_Automatyka_task
Rest API for Elmark Automatyka recruitment task. FastAPI was chosen as a main framework as it is a good solution for REST API development and Mongodb interaction.
Author: Artem Stupak
## Setup instructions
1. Clone this repository using git clone
```shell
git clone https://github.com/ifhyy/Elmark_Automatyka_task.git
cd Elmark_Automatyka_task
```
2. Configure application by creating .env file based on provided .env.example
```shell
MONGODB_URI="mongodb+srv://rekrutacja:BZijŌwEru0oELxT@cluster11.yxu8n2k.mongodb.net/"
DB_NAME='ARTEM_STUPAK'
```
3. Build docker image by running
```shell
docker build -t elmark_task .
```
4. Run docker container
```shell
docker run -d -p 7777:8000 elmark_task
```

## API documentation
Fastapi genuinely provides automatically-generated documentation by Swagger.
```shell
http://localhost:7777/docs#
```

