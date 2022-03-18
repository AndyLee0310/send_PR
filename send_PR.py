import requests
import json

# input base branch
base_branch = input("Base branch : ")
# input compare branch
compare_branch = input("Compare branch : ")
# input PR title
pr_title = input("PR Title : ")
# input file's location of Test Step
test_step_location = input("test step location : ")

# read files and combine the contents of pr content
first_raw = f"This branch is based on {base_branch}\n"
pr_body = open('./need_add.txt', 'r', encoding='utf-8')
test_case_file = open(test_step_location,'r', encoding='utf-8')
pr_content = first_raw + pr_body.read() + "\n\n" + test_case_file.read()
pr_body.close()
test_case_file.close()

# use github api to add a new pull request
print("Please one moment ~")
repo_url = "https://api.github.com"
owner = "repositorie's owner"
repo = "repositorie name"
auth_token = "user's auth_token"

# array about reviewers, assignees, and labels
reviewers = ["reviewers"]
assignees = ["assignees"]
labels = ["labels"]

# Create a new pull request
r = requests.post(
    f"{repo_url}/repos/{owner}/{repo}/pulls", 
    data = json.dumps({
        "title": pr_title,
        "body": pr_content,
        "head": compare_branch,
        "base": base_branch
    }),
    headers = {'Authorization': f'token {auth_token}'},
)
print(r.status_code)

# Change byte to dict with `content`, and get pull number
pr_number = json.loads(r.content.decode('utf-8'))['number']

# Add reviewers to this pull request
r_reviewers = requests.post(
            f"{repo_url}/repos/{owner}/{repo}/pulls/{pr_number}/requested_reviewers",
            data = json.dumps({
                "reviewers":reviewers
            }),
            headers = {'Authorization': f'token {auth_token}'}
)
print(r_reviewers.status_code)

# Add assignees to this pull request
r_assignees = requests.post(
            f"{repo_url}/repos/{owner}/{repo}/issues/{pr_number}/assignees",
            data = json.dumps({
                "assignees":assignees
            }),
            headers = {'Authorization': f'token {auth_token}'}
)
print(r_assignees.status_code)

# Add assignees to this pull request
r_labels = requests.post(
            f"{repo_url}/repos/{owner}/{repo}/issues/{pr_number}/labels",
            data = json.dumps({
                "labels":labels
            }),
            headers = {'Authorization': f'token {auth_token}'}
)
print(r_labels.status_code)