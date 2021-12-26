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


# Self signing a certificate
1. Make a private key 
```bash
openssl genrsa > privkey.pem
```

2. Make a fullchain certificate in the `nginx/certs` folder
```bash
openssl req -new -x509 -addext "subjectAltName = IP:127.0.0.1,DNS:localhost" -key privkey.pem > fullchain.pem
```
*it needs to be marked as coming from a CA for update-ca-trust to accept and add it. Which is why you can't use the openssl.cnf file to change the subjectAltName, notice that IP addresses have IP: and domain names have DNS:*

3. Convert from .pem to .crt format (might not be neccecary)
```bash
openssl x509 -outform der -in fullchain.pem -out golfpin.crt
```

4. Trust the certificate 
```bash
sudo mv golfpin.crt /etc/pki/ca-trust/source/anchors/
sudo update-ca-trust extract
```
