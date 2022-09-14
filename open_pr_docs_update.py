import sys

from utils import create_pull_request

module = sys.argv[1]
branch = sys.argv[2]

description=f"""
Update {module}* doc links
"""

# Create PR inside community.aws
_ = create_pull_request(
    "ansible-collections", # owner_name
    "community.aws", # repo_name
    description, # description
    "Update doc links", # title
    branch, # head_branch
    "main", # base_branch
)
