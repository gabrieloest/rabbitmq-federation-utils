import yaml

CONFIG_PATH = "./config/config.yml"


class ConfigResolver:

    def __init__(self, logger):
        self.log = logger

    def log_configurations(self, configurations):
        for key, value in configurations.items():
            self.log.info('{}: {}'.format(key, value))

    def load_server_config(self, cluster_name):
        self.log.info('Loading server configurations....')
        with open(CONFIG_PATH, 'r') as ymlfile:
            server_config = yaml.load(ymlfile)

        rabbitmq = server_config['rabbitmq-{}'.format(cluster_name)]
        rabbitmq['vhost'] = rabbitmq['vhost'].replace("/", "%2f")
        self.log_configurations(rabbitmq)

        return rabbitmq
