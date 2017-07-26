import wikipedia

wikipedia.set_lang('ja') # 対象とする言語を日本語に設定する
page = wikipedia.page('存在しないページのタイトルを書く') # 指定したキーワードのページを取得
print(page.title) # ページのタイトルを表示
print(page.summary) # ページの要約を表示

