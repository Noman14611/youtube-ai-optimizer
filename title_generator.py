import openai

openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace on Hugging Face/Streamlit Cloud with secrets

def generate_titles(topic):
    prompt = f"Suggest 5 catchy YouTube titles for: {topic}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8
    )
    titles = response.choices[0].message.content.strip().split("\n")
    return titles

def suggest_tags(topic):
    prompt = f"Give 10 SEO YouTube hashtags for: {topic}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    tags = response.choices[0].message.content.strip().replace("#", "").split()
    return tags

def generate_description(topic):
    prompt = f"Write a detailed, engaging YouTube video description for: {topic}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content.strip()
