import requests

# Webex API의 메시지 전송 URL
url = "https://webexapis.com/v1/messages"

# Access Token과 방 ID 또는 사용자 이메일을 지정
access_token = "your access token"  # 봇 생성 시 복사한 토큰을 여기에 붙여넣습니다.
room_id = "room id"  # 메시지를 보낼 Webex Room의 ID
# 또는 특정 사용자 이메일로 보내려면 email = "user@example.com"

# 메시지 내용을 설정
message = "# 테스트 테스트\n\n- 항목 1\n- 항목 2\n- 항목 3"

# 헤더와 데이터 설정
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
}
data = {
    "roomId": room_id,
    "markdown": message,
}  # 또는 "toPersonEmail": email, text or markdown 지정

# POST 요청 보내기
response = requests.post(url, headers=headers, json=data)

# 요청 결과 확인
if response.status_code == 200:
    print("Message sent successfully!")
else:
    print(f"Failed to send message: {response.status_code}")
    print(response.json())
