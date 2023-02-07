import urllib.request
import json
import configparser


# gets apikey from config file
# comment to test workflow
def get_apikey():
    config = configparser.ConfigParser()
    config.read('app.config')
    apikey_from_file = config['secrets']['apikey']
    return apikey_from_file


# gets password from config file
def get_password():
    config = configparser.ConfigParser()
    config.read('app.config')
    password_from_file = config['secrets']['password']
    return password_from_file


# get form identifier from config file
def get_identifier():
    config = configparser.ConfigParser()
    config.read('app.config')
    identifier_from_file = config['secrets']['identifier']
    return identifier_from_file


# get subdomain from config file
def get_subdomain():
    config = configparser.ConfigParser()
    config.read('app.config')
    subdomain_from_file = config['secrets']['subdomain']
    return subdomain_from_file


# call API to get json data of form entries
def get_json():
    subdomain = get_subdomain()
    base_url = 'https://{}.wufoo.com/api/v3/'.format(subdomain)
    username = get_apikey()
    password = get_password()
    identifier = get_identifier()
    password_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_manager.add_password(None, base_url, username, password)
    handler = urllib.request.HTTPBasicAuthHandler(password_manager)
    opener = urllib.request.build_opener(handler)
    urllib.request.install_opener(opener)
    response = urllib.request.urlopen(base_url + 'forms/{}/entries.json?sort=EntryId&sortDirection=DESC'.format(identifier))
    data = json.load(response)
    return json.dumps(data, indent=4, sort_keys=True)


# write json data from form entries to a file
def write_to_file():
    with open("form_info.json", "w") as outfile:
        outfile.write(get_json())


write_to_file()
