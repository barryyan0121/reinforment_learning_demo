# Run Miniconda Docker Image
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
# Debug containerized apps
Pycharm Professional Edition can be used to debug the code inside the container.

