from googleapiclient.discovery import build

api_key = 'YOUR_GOOGLE_API_KEY' 
search_engine_id = 'YOUR_SEARCH_ENGINE_ID' # https://programmablesearchengine.google.com/

query = 'QUERY'
default_pages = 10

service = build("customsearch", "v1", developerKey=api_key)

response = service.cse().list(q=query, cx=search_engine_id,num=default_pages).execute()

# Result
for i in response['items']:

    print(i['link'])
