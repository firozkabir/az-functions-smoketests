# Azure Functions 
There are three `HttpTrigger` functions in this functions app: 
* `/api/httpBasic`
* `/api/httpIp`
* `/api/httpOracle`


# How to invoke: 
* All functions use `authLevel: anonymous`. So they can be called by anyone.
* Call httpBasic as `https://<function-app-url>/api/httpBase?sisid=<any-number>` to get a response like `{"sisid": "<any-number>"}`
* Call httpIp as `https://<function-app-url>/api/httpIp?sisid=<any-number>` to get a response like `{"sisid": "<any-number>", "ip": "<public-ip-of-server>"}`
* Call httpOracle as `https://<function-app-url>/api/httpBase?sisid=<any-number>` to get a response like `{"sisid": "<any-number>", "version": "<Oracle Database Version>"}`


# What is happening inside: 
* httpBasic is simply taking the sisid parameter passing it to response
* httpIp is calling https://icanhazip.com and returing it in response along with sisid parameter supplied in the request
* httpOracle does the same as httpBasic. Only it also connects to an Oracle database and returns its version in the response. This is to validate your function app can connect to the database.


# Build Instructions: 
* Application expects following to be saved in keyvault: 
    - key: `func-db-username`, secret: `<database username>` 
    - key: `func-db-password`, secret: `<database password>`
    - key: `func-db-host`, secret: `<database host name or ip>`
    - key: `func-db-port`, secret: `<database port>`
    - key: `func-db-sid`, secret: `<database SID or service name>` 
* Once above have been saved in a keyvault, configure a Service Principal (SPN) to read from it 
* You'll need to provide `client-id`, `tenant-id` and `client-secret` from the SPN as well as `keyvault-name` as build arguments: 

```bash
docker build --tag <DOCKER_ID>/eip-smoketest-2022:latest \
--no-cache --build-arg CLIENT_ID="<client-id>" \
--build-arg  TENANT_ID="<tenant-id>" \
--build-arg  CLIENT_SECRET="<client-secret>" \
--build-arg  KEYVAULT_NAME="<keyvault-name>" . 
```

* This means credentials needed to get to the keyvault are only used during compilation. Natuarally, the image will have to be re-built if keyvault credentials change. 

* Please note the program assumes they keyvault is accessed via `https://<keyvault-name>.vault.azure.net` 