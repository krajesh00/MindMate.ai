import sys
import os

# hacky way to import from parent directory
sys.path.insert(1, os.path.join(sys.path[0], '../..'))
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import resource_search.resource_finder
import resource_search.resources_type_enum
import dataCreation as DataCreation

def get_help_message(prompt, resource_type):
    emotions = DataCreation.analysis.identify_emotions(prompt)
    help_message = resource_search.resource_finder.find_resources(emotions, resource_search.resources_type_enum.ResourcesType[resource_type])

    return help_message
