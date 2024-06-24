FROM python:3.12
WORKDIR /diretorio
COPY /source /diretorio
CMD ["python", "hello.py"]