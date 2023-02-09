# Dockerfile for zip code to weather server
FROM python:3.8
WORKDIR /app
COPY . .
RUN pip install Flask
RUN pip install requests
EXPOSE 8000
CMD ["python", "city_to_zipcode.py"]