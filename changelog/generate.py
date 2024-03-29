def changelog_entry(releace, version, bodytags):
    name = version['name']
    if version['compare_link']:
        name = f"[{ name }]({ version['compare_link'] })"

    text = f"## { name } ({ version['date_string'] })\n\n"
    text += changelog_entry_body(releace, bodytags)
    return text

def changelog_entry_body(releace, bodytags):
    text = ''
    commit_dict = {}
    for commit in releace:
        if commit['type'] in commit_dict:
            commit_dict[commit['type']].append(commit)
        else:
            commit_dict[commit['type']] = [commit]
                
    for commit_type, commits in commit_dict.items():
        if commit_type != None:

            text += changelog_block(
                commit_type, 
                [f"{ commit['description'] } ([{ commit['binsha'][:7] }]({ commit['link'] }))" for commit in commits] # body
            )
            text += '\n'

    relevant_texts = get_relevant_texts(releace, bodytags)

    if len(relevant_texts):
        text += changelog_block(None, relevant_texts)
        text += '\n'

    return text

def changelog_block(title, items):
    text = ''
    if title:
        text += f"### { title }\n\n"
    for item in items:
        if ':' in item[:18]:
            item = f"**{ item[:item.index(':') + 1] }**{ item[item.index(':') + 1:] }"
        text += f"* { item }\n"
    return text

def get_relevant_texts(commits, bodytags):
    texts = []
    for commit in commits:
        if 'body' in commit.keys():
            for bodytag in bodytags:
                if bodytag in commit['body']:

                    texts.append(commit['body'])
        
        if 'footer' in commit.keys():
            for bodytag in bodytags:
                if bodytag in commit['footer']:

                    texts.append(commit['footer'])

    return texts
