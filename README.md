# django-drf-swagger

This sample application which having example with DRF and Swagger.

## Dependency
```
Docker
```

## Run Commands
```
docker-compose build
docker-compose up -d

****Migrate database****
docker-compose run web python manage.py migrate

```

## Access URL
Open browser to 
```
localhost:8000
```

## Endpoints

1. ​/assessment​/create​/ (POST)
    

input string
   ```json
    "tags":[],
    "name":"",
    "title":"",
    "description":"",
    "type":"",
    "duration":
```
3. ​/assessment​/list (GET)
4. ​/assessment​/list?search=<tag_name> (GET)
5. ​/assessment​/view​/{id}​/ (GET)
6. ​/tags​/ (GET)
7. ​/tags​/ (POST)

input string
   ```json
    "name":""
```

8. ​/swagger​/ (GET)