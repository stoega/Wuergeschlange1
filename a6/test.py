import pickle
with open(r'a6\Examples\Franz Kafka.pkl', 'rb') as f:
    data = pickle.load(f)
    print(data)
    
with open(r'a6\Franz Kafka.pkl', 'rb') as f:
    data = pickle.load(f)
    print(data)