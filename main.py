from redis_client import Redis_client

if __name__ == "__main__":
    redis = Redis_client(host='http://localhost', port=5000, index='index')
    redis.set(key='name', value='Abhishek')
    redis.get(key='name')
    redis.remove(key='name')
    redis.get(key='name')
