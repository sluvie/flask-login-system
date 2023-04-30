docker stop ducelle-system
docker rm ducelle-system
docker image rm ducelle-system:1.0.0
docker build -t ducelle-system:1.0.0 .
docker run --name ducelle-system -d -v ducelle-volume:/app/files -p 7001:5000 ducelle-system:1.0.0