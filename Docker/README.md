## :shipit: CITY-ZIP-WEATHER MICROSERVICES: :shipit:

**1.	Build image from city-to-zip python file, then run a container from this image.**

        •	$ docker build -t city-to-zip .

<img width="503" alt="build image 1" src="https://user-images.githubusercontent.com/113223572/217951707-f808ee0f-9332-49ff-98c9-204cbe28d377.png">

<img width="1382" alt="image 1" src="https://user-images.githubusercontent.com/113223572/217951924-48eec8a1-f036-48bb-b719-fcd508c8985e.png">

          •	$ docker run --name city-zip-container -p 8000:8000 city-to-zip

<img width="503" alt="image 1 to container" src="https://user-images.githubusercontent.com/113223572/217951943-79ae4a08-6ff4-448d-a597-ce217b3d38c1.png">

<img width="1382" alt="Container1" src="https://user-images.githubusercontent.com/113223572/217951848-dca63677-9032-453a-86e5-ca605611beb9.png">

**2.	Build image from zip-to-weather python file, then run a container from this image.**

        •	$ docker build -t zip-to-weather .

<img width="498" alt="build image 2" src="https://user-images.githubusercontent.com/113223572/217952026-08165725-1906-42c6-b7bf-07c5ffdd3462.png">

        •	$ docker run --name zip-weather-container -p 8001:8001 zip-to-weather

<img width="498" alt="image 2 to container" src="https://user-images.githubusercontent.com/113223572/217952042-b798e8a7-fe45-4fb7-93dd-2fa1aa095952.png">

<img width="1382" alt="截屏2023-02-09 13 12 05" src="https://user-images.githubusercontent.com/113223572/217952062-32d059cc-40ad-4960-bed6-29a4ebd8b213.png">

**3.  Create network and add containers to network.**

        •	$ docker network create city-weather-network
        •	$ docker network ls
        •	$ docker network connect city-weather-network city-zip-container
        •	$ docker network connect city-weather-network zip-weather-container

<img width="498" alt="截屏2023-02-09 13 13 57" src="https://user-images.githubusercontent.com/113223572/217952163-502fea00-a908-466e-a756-6eecdd805e31.png">

<img width="835" alt="截屏2023-02-09 13 15 36" src="https://user-images.githubusercontent.com/113223572/217952179-9bae95bc-687d-49fc-a222-8b2b140103d3.png">

**4.  Check with browser and curl.**

        •	check 127.0.0.1.8000/cityzip?city=Fresno
        •	check 127.0.0.1.8001/zipweather?zip_code=95133
        •	$ curl "http://127.0.0.1:8000/cityzip?c/ity=Fresno"
        •	$ curl "http://127.0.0.1:8000/zipweather?zip_code=10011"

<img width="1524" alt="截屏2023-02-09 13 38 11" src="https://user-images.githubusercontent.com/113223572/217952283-6a9f0df5-7e2f-4a07-9a7f-f6b10a444106.png">

<img width="1524" alt="截屏2023-02-09 13 38 42" src="https://user-images.githubusercontent.com/113223572/217952294-04b7a09c-0b87-4cd6-84db-b1f6a4c813b2.png">

<img width="673" alt="截屏2023-02-09 13 41 52" src="https://user-images.githubusercontent.com/113223572/217952311-93c3bf62-d80b-4dbe-90df-7446340e20cc.png">

