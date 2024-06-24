FROM python:3.12
WORKDIR /diretorio
COPY /requirements.txt .
COPY /source /diretorio
EXPOSE 8000
RUN python -m pip install -r requirements.txt
CMD ["fastapi", "dev", "main.py",  "--port", "8000", "--host", "0.0.0.0"]