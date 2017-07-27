import wikipedia

wikipedia.set_lang('ja')
page = wikipedia.page('Python')
print(page.title)
print(page.summary)

