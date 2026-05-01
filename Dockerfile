# 1. Python base image
FROM python:3.9-slim

# 2. Work directory set karein
WORKDIR /app

# 3. Files copy karein
COPY . /app

# Pip ko upgrade karein taake installation smooth ho
RUN pip install --upgrade pip
# 4. Libraries install karein
RUN pip install -r requirements.txt


# 5. App run karein
CMD ["python", "app.py"]