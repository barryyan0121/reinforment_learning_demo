# Dockerized Python and Miniconda

## Run Miniconda Docker Image

1. Build the image locally using the Dockerfile

```bash
docker image build -t miniconda .
```

2. Run the image

```bash
docker container run -it miniconda /bin/zsh
```

3. Check the PYPI and python version

```bash
pip --version
python --version
```

## Debug containerized apps

### Using Pycharm Professional Edition

Pycharm Professional Edition can be used to debug the code inside the container. It can also use the interpreter inside the container (Python, Conda, Virtualenv) to lint the code. You can choose to pull the image from the Docker Hub or build the image locally everytime the code is changed.

### Using Visual Studio Code

Visual Studio Code can be used to debug the code inside the container. It does not support the interpreter inside the container (Python, Conda, Virtualenv) to lint the code. To use the debugger, you need to specify *task.json* and *launch.json* files. You can use *Docker: Initialize for Docker Debugging* to generate these files and then modify them to suit your needs. A sample *task.json* and *launch.json* files are provided in the repository.
