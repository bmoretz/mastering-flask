docker stop dev
docker rm dev

docker build -t chapter_1 .

docker run --name dev -p 5000:5000 -i -t chapter_1