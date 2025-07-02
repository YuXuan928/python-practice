# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 14:16:12 2025

@author: 職前
"""

import streamlit as st

# 測驗題目資料結構
quiz_data = [
    {
        "question": "1. 在 Python 程式中，我們利用 type() 查詢資料類別。以下程式輸出分別是？\n\n"
                    "type(+1E10)\n"
                    "type(5.0)\n"
                    "type(\"True\")\n"
                    "type(False)\n",
        "options": {
            "A": "int, int, bool, bool",
            "B": "float, float, str, bool",
            "C": "int, float, str, bool",
            "D": "float, int, str, str",
        },
        "answer": ["B"],
        "multi": False
    },
    {
        "question": "2. 哪些下列表達式的值是 True？(可多選)",
        "options": {
            "A": "0 or 5",
            "B": "bool(0)",
            "C": "None is None",
            "D": "-5 < 0 < 5",
        },
        "answer": ["A", "C", "D"],
        "multi": True
    },
    {
        "question": "3. 請判斷下列敘述是否正確：\n\n"
                    "A. 在第3行的語法是不正確的比較\n"
                    "B. 在第6行的語法只有 n1 小於 n2 才會執行\n"
                    "C. 在第8行的語法只有 n1 大於 n2 時才會執行\n"
                    "D. 在第9行的語法是不正確的比較\n",
        "options": {
            "A": "Yes",
            "B": "No",
            "C": "Yes",
            "D": "Yes"
        },
        "answer": {
            "A": "Yes",
            "B": "No",
            "C": "Yes",
            "D": "Yes"
        },
        "multi": "yesno"
    }
]

def main():
    st.title("Python 線上測驗系統")
    st.write("請完成以下題目，支援單選、多選、判斷題（是非題）")

    if 'q_index' not in st.session_state:
        st.session_state.q_index = 0
        st.session_state.score = 0

    if st.session_state.q_index < len(quiz_data):
        q = quiz_data[st.session_state.q_index]

        st.markdown(f"### {q['question']}")

        user_answers = []

        if q.get("multi") == False:
            # 單選題
            user_answer = st.radio("請選擇答案：", list(q["options"].keys()),
                                   format_func=lambda x: f"{x}. {q['options'][x]}")
            user_answers = [user_answer]

        elif q.get("multi") == True:
            # 多選題
            selected_options = []
            for key, text in q["options"].items():
                checked = st.checkbox(f"{key}. {text}")
                if checked:
                    selected_options.append(key)
            user_answers = selected_options

        elif q.get("multi") == "yesno":
            # 判斷題(是非題) - 每題分別有自己的判斷
            yesno_answers = {}
            for key, text in q["options"].items():
                choice = st.radio(f"{key}. {text}", ["Yes", "No"], key=key)
                yesno_answers[key] = choice
            user_answers = yesno_answers

        if st.button("提交答案"):
            correct = False

            if q.get("multi") == "yesno":
                # 比較 dict
                if user_answers == q["answer"]:
                    correct = True
            else:
                # 單選、多選用集合比較
                if set(user_answers) == set(q["answer"]):
                    correct = True

            if correct:
                st.success("✅ 答對了！")
                st.session_state.score += 1
            else:
                st.error("❌ 答錯了！")
                if q.get("multi") == "yesno":
                    wrong_list = []
                    for k, v in q["answer"].items():
                        if user_answers.get(k) != v:
                            wrong_list.append(f"{k}: 正確答案是 {v}")
                    st.write("正確答案：")
                    for w in wrong_list:
                        st.write(w)
                else:
                    correct_str = ", ".join(q["answer"])
                    st.write(f"正確答案是：{correct_str}")

            st.session_state.q_index += 1
            st.experimental_rerun()
    else:
        st.write(f"測驗完成！你的分數是 {st.session_state.score} / {len(quiz_data)}")
        if st.button("重新開始"):
            st.session_state.q_index = 0
            st.session_state.score = 0
            st.experimental_rerun()

if __name__ == "__main__":
    main()
