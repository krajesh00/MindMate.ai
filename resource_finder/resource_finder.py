import sys
import os
import requests
import json as JSON
from resources_type_enum import ResourcesType

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

import config

def find_concrete_resources(emotions):
    num_search_results = 2

    therapist_titles = []
    therapist_links = []
    center_titles = []
    center_links = []
    for emotion in emotions:
        payload = {
            'key': config.CUSTOM_SEARCH_API_KEY,
            'q': f'find a therapist for when you\'re feeling {emotion}',
            'num': num_search_results,
            'cx': config.SEARCH_ENGINE_ID
        }
        
        # search for therapists
        response = requests.get('https://customsearch.googleapis.com/customsearch/v1', params=payload)
        if response.status_code != 200:
            raise Exception(f'ERROR status code {response.status_code}')
        response_json = response.json()
        # for debugging
        # with open(f'therapists_{emotion}.json', 'w') as f:
        #     JSON.dump(response_json, f)
        for result in response_json['items']:
            therapist_titles.append(result['title'])
            therapist_titles[-1] = therapist_titles[-1].replace('...', '')
            therapist_links.append(result['link'])

        # search for wellness centers
        payload['q'] = f'wellness centers for when you\'re feeling {emotion}'
        response = requests.get('https://customsearch.googleapis.com/customsearch/v1', params=payload)
        if response.status_code != 200:
            raise Exception(f'ERROR status code {response.status_code}')
        response_json = response.json()
        # for debugging
        # with open(f'wellness_centers_{emotion}.json', 'w') as f:
        #     JSON.dump(response_json, f)
        for result in response_json['items']:
            center_titles.append(result['title'])
            center_titles[-1] = center_titles[-1].replace('...', '')
            center_links.append(result['link'])
    
    message = f"Here's some resources to find a therapist that could help:\n"
    for title, link in list(zip(therapist_titles, therapist_links)):
        message += f"{title} - {link}\n"
    message += "Here's some wellness centers that might be able to help\n"
    for title, link in list(zip(center_titles, center_links)):
        message += f"{title} - {link}\n"

    return message

resource_functions = {
    ResourcesType.CONCRETE_RESOURCES: find_concrete_resources
}

def find_resources(emotions, resource_type):
    message = f"It looks like you might be feeling {emotions[0]} or {emotions[1]}\n"
    message += resource_functions[resource_type](emotions)
    
    return message
