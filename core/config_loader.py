import yaml

class ConfigLoader:
    def __init__(self, config_path: str):
        self.config_path = config_path

    def load_config(self) -> dict:
        """
        Load YAML configuration from the specified file path.

        Returns:
            dict: Parsed configuration dictionary.
        Raises:
            FileNotFoundError, yaml.YAMLError
        """
        with open(self.config_path, 'r') as f:
            return yaml.safe_load(f)
