import sys
import os
import requests
import json as JSON
from resources_type_enum import ResourcesType

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

import config

NUM_SEARCH_RESULTS = 2

def make_search(query):
    payload = {
            'key': config.CUSTOM_SEARCH_API_KEY,
            'q': query,
            'num': NUM_SEARCH_RESULTS,
            'cx': config.SEARCH_ENGINE_ID
    }

    response = requests.get('https://customsearch.googleapis.com/customsearch/v1', params=payload)
    if response.status_code != 200:
        raise Exception(f'ERROR status code {response.status_code}')
    return response.json()

def find_concrete_resources(emotions):
    therapist_titles = []
    therapist_links = []
    center_titles = []
    center_links = []
    for emotion in emotions:
        # search for therapists
        response = make_search(f'find a therapist for when you\'re feeling {emotion}')
        # for debugging
        # with open(f'therapists_{emotion}.json', 'w') as f:
        #     JSON.dump(response, f)
        for result in response['items']:
            therapist_titles.append(result['title'])
            therapist_titles[-1] = therapist_titles[-1].replace('...', '')
            therapist_links.append(result['link'])

        # search for wellness centers
        response = make_search(f'wellness centers for when you\'re feeling {emotion}')
        # for debugging
        # with open(f'wellness_centers_{emotion}.json', 'w') as f:
        #     JSON.dump(response, f)
        for result in response['items']:
            center_titles.append(result['title'])
            center_titles[-1] = center_titles[-1].replace('...', '')
            center_links.append(result['link'])
    
    message = f"Here's some resources to find a therapist that could help:\n"
    for title, link in list(zip(therapist_titles, therapist_links)):
        message += f"{title} - {link}\n"
    message += "Here's some wellness centers that might be able to help:\n"
    for title, link in list(zip(center_titles, center_links)):
        message += f"{title} - {link}\n"

    return message

def find_helplines(emotions):
    titles = []
    links = []

    for emotion in emotions:
        response = make_search(f'feeling {emotion} helpline')
        for result in response['items']:
            titles.append(result['title'])
            titles[-1] = titles[-1].replace('...', '')
            links.append(result['link'])
    
    message = f"Here's some helplines that you can call for help:\n"
    for title, link in list(zip(titles, links)):
        message += f"{title} - {link}\n"

    return message

def find_blog_posts(emotions):
    titles = []
    links = []

    for emotion in emotions:
        response = make_search(f'how to stop feeling {emotion}')
        for result in response['items']:
            titles.append(result['title'])
            titles[-1] = titles[-1].replace('...', '')
            links.append(result['link'])
    
    message = f"Here's some resources you can look at:\n"
    for title, link in list(zip(titles, links)):
        message += f"{title} - {link}\n"

    return message

def find_exercises(emotions):
    titles = []
    links = []

    for emotion in emotions:
        response = make_search(f'exercises to stop feeling {emotion}')
        for result in response['items']:
            titles.append(result['title'])
            titles[-1] = titles[-1].replace('...', '')
            links.append(result['link'])
    
    message = f"Here's some exercises you can do to feel better:\n"
    for title, link in list(zip(titles, links)):
        message += f"{title} - {link}\n"

    return message

def find_starting_point(emotions):
    message = f"Take a moment to just take a few deep breaths\n"

    return message

resource_functions = {
    ResourcesType.CONCRETE_RESOURCES: find_concrete_resources,
    ResourcesType.HELPLINES: find_helplines,
    ResourcesType.BLOG_POSTS: find_blog_posts,
    ResourcesType.EXERCISES: find_exercises,
    ResourcesType.STARTING_POINT: find_starting_point
}

def find_resources(emotions, resource_type):
    message = f"It looks like you might be feeling "
    if emotions.length == 1:
        message += f"{emotions[0]}\n"
    elif emotions.length == 2:
        message += f"{emotions[0]} or {emotions[1]}\n"
    elif emotions.length > 2:
        for i in range(len(emotions) - 1):
            message += f"{emotions[i]}, "
        message += f"or {emotions[-1]}\n"
    message += resource_functions[resource_type](emotions)
    
    return message
