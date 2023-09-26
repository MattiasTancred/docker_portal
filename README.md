# docker_portal
#Build your Docker image:
/n
sudo docker build -t flask-app .

#Allow Docker to communicate with your X server:
xhost +local:docker

#Run your Docker container:
sudo docker run -e DISPLAY=unix$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -p 5000:5000 flask-app
