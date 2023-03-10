FROM apache/airflow:2.2.3-python3.8

USER root

WORKDIR /app

# Instale as dependências do Docker Compose
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        docker-compose

# Copie o arquivo docker-compose.yml para o diretório de trabalho
COPY docker-compose.yml .

# Defina a variável de ambiente AIRFLOW_HOME
ENV AIRFLOW_HOME=/app

# Exponha as portas padrão do Airflow
EXPOSE 8080 5555 8793

# Inicie o Airflow usando o Docker Compose
CMD ["docker-compose", "up"]
