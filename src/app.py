import streamlit as st
from csv_profiler.io import read_csv_rows
from csv_profiler.profile import basic_profile
from csv_profiler.render import render_markdown
import csv
from io import StringIO
import json
from pathlib import Path

lst = read_csv_rows(r"C:\Users\HP\Desktop\SDAIA_BOOTCAMP\csv-profiler\src\data\sample.csv")
st.title("Hello Serry this is the title Wallah am not cheating")
st.set_page_config(page_title="CSV Profiler", layout="wide")
st.caption("This is my caption  and i just wana say Serry am not cheating")
st.sidebar.header("i did side bar header to just let u know Serry")

rows = None
report = st.session_state.get("report")


# source = st.sidebar.selectbox("osama source", ["Upload", "Local path"])



uploaded = st.file_uploader("Uplod here Serry",type=["csv"])
preview= st.checkbox("Serry show it", value=True)



if uploaded is not None:
    text = uploaded.getvalue().decode("utf-8-sig")
    file=StringIO(text)
    reader = csv.DictReader(file)
    rows = list(reader)

    if len(rows) == 0:
        st.error("CSV has no data. Upload a CSV with at least 1 row.")
        st.stop()
    if len(rows[0]) == 0:
        st.warning("CSV has no headers (no columns detected).")




    if preview:
        st.subheader("Preview")
        if st.button("Press"):
            st.write(rows[:5])
    else:
        st.info("Serry Upload a CSV to begin and use mouse.")


    if rows is not None:
        if len(rows) > 0:
            if st.button("GENERate RePoRt"):
                report= basic_profile(rows)
                st.session_state["report"] = report
    if report is not None:
        st.subheader("Columns")
        st.write(report["columns"])
    
    if report is not None:
        report_name = st.sidebar.text_input("Report name", value="report")
        json_file = report_name + ".json"
        json_text = json.dumps(report, indent=2, ensure_ascii=False)
        md_file = report_name + ".md"
        md_text = render_markdown(report)
        st.write(md_text)

        if st.button("Save to outputs/"):
            c1, c2 = st.columns(2)
            c1.download_button("Download JSON", data=json_text, file_name=json_file)
            c2.download_button("Download Markdown", data=md_text, file_name=md_file)
            out_dir = Path("outputs")
            out_dir.mkdir(parents=True, exist_ok=True)
            (out_dir / json_file).write_text(json_text, encoding="utf-8")
            (out_dir / md_file).write_text(md_text, encoding="utf-8")
            st.success("Saved outputs/" + json_file + " and outputs/" + md_file)
    






# if st.button("show it as markdown"):
#     report =st.session_state["report"]
#     








# st.write("Selected:", source)
# st.write(lst[0:5])


# uploaded = st.file_uploader("Upload a CSV", type=["csv"])
# if uploaded is not None:
#     st.write("Filename:", uploaded.name)
#     st.write("Size (bytes):", uploaded.size)


# text = uploaded.getvalue().decode("utf-8-sig")
# file_like = StringIO(text)
# reader = csv.DictReader(file_like)   
# rows = list(reader)     