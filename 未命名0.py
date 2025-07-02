import tkinter as tk
from tkinter import messagebox
import random
from functools import partial

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
        "answer": "C",
        "explanation": (
            "正確答案是 C。\n"
            "list_1 + list_2 結果為 [1, 2, 3, 4, 5, 6]。\n"
            "list_3 * 2 表示將串列重複兩次，\n"
            "所以結果是 [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]。"
        )
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
        "answer": "D",
        "explanation": (
            "正確答案是 D。\n"
            "(1) 使用 float 處理距離，保留小數點。\n"
            "(2)(3) 分與秒都需轉換為 int 才能計算。\n"
            "其他選項使用 string 或 int 錯誤會造成運算失敗或精度不足。"
        )
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
        "answer": "C",
        "explanation": (
            "正確答案為 C。\n"
            "age = 12 → int\n"
            "minor = False → bool\n"
            "name = \"David\" → str\n"
            "weight = 64.5 → float\n"
            "zip = \"545\" → str（雖然是數字，但有引號，代表是字串）"
        )
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
        "answer": "A",
        "explanation": (
            "✅ 正確答案是 A。\n"
            "- 在 01 和 02 行中，input() 回傳的是 str。\n"
            "- eval(year) 與 eval(age) 才會將字串轉為 int。\n"
            "- born 是 int，非 float。\n"
            "- message 是字串，非 bool。"
        )
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
    "answer": ["A", "B"],  # ✅ 改為陣列，多選題正確選項
    "multi": True  # ✅ 加入這個欄位來辨識這是多選題
}
    
]

random.shuffle(quiz_data)

current_question_index = 0
current_shuffled_options = []

def show_question():
    global current_shuffled_options
    question_data = quiz_data[current_question_index]

    options_list = list(question_data["options"].items())
    random.shuffle(options_list)
    current_shuffled_options = options_list

    question_label.config(text=question_data["question"])

    for i, (key, text) in enumerate(options_list):
        btn = option_buttons[chr(65 + i)]
        btn.config(
            text=f"({chr(65 + i)}) {text}",
            command=partial(check_answer, text)
        )

def check_answer(selected_text):
    global current_question_index
    question_data = quiz_data[current_question_index]

    correct_key = question_data["answer"]
    correct_text = question_data["options"][correct_key]

    correct_label = None
    for idx, (key, text) in enumerate(current_shuffled_options):
        if text == correct_text:
            correct_label = chr(65 + idx)
            break

    if selected_text == correct_text:
        messagebox.showinfo("答題結果", "✅ 答對了！")
    else:
        messagebox.showerror(
            "答題結果",
            f"❌ 答錯了！\n\n正確答案是：({correct_label}) {correct_text}"
        )

    current_question_index += 1
    if current_question_index < len(quiz_data):
        show_question()
    else:
        messagebox.showinfo("完成測驗", "🎉 你已完成所有題目！")
        root.destroy()

root = tk.Tk()
root.title("Python 隨機選擇題測驗（選項順序亂數）")
root.geometry("760x540")

question_label = tk.Label(root, text="", justify="left", wraplength=720, font=("Arial", 12))
question_label.pack(pady=20)

option_buttons = {}
for i in range(4):
    btn = tk.Button(root, text="", width=90, anchor="w", font=("Arial", 11))
    btn.pack(pady=5)
    option_buttons[chr(65 + i)] = btn

show_question()
root.mainloop()


