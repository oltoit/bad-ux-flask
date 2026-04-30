FROM python:3.12-slim

WORKDIR /app

# Install dependencies
COPY src/requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN rm requirements.txt

RUN pip install gunicorn

COPY src/ .

EXPOSE 8080
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "app:app"]