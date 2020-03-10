import json
from pprint import pprint
from datetime import datetime, timedelta


def generate_data(config):
    # data = {}
    # data['name'] = config['name']
    current_time = datetime.utcnow()
    print(current_time)

    today = datetime.today().strftime('%Y-%m-%d')
    tomorrow = (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d')
    checkpoints = config['checkPoint']

    for i in range((len(checkpoints)-1), -1, -1):
        prev_cp = datetime.strptime(today + ' ' + checkpoints[i]['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
        # print('finding previous ckeck point, checking timestamp:' + str(prev_cp))
        # caluclating time diff between current time and checkpoint time to find which value should be generated.
        time_elasped = int((current_time - prev_cp).total_seconds())
        # print(time_elasped)
        if time_elasped > 0:
            print('found previous ckeck point, timestamp:' + str(prev_cp))
            next_cp = datetime.strptime(tomorrow + ' ' + checkpoints[0]['timestamp'], '%Y-%m-%d %H:%M:%S.%f') if i == (len(checkpoints)-1) else datetime.strptime(today + ' ' + checkpoints[i+1]['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
            print('next ckeck point timestamp:' + str(next_cp))

            next_value = checkpoints[0]['value'] if i == (len(checkpoints)-1) else checkpoints[i+1]['value']
            print('time_elasped:' + str(time_elasped))

            generated_data = checkpoints[i]['value'] + ((next_value - checkpoints[i]['value'])/int((next_cp - prev_cp).total_seconds())) * time_elasped
            return generated_data
        elif time_elasped == 0:
            return checkpoints[i]['value']


def generate_label(config, generated_data):
    weight = config['weight']
    th = config['threshold']
    result = 0
    label = 0

    for (k, v) in generated_data.items():
        # print("Key: " + k)
        # print("Value: " + str(v))
        result += weight[k] * v

    if result >= th:
        label = 1
    else:
        label = 0


def load_config(config_filename):
    with open(config_filename) as json_file:
        return json.load(json_file)

# data['value'] = round(random.uniform(0.1, 9.9),2)
# data['timestamp'] = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]