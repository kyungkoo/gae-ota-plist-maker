# -*- coding: utf-8 -*-

template_url = "{{url}}"
template_bundle_id = "{{bundle_id}}"
template_app_version = "{{app_version}}"
template_app_title = "{{app_title}}"


def _ask_app_info():
    """
    plist 생성에 필요한 정보들을 물어보는 메소드.
    """
    url = raw_input("URL > ")
    bundle_id = raw_input("Bundle ID > ")
    version = raw_input("Version > ")
    title = raw_input("Title > ")
    return (url, bundle_id, version, title)


def _write_plist(title, lines):
    """
    전달받은 title 과 lines 을 title.plist 에 저장하는 메소드.
    """
    file_name = title+".plist"
    with open(file_name, "w") as file:
        file.write(lines)


def make_plist(url, bundle_id, version, title):
    """
    template.plist 에 전달받은 정보를 매핑하여 title.plist 를 생성하는 메소드.
    """
    lines = ""
    with open('template.plist', 'r') as template:
        for line in template:
            if template_url in line:
                lines += line.replace(template_url, url)
            elif template_bundle_id in line:
                lines += line.replace(template_bundle_id, bundle_id)
            elif template_app_version in line:
                lines += line.replace(template_app_version, version)
            elif template_app_title in line:
                lines += line.replace(template_app_title, title)
            else:
                lines += line

    return lines
