#환경: 윈도우 with "curl" command
#-X: HTTP method option
#-H: Header option

# 1-1. get room id: command
curl -X GET "https://webexapis.com/v1/rooms" -H "Authorization: Bearer [your access token]"

# 1-2. get room id: result
{"items":[{"id":"[room id]",
           "title":"[room title]",
           "type":"[room type]",
           "isLocked":[boolean],
           "lastActivity":"[date]",
           "creatorId":"[ID]",
           "created":"[date]",
           "ownerId":"ID",
           "isPublic":[boolean],
           "isReadOnly":[boolean]}]
}

# 2-1. 로컬 환경에서 POST로 웹훅 메세지 날리기 (text 형태)
curl -X POST -H "Content-Type: application/json" -d "{\"text\": \"# 웹엑스 테스트\"}" "[WebHook URL]"

# 2-2. 로컬 환경에서 POST로 웹훅 메세지 날리기 (markdown 형태)
curl -X POST -H "Content-Type: application/json" -d "{\"markdown\": \"# Webex* Message *TEST* **GOOD**\"}" "[WebHook URL]"