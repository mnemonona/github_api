import requests

from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable.
response_dict = r.json()

# Explore information about the repositories.
repo_dicts = response_dict['items']

repo_links, stars, labels = [], [], []
for repo in repo_dicts:
    repo_name = repo['name']
    repo_url = repo['html_url']
    repo_link = f'<a href = "{repo_url}"> {repo_name} </a>'
    repo_links.append(repo_link)
    stars.append(repo['stargazers_count'])

    owner = repo['owner']['login']
    description = repo['description']
    label = f"{owner}<br />{description}"
    labels.append(label)

data = [{
    'type': 'bar', 
    'x' : repo_names, 
    'y' : stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)', 
        'line' : {
            'width': 1.5, 
            'color': 'rgb(25, 25, 25)'
        }, 
        'opacity': 0.6
    }
}]

my_layout = {
    'title': "Найпопулярніші Python проекти на Github", 
    'titlefont': {'size': 28}, 
    'xaxis': {
        'title': "Репозиторії", 
        'titlefont': {'size': 24}, 
        'tickfont': {'size':14}
        }, 
    'yaxis': {
        'title': "Зірки", 
        'titlefont': {'size': 24}, 
        'tickfont': {'size':14}
        }
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename = "python_repos.html")