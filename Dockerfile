FROM python:3.6
RUN pip install -U Flask
WORKDIR /app
COPY app /app
EXPOSE 8080
CMD ["python", "app.py"]
