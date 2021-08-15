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
2. ​/assessment​/list (GET)
3. ​/assessment​/list?search=<tag_name> (GET)
4. ​/assessment​/view​/{id}​/ (GET)
5. ​/tags​/ (GET)
6. ​/tags​/ (POST)
7. ​/swagger​/ (GET)