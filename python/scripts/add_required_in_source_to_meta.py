import json

original_json = 'meta.json'
new_json = 'new_meta.json'

def main():
    with open(original_json) as json_data:
      data = json.load(json_data)

    for source_name, contents in data.items():
        for field in contents['fields']:
            field['required_in_source'] = False

    with open(new_json, 'w') as new:
        json.dump(data, new, sort_keys=True)

if __name__ == '__main__':
    main()