"""
Example script for fetching problems and convert them to text descriptions.
"""
import requests, json, os

# Those two environment variables must be present
if 'DT_URL' not in os.environ:
    print("Environment variable DT_URL is missing!")
    exit()
    
if 'DT_API_TOKEN' not in os.environ:
    print("Environment variable DT_API_TOKEN is missing!")
    exit()

YOUR_DT_API_URL = os.environ['DT_URL']
# Dynatrace API token with v2 problems, events and entity read scope activated
YOUR_DT_API_TOKEN = os.environ['DT_API_TOKEN'] 

def extract_event_description(event):
    for p in event['data']['properties']:
        if p['key'] == 'dt.event.description':
            return p['value']
    return ""

def fetch_problem(problem_id):
    r = requests.get(YOUR_DT_API_URL + '/api/v2/problems/' + problem_id, headers={'Authorization' : 'Api-Token ' + YOUR_DT_API_TOKEN})
    if r.status_code == 200: 
        return r.json()
    else:
        print("Http error: %d" % (r.status_code))
        return {}
    
def text_formatter(p_json):
    entity_event_map = {}
    entity_details = {}
    p_str = "Summary of the {category} Problem {problem_id}, where Dynatrace detected a {title} on {level} level.\n".format(category = p_json['severityLevel'], problem_id = p_json['displayId'], title = p_json['title'], level = p_json['impactLevel'])
    print(len(p_json['evidenceDetails']['details']))
    for evidence in p_json['evidenceDetails']['details']:
        print(evidence['displayName'])
        # remember the list of entities
        entity_details[evidence['entity']['entityId']['id']] = evidence['entity']
        # group evidences found by entity identifier
        if evidence['entity']['entityId']['id'] not in entity_event_map:
            entity_event_map[evidence['entity']['entityId']['id']] = []
        entity_event_map[evidence['entity']['entityId']['id']].append(evidence)


    print(len(entity_details.keys())) 
    print(len(entity_event_map.keys()))
    # iterate through all the findings and collect the texts per entity
    for entity_id in entity_details.keys():
        print(entity_details[entity_id])
        for event in entity_event_map[entity_id]:
            if event['evidenceType'] == 'EVENT':
                p_str += "{entity_type} '{entity_name}' with id {entity_id} shows a {event_title} event where {event_details}.\n".format(entity_type = entity_details[entity_id]['entityId']['type'], entity_name = entity_details[entity_id]['name'], entity_id = entity_id, event_title = event['displayName'], event_details=extract_event_description(event))
                



    return p_str


#print(text_formatter(fetch_problem('4998261499535699417_1679896620000V2')))

print(text_formatter(fetch_problem('7224322424952039803_1679891220000V2')))

