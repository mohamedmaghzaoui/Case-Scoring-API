# Lancer le projet avec docker
```
docker build -t folder-api .
docker run -p 8000:8000 folder-api
```

# Lancer le projet sans docker
```
$ uvicorn backend:app --reload --port 8000
```