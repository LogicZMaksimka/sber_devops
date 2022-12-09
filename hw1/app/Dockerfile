FROM python:3.9
ENV FLASK_DEBUG=True
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python3", "app.py"]