import sys

from utils import dump_to_file
from utils import load_file

module = sys.argv[1]
path = sys.argv[2]


def update_doc_links():
    to_be_migrated = []
    com_data = load_file(f"{path}/meta/runtime.yml")

    for module_name in com_data['action_groups']['aws']:
        if module in module_name:
            to_be_migrated.append(module_name)

    docs_pr = load_file(f"{path}/.github/workflows/docs-pr.yml")

    for module_name in to_be_migrated:
        docs_pr['jobs']['validate-docs']['with']['provide-link-targets'] += f"ansible_collections.amazon.aws.{module_name}_module\n"
        docs_pr['jobs']['build-docs']['with']['provide-link-targets'] += f"ansible_collections.amazon.aws.{module_name}_module\n"
    
    dump_to_file(docs_pr, f"{path}/.github/workflows/docs-pr.yml")

    docs_push = load_file(f"{path}/.github/workflows/docs-push.yml")
    for module_name in to_be_migrated:
        docs_push['jobs']['build-docs']['with']['provide-link-targets'] += f"ansible_collections.amazon.aws.{module_name}_module\n"

    dump_to_file(docs_push, f"{path}/.github/workflows/docs-pr.yml")


update_doc_links()