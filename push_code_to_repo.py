import requests

cloud_function_url = 'https://us-central1-ai-driven-deployment.cloudfunctions.net/gemini-devops'

query='Analyze the code and suggest the changes required in the files which have any issue.'

payload = {
    'query': query,
    'REPO_OWNER': 'kaushalm',
    'REPO_NAME': 'JAVA'
}

headers = {
    'Content-Type': 'application/json'
}

response = requests.post(cloud_function_url, json=payload, headers=headers)
print(response)

output_response = response.json()
print('Response from Cloud Function:', output_response['response'])
