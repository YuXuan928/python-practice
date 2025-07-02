# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 14:16:12 2025

@author: 職前
"""

import streamlit as st

if "question_index" not in st.session_state:
    st.session_state.question_index = 0

def next_question():
    st.session_state.question_index += 1
    st.experimental_rerun()

st.write(f"Current question index: {st.session_state.question_index}")

if st.button("下一題"):
    next_question()

# 測驗題目資料結構
quiz_data = [
    {
        "question": "你編寫了以下的程式碼：\n"
                    "list_1 = [1, 2, 3]\n"
                    "list_2 = [4, 5, 6]\n"
                    "list_3 = list_1 + list_2\n"
                    "list_4 = list_3 * 2\n\n"
                    "print(list_4)\n\n"
                    "執行程式碼的輸出值是？",
        "options": {
            "A": "[[1, 2, 3], [4, 5, 6], [1, 2, 3], [4, 5, 61]",
            "B": "[4, 10, 18]",
            "C": "[1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]",
            "D": "[[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]]"
        },
        "answer": ["C"],
        "multi": False
    },
    {
        "question": "你是運動App的程式設計師。你必須製作一個函式為跑者計算步速，"
                    "所謂步速就是每公里所花的時間。輸出結果必須盡可能精準。\n\n"
                    "請選出以下空格應填入的函式名稱：\n\n"
                    "#步速計算器\n"
                    "distance = ___(1)___ (input(\"Enter the distance traveled in meters\"))\n"
                    "distance_kms = distance / 1000  # convert to kilometers\n"
                    "time_minute = ___(2)___ (input(\"Enter the time elapsed in minutes\"))\n"
                    "time_sec = ___(3)___ (input(\"Enter the time elapsed in seconds\"))\n"
                    "time = time_minute * 60 + time_sec\n"
                    "pace = time / distance_kms\n"
                    "print(\"The average velocity is\", str((pace//60)) + \" min \" + str((pace % 60)) + \" sec\")",
        "options": {
            "A": "(1) int  (2) int  (3) int",
            "B": "(1) string  (2) string  (3) string",
            "C": "(1) float  (2) string  (3) string",
            "D": "(1) float  (2) int  (3) int"
        },
        "answer": ["D"],
        "multi": False
    },
    {
        "question": "你正在編寫一個 Python 程式用來記錄客戶資料並將其儲存在資料庫中。\n"
                    "這個程式處理各種各樣的資料。以下的變數宣告後，它們的資料類別是？\n"
                    "請選出正確的型別配對：\n\n"
                    "🧿 age = 12\n"
                    "🧿 minor = False\n"
                    "🧿 name = \"David\"\n"
                    "🧿 weight = 64.5\n"
                    "🧿 zip = \"545\"",
        "options": {
            "A": "age: int, minor: bool, name: str, weight: float, zip: int",
            "B": "age: str, minor: bool, name: str, weight: float, zip: str",
            "C": "age: int, minor: bool, name: str, weight: float, zip: str",
            "D": "age: float, minor: str, name: int, weight: float, zip: int"
        },
        "answer": ["C"],
        "multi": False
    },
    {
        "question": "你正在編寫一個計算使用者出生年份的程式。\n"
                    "該程式詢問使用者的年齡和當前年份，然後輸出使用者的出生年份。\n"
                    "你編寫以下程式碼，其中行號僅供參考：\n\n"
                    "01 age = input(\"Enter your age: \")\n"
                    "02 year = input(\"Enter the four digit year: \")\n"
                    "03 born = eval(year) - eval(age)\n"
                    "04 message = \"You were born in \" + str(born)\n"
                    "05 print(message)\n\n"
                    "請問下列何者是正確的？",
        "options": {
            "A": "在 01 行中 year 的資料類型是 str",
            "B": "在 03 行中 born 的資料類型是 float",
            "C": "在 04 行中 message 的資料類型是 bool",
            "D": "在 05 行中 age 是 int 型態"
        },
        "answer": ["A"],
        "multi": False
    },
    {
        "question": "在 Python 資料類型的課程中創建以下三個程式碼片段：\n\n"
                    "# Code segment 1\n"
                    "x1 = \"5\"\n"
                    "y1 = 4\n"
                    "a = x1 * y1    # '5555'\n\n"
                    "# Code segment 2\n"
                    "x2 = 10\n"
                    "y2 = 4\n"
                    "b = x2 / y2    # 2.5\n\n"
                    "# Code segment 3\n"
                    "x3 = 5.5\n"
                    "y3 = 1\n"
                    "c = x3 / y3    # 5.5\n\n"
                    "你需要評估程式碼片段。請問下列何者是正確的？（可多選）",
        "options": {
            "A": "執行程式碼片段 1 後，變數 a 的資料類為 str。",
            "B": "執行程式碼片段 2 後，變數 b 的資料類型是 float。",
            "C": "執行程式碼片段 3 後，變數 c 的資料類型為 int。"
        },
        "answer": ["A", "B"],
        "multi": True
    },
    {
    "question": "在 Python 程式中我們利用 type() 查詢每個值的資料類別，\n"
                "以下的程式執行後出現的資料類別分別是：\n\n"
                "type(+1E10)\n"
                "type(5.0)\n"
                "type(\"True\")\n"
                "type(False)\n",
    "options": {
        "A": "int, int, bool, bool",
        "B": "float, float, str, bool",
        "C": "int, float, str, bool",
        "D": "float, int, str, str"
    },
    "answer": ["B"],   # ✅ 正確答案
    "multi": False      # ✅ 單選題
},
    {
    "question": "你加入了電子商務公司成為其程式開發部門的實習生。\n"
                "你的程式中有一個地方要讓使用者提供一個數值。\n"
                "即使使用者輸入了小數，該值也必須轉換為整數來進行計算。\n"
                "你應該使用哪個程式碼片段？",
    "options": {
        "A": "totalNums = input(\"How many items would you like?\")",
        "B": "totalNums = int(input(\"How many items would you like?\"))",
        "C": "totalNums = str(input(\"How many items would you like?\"))",
        "D": "totalNums float(input(\"How many items would you like?\"))"
    },
    "answer": ["B"],
    "multi": False
},
  
  {
    "question": "高年級的老師要製作一份報表來顯示這次考試班上所有學生的平均分數。\n"
                "報表必須去除平均分數的小數部分。每個正確的答案都提供了一個完整的解決方案。\n"
                "你應該使用哪兩個程式碼片段？（可多選）",
    "options": {
        "A": "average_score = float(total_score // number_of_students)",
        "B": "average_score = int(total_score / number_of_students)",
        "C": "average_score = float(total_score ** number_of_students)",
        "D": "average_score = total_score // number_of_students"
    },
    "answer": ["B", "D"],
    "multi": True
},
  {
    "question": "你編寫了以下的程式碼：\n"
                "a = 24\n"
                "b = 7\n"
                "ans = (a % b * 100) // 2.0 ** 3.0 - b\n"
                "print(ans)\n\n"
                "執行程式碼的輸出值是？",
    "options": {
        "A": "30.0",
        "B": "30.5",
        "C": "457",
        "D": "語法錯誤"
    },
    "answer": ["A"],
    "multi": False
},
  {
    "question": "你正在編寫 Python 程式用於計算一個數學公式。\n"
                "公式內容為 b 等於 a 加上 5，然後再平方，其中 a 是輸入的值，b 是結果。\n\n"
                "你設計了以下的程式碼片段：\n"
                "01 a = eval(input(\"Enter a number for the equation:\"))\n"
                "02 b =\n\n"
                "如何完成 02 行的程式碼？",
    "options": {
        "A": "b = (a + 5)**2",
        "B": "b = a + 5 ** 2",
        "C": "b = a + 5 * 2",
        "D": "b = a + (5**2)"
    },
    "answer": ["A"],
    "multi": False
},
{
    "question": "你正在開發一個補習班的 Python 函式來計算折扣，補習班希望鼓勵小朋友和老年人報名，\n"
                "只要是小朋友和老年人報名相關課程就會獲得 10% 的折扣。\n"
                "你編寫了以下程式碼：\n\n"
                "01 def get_discount(kid, senior):\n"
                "02     discount = 0.1\n"
                "03     ???\n"
                "04         discount = 0\n"
                "05     return discount\n\n"
                "為了完成這個程式碼，你應該在 03 行加入什麼程式碼？",
    "options": {
        "A": "if not (kid or senior):",
        "B": "if (not kid) or senior:",
        "C": "if not (kid and senior):",
        "D": "if (not kid) and senior:"
    },
    "answer": ["A"],
    "multi": False
},
{
    "question": "你開發了一個比較數字的 Python 程式，下列何者的值是 True？（可複選）",
    "options": {
        "A": "0 or 5",
        "B": "bool(0)",
        "C": "None is None",
        "D": "-5 < 0 < 5"
    },
    "answer": ["C", "D"],
    "multi": True
},
{
    "question": "計算以下的 Python 數學運算式： (3*(1+2)**2 - 2**2*3) 結果為何？",
    "options": {
        "A": "3",
        "B": "13",
        "C": "15",
        "D": "69"
    },
    "answer": ["C"],
    "multi": False
},
{
    "question": "你編寫了以下的程式碼：\n"
                "a = 'Test 1'\n"
                "print(a)\n"
                "b = 'Test2'\n"
                "a += b\n"
                "print(a)\n"
                "print(b)\n\n"
                "根據程式碼片段選擇每個問題的答案：\n"
                "(1) 第一次 print() 輸出為？\n"
                "(2) 第二次 print() 輸出為？\n"
                "(3) 第三次 print() 輸出為？",
    "options": {
        "A": "(1) Test 1, (2) Test 1, (3) Test 1",
        "B": "(1) Test 1, (2) Test 1Test2, (3) Test2",
        "C": "(1) Test2, (2) Test 1Test2, (3) Test2",
        "D": "(1) Test 1, (2) Test2, (3) Test 1Test2"
    },
    "answer": ["B"],
    "multi": False
},
{
    "question": "高年級的老師要製作一份報表來顯示這次考試班上所有學生的平均分數。\n"
                "報表必須去除平均分數的小數部分。\n"
                "每個正確的答案都提供了一個完整的解決方案。\n"
                "你應該使用哪兩個程式碼片段？（可複選）",
    "options": {
        "A": "average_score = float(total_score // number_of_students)",
        "B": "average_score = int(total_score / number_of_students)",
        "C": "average_score = float(total_score ** number_of_students)",
        "D": "average_score = total_score // number_of_students"
    },
    "answer": ["B", "D"],
    "multi": True
},
{
    "question": "請按先後順序從頭至尾排列這六類運算的正確順序：\n"
                "加法和減法(+, -)\n"
                "乘法和除法(*, /)\n"
                "正數 (+)、負數 (-) 與反位元 (not)\n"
                "括弧\n"
                "指數 (**)\n"
                "且 (and)",
    "options": {
        "A": "加法和減法 -> 乘法和除法 -> 正數、負數與反位元 -> 括弧 -> 指數 -> 且",
        "B": "括弧 -> 指數 -> 正數、負數與反位元 -> 乘法和除法 -> 加法和減法 -> 且",
        "C": "指數 -> 乘法和除法 -> 正數、負數與反位元 -> 括弧 -> 且 -> 加法和減法",
        "D": "乘法和餘法 -> 括弧 -> 正數、負數與反位元 -> 指數 -> 且 -> 加法和減法"
    },
    "answer": ["B"],
    "multi": False
},
 {
    "question": "租車公司需要一種方法來決定客戶租用車輛的費用。\n"
                "費用結構如下所示：\n"
                "• 每天 100 美元\n"
                "• 如果車輛在晚上11點後返還，收取額外一天費用\n"
                "• 如果在星期天租車，享有 10% 折扣\n"
                "• 如果在星期四租車，享有 20% 折扣\n\n"
                "請問如何正確填入以下程式碼中的條件判斷？\n\n"
                "# 車輛出租計算機\n"
                "ontime = input(\"Was car returned before 11 pm? y or n\").lower()\n"
                "days_rented = int(input(\"How many days was car rented?\"))\n"
                "day_rented = input(\"What day was the car rented?\").capitalize()\n"
                "cost_per_day = 100\n"
                "if ontime _____ (1)______     # 不準時\n"
                "    days_rented += 1\n"
                "if day_rented _____(2)_____    # 星期天租的\n"
                "    total = (days_rented * cost_per_day) * 0.9\n"
                "elif day_rented _____(3)_____  # 星期四租的\n"
                "    total = (days_rented * cost_per_day) * 0.8\n"
                "else:\n"
                "    total = days_rented * cost_per_day\n"
                "print(\"Cost of the car rental is : $\", total)",
    "options": {
        "A": "(1) != \"n\":  (2) == \"Sunday\":  (3) == \"Thursday\"",
        "B": "(1) == \"n\":  (2) >= \"Sunday\":  (3) <= \"Thursday\"",
        "C": "(1) == \"y\":  (2) is \"Sunday\":  (3) is \"Thursday\""
    },
    "answer": ["A"],
    "multi": False
},
 {
    "question": "你設計了一個數學運算的 Python 程式，程式碼如下：\n"
                "a = 11\n"
                "b = 5\n\n"
                "請配對下列每個運算結果與對應的程式碼：\n\n"
                "結果區：\n"
                "1   🧿\n"
                "2   🧿\n"
                "2.2 🧿\n\n"
                "回答區：\n"
                "🧿 print(a / b)\n"
                "🧿 print(a // b)\n"
                "🧿 print(a % b)\n",
    "options": {
        "A": "1 ➝ print(a % b), 2 ➝ print(a // b), 2.2 ➝ print(a / b)",
        "B": "1 ➝ print(a // b), 2 ➝ print(a % b), 2.2 ➝ print(a / b)",
        "C": "1 ➝ print(a / b), 2 ➝ print(a // b), 2.2 ➝ print(a % b)",
        "D": "1 ➝ print(a // b), 2 ➝ print(a / b), 2.2 ➝ print(a % b)"
    },
    "answer": ["A"],
    "multi": False
},
 {
       "question": "12. 你設計了一個比較數字的 Python程式，内容如下：\n"
                   "01 n1 = eval(input(\"Please enter the first number:\"))\n"
                   "02 n2 = eval(input(\"Please enter the second number:\"))\n"
                   "03 if nl = n2:   \n"
                   "04    print(\"The two numbers are equal.\")\n"
                   "05 if n1 <= n2:\n"
                   "06    print(\"Number 1 is less than number 2.\")\n"
                   "07 if n1 > n2:\n"
                   "08    print(\"Number 1 is greater than number 2.\")\n"
                   "09 if n2 <> n1:  \n"
                   "10    print(\"The two numbers are the same.\")\n"
                   "針對下列每個敘述，如果正確就選擇Yes，否則請選擇 No。",
       "options": {
           "A": "在03行的語法是不正確的比較。",
           "B": "在06行的語法只有n1小於n2 會的出来。",
           "C": "在08行的語法只有n1大於n2 時才會列印出來。",
           "D": "在09行的語法是不正確的比較。"
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
                # 注意：這裡的 user_answers 是一個字典，q["answer"] 也是一個字典
                if user_answers == q["answer"]:
                    correct = True
            else:
                # 單選、多選用集合比較
                # 確保 user_answers 和 q["answer"] 都是可轉換為集合的類型
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
                        # 確保 user_answers.get(k) 存在且與正確答案不符
                        if user_answers.get(k) != v:
                            wrong_list.append(f"{k}: 正確答案是 {v}")
                    st.write("正確答案：")
                    for w in wrong_list:
                        st.write(w)
                else:
                    correct_str = ", ".join(q["answer"])
                    st.write(f"正確答案是：{correct_str}")

            st.session_state.q_index += 1
            # 將 st.experimental_rerun() 替換為 st.rerun()
            st.rerun()
    else:
        st.write(f"測驗完成！你的分數是 {st.session_state.score} / {len(quiz_data)}")
        if st.button("重新開始"):
            st.session_state.q_index = 0
            st.session_state.score = 0
            # 將 st.experimental_rerun() 替換為 st.rerun()
            st.rerun()

if __name__ == "__main__":
    main()

