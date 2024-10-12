# Python script to convert the anomaly-detection settings 2.0 schema to a CSV file 
# that can be analyzed easily in an Excel Pivot table.
# This script works only on top of the settings 2.0 schema of 'builtin:anomaly-detection.metric-events'
# author: wolfgang beer
import json

# globals
csv = []

def load_json_file(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None
    
def entity_filter_to_string(entity_filter):
    str = ""
    if 'dimensionKey' in entity_filter:
        str = str + ":"  + entity_filter['dimensionKey']
        for c in entity_filter['conditions']:
            str = str + ":"  + c['type'] + ':' + c['operator'] + ':' + c['value']
    return str.replace(",", "")

def dim_filter_to_string(dim_filter):
    str = ""
    for filter in dim_filter:
        str = str + ":"  + filter['dimensionKey'] + ":" + filter['dimensionValue']
    return str.replace(",", "")

def write_array_to_file(file_path, arr):
    try:
        with open(file_path, 'w') as file:
            for l in csv:
                file.write(l + "\n")
        print(f"CSV file has been written to {file_path} successfully.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

file_path = 'response.json' 
loaded_data = load_json_file(file_path)
if loaded_data:
    print("JSON file loaded successfully.")
    print("Total: {}".format(loaded_data['totalCount']))
    csv.append("key, type, enabled, author, metricKey, metricSelector, entityFilter, dimFilter, threshold")
    for conf in loaded_data['settings']:
        metricKey = ""
        metricSelector = ""
        entityFilter = ""
        dimFilter = ""
        threshold = ""
        if conf['value']['modelProperties']['type'] == 'STATIC_THRESHOLD':
            threshold = str(conf['value']['modelProperties']['threshold'])

        if conf['value']['queryDefinition']['type'] == 'METRIC_KEY':
            metricKey = conf['value']['queryDefinition']['metricKey']
            entityFilter = entity_filter_to_string(conf['value']['queryDefinition']['entityFilter'])
            dimFilter = dim_filter_to_string(conf['value']['queryDefinition']['dimensionFilter'])
        else:
            metricSelector = conf['value']['queryDefinition']['metricSelector']
        csv.append("{}, {}, {}, {}, {}, {}, {}, {}, {}".format(conf['key'], 
                                           conf['value']['queryDefinition']['type'], 
                                           conf['value']['enabled'],
                                           conf['author'].replace(",", ""),
                                           metricKey,
                                           metricSelector.replace(",", ""),
                                           entityFilter,
                                           dimFilter,
                                           threshold
                                           ))

write_array_to_file("test.csv", csv)
