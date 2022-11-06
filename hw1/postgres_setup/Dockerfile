FROM postgres:latest
ENV POSTGRES_PASSWORD=123456
ENV POSTGRES_USER=postgres
# ENV POSTGRES_DB=cacti
# ENV POSTGRES_HOST=localhost
ENV POSTGRES_PORT=5432
EXPOSE 5432
WORKDIR /postgres_setup
# COPY fill.sql /docker-entrypoint-initdb.d/create_fixtures.sql
CMD [ "bash", "run.sh" ]