import wolframalpha
import wikipedia as wk
import wikipediaapi as kw

while True:
    user_input = input("Question: ")
    try:
        #wolframalpha
        app_id = "HWWEQW-2J96G39LYU"
        client = wolframalpha.Client(app_id)
        result = client.query(user_input)
        answer = next(result.results).text
        print(answer)
    except:
        #wikipedia
        print(wk.summary(user_input))
        wiki_wiki = kw.Wikipedia("Thomas Edison", 'en')