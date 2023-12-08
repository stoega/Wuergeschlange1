import datetime
import pickle
import os


def write_log(log_file: str, msg: str):
    with open(f"a6/{log_file}", 'a') as f:
        f.write(msg)


def create_user(name: str, data: str, password: str, log_file: str = 'logs.txt'):
    user = {'name': name, 'data': data,
            'password': password, 'last_changed': datetime.datetime.now()}

    file_path = f"a6/{name}.pkl"
    log_msg = ''
    if os.path.isfile(file_path):
        log_msg = f"Attempted creation of existing user {name} at {datetime.datetime.now()}\n"
    else:
        with open(file_path, 'wb') as f:
            pickle.dump(user, f)
        log_msg = f"Created user {name} at {datetime.datetime.now()}\n"

    write_log(log_file, log_msg)


def login(name: str, password: str, log_file: str = 'logs.txt'):
    write_log(log_file, f'Attempted login for user {name} at {datetime.datetime.now()}\n')

    file_path = f'a6/{name}.pkl'
    if not os.path.isfile(file_path):
        write_log(
            log_file, f'Attempted login for non-existing user {name} at {datetime.datetime.now()}\n')
        return None

    with open(file_path, 'rb') as f:
        content = pickle.load(f)
        data = None
        log_msg = ''

        if content['password'] == password:
            log_msg = f'Login successful for user {name} at {datetime.datetime.now()}\n'
            data = content['data']
        else:
            log_msg = f'Login failed for user {name} at {datetime.datetime.now()}\n'

        write_log(log_file, log_msg)

    return data


def change_password(name: str, old_password: str,
                    new_password: str, log_file: str = 'logs.txt'):
    time = datetime.datetime.now()
    msg_end = f"user {name} at {time}\n"
    file_path = f'a6/{name}.pkl'
    
    write_log(log_file, f'Attempted password change for {msg_end}')
    
    with open(file_path, 'rb') as f:
        content = pickle.load(f)
        if content['password'] == old_password:
            content['password'] = new_password
            content['last_changed'] = time
            log_msg = f"Password change successful for "
        else:
            log_msg = f"Password change failed for "

    write_log(log_file, log_msg + msg_end)
    


# if os.path.isfile('a6/Franz Kafka.pkl'):
#     os.remove('a6/Franz Kafka.pkl')
# if os.path.isfile('a6/H. P. Lovecraft.pkl'):
#     os.remove('a6/H. P. Lovecraft.pkl')
# if os.path.isfile('a6/William Golding.pkl'):
#     os.remove('a6/William Golding.pkl')
# if os.path.isfile('a6/George Orwell.pkl'):
#     os.remove('a6/George Orwell.pkl')
# if os.path.isfile('a6/logs.txt'):
#     os.remove('a6/logs.txt')


# create_user('Franz Kafka', 'Die Verwandlung', 'fkafka')
# create_user('H. P. Lovecraft', 'The Call of Cthulhu', 'lcrft')
# create_user('William Golding', 'Lord of the Flies', 'password')
# create_user('George Orwell', '1984', 'orwell1948')
# print(login('Franz Kafka', 'fkafks'))
# print(login('Franz Kafka', 'fkafka'))
# print(login('H. P. Lovecraft', 'lcrft'))
# print(login('William Golding', 'password'))
# change_password('William Golding', 'password', 'wigold')
# login('George Orwell', 'orwell1984')
# login('George Orwell', 'orwell1948')
# change_password('George Orwell', 'orwell1984', 'orwell1984')
# change_password('George Orwell', 'orwell1948', 'orwell1984')
# print(login('George Orwel', 'orwell1984'))
# create_user('George Orwell', '1984', 'orwell1984')