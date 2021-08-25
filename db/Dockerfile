FROM mysql

EXPOSE 3306

COPY my.cnf /etc/mysql/conf.d/
COPY init/* /docker-entrypoint-initdb.d/

CMD ["mysqld"]
