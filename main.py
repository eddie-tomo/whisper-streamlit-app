import streamlit as st
import whisper
import tempfile

st.title("問診内容の音声→テキスト化")

uploaded_file = st.file_uploader("音声ファイルをアップロードしてください", type=["mp3", "m4a", "wav"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    model = whisper.load_model("base")
    result = model.transcribe(tmp_path, language="ja")

    st.subheader("🎧 文字起こし結果")
    st.text_area("テキスト出力", result["text"], height=300)
