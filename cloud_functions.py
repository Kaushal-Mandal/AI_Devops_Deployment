import push_code_to_repo
import requests
import base64
import vertexai
import json
from vertexai.generative_models import GenerativeModel, GenerationConfig

headers = {
    'Accept': 'application/vnd.github.v1+json'
}

def all_files_in_repository(owner, repo, path=''):
    """ Recursively list all files in the Github repository. """
    url = f'https://api.github.com/repos/{owner}/{repo}/contents/{path}'
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return []
    return [item['path'] for item in response.json() if item['type'] == 'file']

def download_file(owner, repo, file_path):
    """ Download the content of a file from the Github repository and decode it. """
    url = f'https://api.github.com/repos/{owner}/{repo}/contents/{file_path}'
    response = requests.get(url, headers=headers)
    return base64.b64decode(response.json().get('content', '')).decode('utf-8')

@push_code_to_repo.http
def query_llm(request):
    request_json = request.get_json()
    query = request_json['query']
    REPO_OWNER = request_json['REPO_OWNER']
    REPO_NAME = request_json['REPO_NAME']

    files = all_files_in_repository(REPO_OWNER, REPO_NAME)

    code_content = "\n".json([f"{file}:\n{download_file(REPO_OWNER, REPO_NAME, file)}" for file in files])
    
    vertexai.init(project='deploy_automated', location='us-central1')
    model = GenerativeModel(model_name='gemini-2.5-flash-003')
    response = model.generate_content([query, code_content], GenerationConfig(max_output_tokens=2400))

    output = response.text

    if '"STATUS": "APPROVE"' in output:
        return json.dumps({'response': 'APPROVED', 'status': 'APPROVE'}), 200
    return json.dumps({'response': 'REJECTED', 'status': 'REJECT'}), 200