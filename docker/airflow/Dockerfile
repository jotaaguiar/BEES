FROM apache/airflow:2.7.2-python3.10

USER root
RUN apt-get update && apt-get install -y default-jdk

USER airflow
RUN pip install --upgrade pip && \
    pip install requests pyspark pandas pytest

ENV JAVA_HOME=/usr/lib/jvm/default-java
ENV PATH=$JAVA_HOME/bin:$PATH
