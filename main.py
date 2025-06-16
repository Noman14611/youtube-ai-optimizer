import streamlit as st
from title_generator import generate_titles, suggest_tags, generate_description
from thumbnail_analyzer import analyze_thumbnail
from PIL import Image

st.set_page_config(page_title="YouTube AI Optimizer", layout="wide")

st.title("🎯 YouTube AI Optimizer")

tab1, tab2, tab3 = st.tabs(["📢 Title & Tags", "🖼️ Thumbnail Analyzer", "📄 Description"])

with tab1:
    st.header("Generate Better Titles & Tags")
    video_topic = st.text_input("Enter your video topic/title:")
    if st.button("Generate"):
        titles = generate_titles(video_topic)
        tags = suggest_tags(video_topic)
        st.subheader("✨ Suggested Titles:")
        for title in titles:
            st.markdown(f"- {title}")
        st.subheader("🏷️ Suggested Hashtags/Tags:")
        st.code(", ".join(tags))

with tab2:
    st.header("Upload Thumbnail for Clickability Feedback")
    img = st.file_uploader("Upload Thumbnail", type=["jpg", "png"])
    if img:
        image = Image.open(img)
        st.image(image, caption="Uploaded Thumbnail", width=400)
        result = analyze_thumbnail(image)
        st.success(result)

with tab3:
    st.header("AI Video Description Generator")
    base_title = st.text_input("Enter your title or topic:")
    if st.button("Generate Description"):
        desc = generate_description(base_title)
        st.text_area("AI Description", value=desc, height=200)
