Generate dhparams
```bash
cd nginx/config
openssl dhparam -out dhparams.pem 4096
```


Generate self signed cert
```bash
cd nginx/certs
openssl genrsa > privkey.pem
openssl req -new -x509 -key privkey.pem > fullchain.pem
```


Build pyproject and docker containers
```bash
docker-compose build
```



Start up the whole thing
```bash
docker-compose up
```
