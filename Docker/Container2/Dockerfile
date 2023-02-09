# Dockerfile for city to zip code server
FROM python:3.8
WORKDIR /app
COPY . .
RUN pip install requests
RUN pip install Flask
EXPOSE 8001
CMD ["python", "zipcode_to_weather.py"]