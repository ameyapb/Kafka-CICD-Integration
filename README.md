# Kafka-CICD-Integration

This repository provides a practical example of integrating Apache Kafka with Continuous Integration and Continuous Deployment (CI/CD) pipelines. The main goal is to showcase how to automate the creation of Kafka topics using a Python script.

To get started, ensure that you have Apache Kafka installed and a running Kafka cluster. Additionally, you'll need Python 3.x and the confluent-kafka Python package installed. The repository includes a Python script, create_kafka_topic.py, which utilizes the Confluent Kafka library to create Kafka topics.

Before executing the script, make sure to configure the required environment variables. If you're using GitLab CI/CD or a similar platform, set the environment variables KAFKA_TOPIC_NAME, KAFKA_NUM_PARTITIONS, and KAFKA_REPLICATION_FACTOR according to your desired topic configuration. Alternatively, you can manually set these variables on your system.

Once the setup is complete, run the Python script, create_kafka_topic.py, to connect to the Kafka cluster and create a topic with the specified configuration. The script utilizes the provided environment variables to determine the topic's name, number of partitions, and replication factor. You'll receive a success message once the topic is successfully created.
