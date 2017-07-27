import wikipedia


def wikipedia_command(command):
    cmd, keyword = command.split(maxsplit=1)
    wikipedia.set_lang('ja')
    try:
        page = wikipedia.page(keyword)
        title = page.title
        summary = page.summary
        response = 'タイトル: {}\n{}'.format(title, summary)
    except wikipedia.exceptions.PageError:
        response = '「{}」ノ意味ガ見ツカリマセンデシタ'.format(keyword)
    return response
