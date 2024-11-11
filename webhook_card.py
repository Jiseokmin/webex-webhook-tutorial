import requests

access_token = "your access token"
room_id = "room id"
adaptive_card_content = {
    "type": "AdaptiveCard",
    "version": "1.0",
    "body": [
        {
            "type": "ColumnSet",
            "columns": [
                {
                    "type": "Column",
                    "width": 2,
                    "items": [
                        {
                            "type": "TextBlock",
                            "text": "Tell us about yourself",
                            "weight": "bolder",
                            "size": "large",
                            "color": "attention",
                        },
                        {
                            "type": "TextBlock",
                            "text": "We just need a few more details to get you booked for the trip of a lifetime!",
                            "isSubtle": True,
                            "wrap": True,
                        },
                        {
                            "type": "TextBlock",
                            "text": "Don't worry, we'll never share or sell your information.",
                            "isSubtle": True,
                            "wrap": True,
                            "size": "small",
                        },
                        {"type": "TextBlock", "text": "Your name", "wrap": True},
                        {
                            "type": "Input.Text",
                            "id": "Name",
                            "placeholder": "John Andersen",
                        },
                        {"type": "TextBlock", "text": "Your website", "wrap": True},
                        {
                            "type": "Input.Text",
                            "id": "Url",
                            "placeholder": "https://example.com",
                        },
                        {"type": "TextBlock", "text": "Your email", "wrap": True},
                        {
                            "type": "Input.Text",
                            "id": "Email",
                            "placeholder": "john.andersen@example.com",
                            "style": "email",
                        },
                        {"type": "TextBlock", "text": "Phone Number"},
                        {
                            "type": "Input.Text",
                            "id": "Tel",
                            "placeholder": "+1 408 526 7209",
                            "style": "tel",
                        },
                    ],
                },
                {
                    "type": "Column",
                    "width": 1,
                    "items": [
                        {
                            "type": "Image",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/b/b2/Diver_Silhouette%2C_Great_Barrier_Reef.jpg",
                            "size": "auto",
                        }
                    ],
                },
            ],
        }
    ],
    "actions": [
        {"type": "Action.OpenUrl", "title": "더 보기", "url": "https://www.webex.com"}
    ],
}

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
}

message_data = {
    "roomId": room_id,
    "markdown": "Webex Adaptive Card 메시지",
    "attachments": [
        {
            "contentType": "application/vnd.microsoft.card.adaptive",
            "content": adaptive_card_content,
        }
    ],
}

response = requests.post(
    "https://webexapis.com/v1/messages", headers=headers, json=message_data
)
print(response.json())
