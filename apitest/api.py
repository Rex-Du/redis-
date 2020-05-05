import redis

conn = redis.Redis(host='127.0.0.1', port=6379)

print(conn.get('a'))