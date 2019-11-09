import json

with open('source_file_2.json') as json_file:
    data = json.load(json_file)

sorted_data = sorted(data, key=lambda x: abs(0 - x['priority']))

managers = {}
watchers = {}

for project in sorted_data:
    for manager in project['managers']:
        if not manager in managers:
            managers[manager] = []
        managers[manager].append(project['name'])

    for watcher in project['watchers']:
        if not watcher in watchers:
            watchers[watcher] = []
        watchers[watcher].append(project['name'])

#Exporting files
with open('managers.json', 'w') as managers_json:
    json.dump(managers, managers_json)

with open('watchers.json', 'w') as watchers_json:
    json.dump(watchers, watchers_json)