import requests

response = requests.get("https://gitlab.com")

print(response)

response1 = requests.get("https://github.com/CooperEthan?tab=repositories", auth=('cooperethan', 'Dersim2362'))


my_projects = response1.json()
print(my_projects)


for project in my_projects:
    print(f"Project Name: {project['name']}\nProject Url: {project['web_url']}\n")