import os
from confluent_kafka.admin import AdminClient, NewTopic

def create_topic(topic_name, num_partitions, replication_factor, bootstrap_servers):
    # Set up the AdminClient with Kafka bootstrap servers
    admin_client = AdminClient({'bootstrap.servers': bootstrap_servers})

    # Create a NewTopic object with the desired configuration
    topic = NewTopic(topic_name, num_partitions, replication_factor)

    # Create the topic using the AdminClient
    admin_client.create_topics([topic])

    # Confirm successful creation
    print(f"Topic '{topic_name}' created successfully.")

# GitLab CI/CD environment variables
gitlab_ci_env = os.environ

# Configuration for Kafka cluster
bootstrap_servers = 'localhost:9092'

# Kafka topic creation parameters
topic_name = gitlab_ci_env.get('KAFKA_TOPIC_NAME', 'my_topic')
num_partitions = int(gitlab_ci_env.get('KAFKA_NUM_PARTITIONS', '3'))
replication_factor = int(gitlab_ci_env.get('KAFKA_REPLICATION_FACTOR', '1'))

# Create the Kafka topic
create_topic(topic_name, num_partitions, replication_factor, bootstrap_servers)
