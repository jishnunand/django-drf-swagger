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

1. /api/v1​/assessment​/create​/ (POST)
    

input string
   ```json
    "tags":[],
    "name":"",
    "title":"",
    "description":"",
    "type":"",
    "duration":
```
2. /api/v1​/assessment​/list (GET)
3. /api/v1​/assessment​/list?search=<tag_name> (GET)
4. /api/v1​/assessment​/view​/{id}​/ (GET)
5. /api/v1​/tags​/ (GET)
6. /api/v1​/tags​/ (POST)

input string
   ```json
    "name":""
```

7. ​/swagger​/ (GET)