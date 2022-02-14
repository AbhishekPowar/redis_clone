import utils
from collections import defaultdict
from dataclasses import dataclass

index_dict = defaultdict(dict)


@dataclass
class Redis_value():
    value: str
    metadata: dict

    def get_dict(self):
        return self.__dict__

    @classmethod
    def load_dict(cls, json_data: dict):
        if 'value' not in json_data:
            raise Exception('Json schema error')
        return cls.__new__(value=json_data.get('value'), metadata=json_data.get('metadata', {}))


class Redis_service():
    def __init__(self, index: str = "index", config={}) -> None:
        self.index = index
        self.config = config
        self.filename = f"data/{self.index}.json"

        if self.config.get('load_file', False):
            self.cache = utils.read_file_as_json(filename=self.filename)
        else:
            self.cache = index_dict["index"]

    def set(self, key, value):
        expiry = self.config.get('expiry', -1)
        metadata = {}

        metadata['ttl'] = expiry if expiry == - \
            1 else utils.get_cur_epoch() + expiry

        self.cache[key] = Redis_value(
            value=value, metadata=metadata).get_dict()

        if self.config.get('persist', False):
            utils.write_obj_to_file(filename=self.filename, obj=self.cache)

        return True

    def get(self, key):
        redis_value = self.cache.get(key, {})
        ttl = redis_value.get('metadata', {}).get('ttl', -1)
        if ttl > 0:
            # if value is expired
            if ttl < utils.get_cur_epoch():
                self.remove(key)
                return None

        return redis_value.get('value')

    def remove(self, key):

        value = None
        if key in self.cache:
            value = self.cache.pop(key)
            if self.config.get('persist', False):
                utils.write_obj_to_file(filename=self.filename, obj=self.cache)
        return value

    def get_all(self):
        return self.cache
