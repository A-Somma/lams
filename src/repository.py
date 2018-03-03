import pandas
import os
import time
import datetime

START_TIMESTAMP = datetime.datetime.today().strftime('%y%m%d_%H%M%S')
DATA_FOLDER = 'data'
RESULTS_FOLDER = 'results'
SOURCE_DATA_FOLDER = 'source'
BOOTSRTAP_FOLDER = 'bootstrap'
DATA_FILE = ''


def get_source_data():
    f = os.path.join(DATA_FOLDER, SOURCE_DATA_FOLDER, DATA_FILE+'.csv')
    assert os.path.exists(f), 'File: {} not found'.format(f)
    return pandas.read_csv(f)

def add_header_to_results(header):
    folder = os.path.join(DATA_FOLDER, RESULTS_FOLDER, DATA_FILE)
    if not os.path.exists(folder):
                        os.makedirs(folder)
    file_path = os.path.join(folder, '{}.csv'.format(START_TIMESTAMP))
    with open(file_path, 'wb') as results:
        results.write(header)

def append_result(result):
    folder = os.path.join(DATA_FOLDER, RESULTS_FOLDER, DATA_FILE)
    file_path = os.path.join(folder, '{}.csv'.format(START_TIMESTAMP))
    assert os.path.exists(file_path), 'Data file is missing!'
    with open(file_path, 'ab') as results:
        results.write(result)

def save_bootstrap_data(data):
    folder = os.path.join(DATA_FOLDER, BOOTSRTAP_FOLDER, DATA_FILE)
    if not os.path.exists(folder):
                        os.makedirs(folder)
    timestamp = datetime.datetime.today().strftime('%y%m%d_%H%M%S') 
    file_name = 'bs_{}.csv'.format(timestamp)
    file_path = os.path.join(folder, file_name)
    assert not os.path.exists(file_path), 'File already exits, aborting...'
    data.to_csv(file_path, index = False)
    return file_name