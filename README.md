# Application for booking parking spaces in the “Fregat office center”.

### Quick Start
To get this project up and running locally on your computer follow the following steps.
1. Set up a python virtual environment
2. Run the following commands
    * pip install -r requirements.txt
    * python manage.py makemigrations
    * python manage.py migrate
    * python manage.py createsuperuser
    * python manage.py runserver
   
3. Open a browser and go to http://localhost:8000/


## Part of Api:


## Get token

### Request

`GET api/v1/api-token-auth/`


## Get list of bookings

### Request

`GET api/v1/bookings/`

    curl -i -H 'Accept: application/json' http://localhost:8000/api/v1/bookings/

### Response

    HTTP/1.1 200 OK
    Date: Thu, 12 Dec 2021 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    [{"id":1,"owner":"","from_time":"default:10:00:00","to_time":"default:17:00:00","description":""}]


## Get a Booking with ID


### Request

`GET api/v1/bookings/<int:park_id>`

    curl -i -H 'Accept: application/json' -d 'name=Foo&status=new' http://localhost:8000/api/v1/bookings/<int:park_id>

### Response

    HTTP/1.1 200 OK
    Date: Thu, 12 Dec 2021 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    [{"id":1,"owner":"","from_time":"default:10:00:00","to_time":"default:17:00:00","description":""}]


## Create a new Booking

### Request

`POST api/v1/bookings/`

    curl  -H 'Content-Type: application/json' --data '{"owner":"","from_time":"", "to_time":""}' http://localhost:8000/api/v1/bookings/

### Response

    HTTP/1.1 201 Created
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 201 Created
    Connection: close
    Content-Type: application/json
    Location: /thing/1
    Content-Length: 36

    {"id":1,"owner":"","from_time":"default:10:00:00","to_time":"default:17:00:00","description":""}
