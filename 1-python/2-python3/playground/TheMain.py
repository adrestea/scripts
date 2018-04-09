#!/usr/bin/env python3

projects = {}
debug = True
project_lists = (
    '1.xml',
    '2.xml',
    '3.xml',
    '4.xml',
    '5.xml',
)

android_original_list = (
    'o.xml',
)

bash_app_commands = (
    '$repo init -u ssh://abc@xx.xx.xx.xxx:xxxxx/app/manifest -b xxx/master -m {} '
    '--repo-url=ssh://abc@xx.xx.xx.xxx:xxxxx/git-repo.git --repo-branch=stable --no-repo-verify',
    'repo sync'
)

bash_android_commands = (
    ''
)


def show_all_projects():
    global projects
    projects = {str(i): project_lists[i] for i in range(len(project_lists))}
    if debug:
        print(projects)
    items = projects.items()
    print("-" * 20)
    for k, v in items:
        print("    %s: %s" % (k, v))
    print("-" * 20)


def get_input(tips):
    return input(tips)


if __name__ == '__main__':
    show_all_projects()
    user_select = get_input("Please input select:")
    while user_select not in projects.keys():
        user_select = str(get_input("Please confirm input select:"))
    download_project = projects[user_select]
    if debug:
        print("select project xml is :%s" % download_project)
    exit(0)

