FROM python:3.10-slim

WORKDIR /app

COPY . .

# RUN python3 -m venv /opt/venv

# COPY ./requirements.txt /app/requirements.txt
# RUN . /opt/venv/bin/activate && pip install -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]