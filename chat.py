import requests

response = requests.post(
    "https://api.inceptionlabs.ai/v1/chat/completions",
    headers={
        "Authorization": "Bearer sk_9be7e1057379c954fb5c7b7d19a59c4c",
        "Content-Type": "application/json"
    },
    json={
        "model": "mercury-2",
        "messages": [
            {
                "role": "system",
                "content": "You are StartupForge AI, an expert startup coach. Help aspiring entrepreneurs turn ideas into successful businesses by providing clear, practical, and actionable guidance on validation, planning, branding, funding, and growth."
            },
            {
                "role": "user",
                "content": "I have an idea for a food delivery startup. How can I validate it?"
            },
            {
                "role": "assistant",
                "content": "To validate your food delivery startup idea, start by identifying your target customers, conducting surveys, analyzing competitors, and building a simple MVP to test market demand."
            },
            {
                "role": "user",
                "content": "What should I include in the MVP?"
            }
        ]
    }
)

print(response.json())