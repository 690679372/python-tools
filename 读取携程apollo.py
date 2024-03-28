from pyapollos import ApolloClient

# 初始化Apollo客户端
apollo_client = ApolloClient(
    app_id="your_app_id",  # 替换为你的应用ID
    cluster='YOUR_CLUSTER',  # 替换为你的集群名称，如'PROD'或'TEST'
    config_server_url="http://your_apollo_server:8080",  # 替换为你的Apollo配置服务器地址
)

# 获取某个特定namespace下的key值
value1 = apollo_client.get_value('key1', namespace='application')

# 如果要读取非k-v格式的私有namespace（例如模拟读取文本文件内容）
value2 = apollo_client.get_value('content', namespace='test.txt')

print(value1)
print(value2)
