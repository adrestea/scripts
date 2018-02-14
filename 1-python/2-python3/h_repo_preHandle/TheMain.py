#!/usr/bin/env python3

projects = {}
debug = True
project_lists = (
    'WirelessEarbudsCompanion_app_apps_WirelessEarbudsCompanion_1.00_api19_master.xml',
    'HTCSetupWizard_app_apps_HTCSetupWizard_9.10_and8.0_mainline_O80.xml',
    'CustomizationSettingsProvider_app_providers_CustomizationSettingsProvider_7.0_and5.1_mainline.xml',
    'CustomizationSetup_app_apps_CustomizationSetup_9.10_and8.0_mainline.xml',
    'UIBC_app_apps_UIBC_8.00_api26_Sense90.xml',
    'UIBC_app_apps_UIBC_8.00_api26_Sense90_g3.0.xml',
    'UDove_app_apps_UDove_9.00_api26_master.xml',
    'UDove_app_apps_UDove_9.10_api26_master.xml'
)

android_original_list = (
    'o-rel_shep_qct845.xml',
)

bash_app_commands = (
    '$repo init -u ssh://archermind@10.14.11.14:29418/app/manifest -b htc/master -m {} '
    '--repo-url=ssh://archermind@10.13.14.218:29418/git-repo.git --repo-branch=stable --no-repo-verify',
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
        user_select = get_input("Please confirm input select:")
    download_project = projects[user_select]
    if debug:
        print("select project xml is :%s" % download_project)
        # print(cmds[0].format(download_project))
    for cmd in bash_commands:
        cmd = cmd.format(download_project)
        print(cmd)
        # os.system(cmd)
