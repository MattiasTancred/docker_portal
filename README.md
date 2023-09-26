# docker_portal
#Install Flask:

pip install Flask

#Install gunicorn

pip install gunicorn

#Install docker

docker --version

sudo apt-get update

sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io

docker --version

#Build your Docker image:

sudo docker build -t flask-app .

#Allow Docker to communicate with your X server:

xhost +local:docker

#Run your Docker container:

sudo docker run -e DISPLAY=unix$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -p 5000:5000 flask-app

/path/to/your/project
├── app.py
├── Dockerfile
├── client.py
├── requirements.txt
└── templates
    └── index.html


