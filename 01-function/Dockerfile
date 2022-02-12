# To enable ssh & remote debugging on app service change the base image to the one below
#FROM mcr.microsoft.com/azure-functions/python:3.0-python3.9-appservice
FROM mcr.microsoft.com/azure-functions/python:3.0-python3.9

# installing oracle libraries
RUN apt-get update && apt-get install -y libaio1 wget unzip
WORKDIR /opt/oracle
RUN wget https://download.oracle.com/otn_software/linux/instantclient/instantclient-basiclite-linuxx64.zip && \
    unzip instantclient-basiclite-linuxx64.zip && rm -f instantclient-basiclite-linuxx64.zip && \
    cd /opt/oracle/instantclient* && rm -f *jdbc* *occi* *mysql* *README *jar uidrvci genezi adrci && \
    echo /opt/oracle/instantclient* > /etc/ld.so.conf.d/oracle-instantclient.conf && ldconfig
RUN python -m pip install cx_Oracle


# back to what was in azure functions
ENV AzureWebJobsScriptRoot=/home/site/wwwroot \
    AzureFunctionsJobHost__Logging__Console__IsEnabled=true


COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY . /home/site/wwwroot


ARG CLIENT_ID
ARG TENANT_ID
ARG CLIENT_SECRET
ARG KEYVAULT_NAME

ENV CLIENT_ID=${CLIENT_ID}
ENV TENANT_ID=${TENANT_ID}
ENV CLIENT_SECRET=${CLIENT_SECRET}
ENV KEYVAULT_NAME=${KEYVAULT_NAME}


