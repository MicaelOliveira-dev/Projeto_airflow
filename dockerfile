FROM ubuntu:20.04

# Instala as dependências do Airflow
RUN apt-get update && \
    apt-get install --no-install-recommends -y python3-pip && \
    pip3 install --no-cache-dir -U pip setuptools wheel && \
    pip3 install --no-cache-dir apache-airflow==2.3.2

# Define o diretório de trabalho
WORKDIR /projeto-airflow

# Copia o conteúdo do diretório atual para o diretório de trabalho
COPY . .

# Define a variável de ambiente AIRFLOW_HOME
ENV AIRFLOW_HOME=/projeto-airflow

# Inicializa o banco de dados do Airflow
RUN airflow db init

# Cria um usuário administrador
RUN airflow users create \
    --username admin \
    --password admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com

# Define o comando padrão para executar o servidor da Web do Airflow
CMD ["airflow", "webserver", "-p", "8080"]

