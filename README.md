

## Running with Docker

- A sample Dockerfile and a docker-compose is provided to run the application in an isolated environment
- Make sure you have `docker` and `docker-compose` installed and that the Docker daemon is running
- Build `docker-compose build`
- Run the container: `docker-compose up`
- Start making some requests: `http://localhost:8000/client/`


## Project Structure Notes

- There are one django app installed `SampleAPI`
- Django is used as a RESTful API, no html rendering is required

Project structure:
```
.
├── README.md
├── manage.py
├── requirements.txt
|── test.py
└── SampleAPI(App Folder)
```
REQUEST

POST http://localhost:8000/Client/


```json
{       "name": "himanshu",
        "contact_number" : 555555,
        "contact_email" : "himanshu4@gmail.com",
        "status": True
        }
```
RESPONSE
```json
   
{
  "id": 16,
  "contact_number": 555555,
  "name": "himanshu",
  "contact_email": "himanshu4@gmail.com",
  "status": true
}
```

REQUEST

GET http://localhost:8000/Client/

RESPONSE
```json
[
{
  "id": 1,
  "contact_number": 97824525,
  "name": "",
  "contact_email": "himasu@gmail.com",
  "status": true
},
{
  "id": 2,
  "contact_number": 978245525,
  "name": "himaaaaa",
  "contact_email": "higmasu@gmail.com",
  "status": true
},
{
  "id": 3,
  "contact_number": 9782455254,
  "name": "dfdth",
  "contact_email": "higma4su@gmail.com",
  "status": true
}
]
```

REQUEST
```json
{
   "name": "Agarwal"
}

PUT http://localhost:8000/Client/2 

RESPONSE
```json
{
  "id": 2,
  "contact_number": 978245525,
  "name": "Agarwal",
  "contact_email": "higmasu@gmail.com",
  "status": true
}
```

REQUEST

GET http://localhost:8000/Client/3 

RESPONSE
```json
{
  "id": 3,
  "contact_number": 9782455254,
  "name": "dfdth",
  "contact_email": "higma4su@gmail.com",
  "status": true
}
```

REQUEST

delete http://localhost:8000/Client/3 

RESPONSE
```json
{}
 
# I don't have GIT installed in on my persoanl computer so there is no GIT history
