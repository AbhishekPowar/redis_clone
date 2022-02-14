import imp
import json

def read_file_as_json(filename):
    with open(filename, 'r') as f:
        s = f.read()
    return json.loads(s)

def read_file_as_text(filename):
    with open(filename, 'r') as f:
        s = f.read()
    return s

def write_obj_to_file(filename, obj):
    s = json.dumps(obj)
    with open(filename, 'w') as f:
       f.write(s)

def write_text_to_file(filename, text):
    with open(filename, 'w') as f:
        f.write(text)

def get_cur_epoch():
    from datetime import datetime
    return int(datetime.now().timestamp())
