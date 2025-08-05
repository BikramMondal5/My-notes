# Write code of custom exception handling to open a file which does not exists in the given path.

class FileFormatError(Exception):
    pass

class ConfigError(Exception):
    def __init__(self, message="A custom error occurred"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"Custom Error: {self.message}"
    pass

def read_config(filename):
    try:
        with open(filename, "r") as f:
            content = f.read()
            
        if not content.strip().startswith("[CONFIG]"):
            raise FileFormatError(
                "Invalid config file format")
        
    except FileNotFoundError:
        raise ConfigError("Config file not found")
    except FileFormatError as e:
        raise ConfigError(f"Format error: {e}")

if __name__ == '__main__':
    
    try:
        read_config("data.txt")
    except ConfigError as e:
        print(f"Caught an error: {e}")    