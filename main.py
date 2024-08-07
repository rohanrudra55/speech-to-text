"""
MIT License

Copyright (c) 2024 Rohan Rudra

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""




import streamlit as st
import assemblyai as aai
import os


def transcribe_and_generate_subtitles(api_key, sub_limit, audio_file):
    aai.settings.api_key = api_key

    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(audio_file)
    if transcript.status == aai.TranscriptStatus.error:
        st.error(transcript.error)
    else:
        subtitles = transcript.export_subtitles_srt(chars_per_caption=int(sub_limit))
        return subtitles


def main():
    st.set_page_config(page_title="rohanai", page_icon="assets/chrome.png")
    st.title("Transcribe Audio to Subtitles")
    st.write(
        "To use this tool, you'll need a free AssemblyAI account. Sign up using your institutional/work email and copy your API key into the field provided. We'll handle the rest!"
    )
    # st.image('assets/bg.jpeg')
    col1, col2 = st.columns([1, 5])
    with col1:
        st.link_button("About Me", "https://www.linkedin.com/in/rohanrudra55/")
    with col2:
        st.link_button("AssemblyAI", "https://www.assemblyai.com/")
    with st.form("APP"):
        api_key = st.text_input("Enter your AssemblyAI API key:")
        sub_limit = st.slider(
            "Character limit per line:", min_value=20, max_value=150, value=75
        )
        audio_file = st.file_uploader("Upload an audio file:")
        submitted = st.form_submit_button("Transcribe", type="primary")
        if submitted and api_key and audio_file:
            subtitles = transcribe_and_generate_subtitles(
                api_key, sub_limit, audio_file
            )
            if subtitles:
                st.success("Subtitles generated successfully!")
                output_file_name = (
                    os.path.splitext(audio_file.name)[0] + "_SUBTITLES.srt"
                )
                if st.button("Save Subtitles"):
                    with open(output_file_name, "a") as f:
                        f.write(subtitles)
                        f.close()
                    st.success(f"Subtitles saved as {output_file_name}")

                st.text_area("Subtitles:", value=subtitles)


if __name__ == "__main__":
    main()
