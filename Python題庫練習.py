# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 11:31:23 2025

@author: 職前
"""

import tkinter as tk
from tkinter import messagebox
import random
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
   },
 {
    "question": "老閭要求你對以下程式碼除錯：\n"
                "x = 0\n"
                "while x < 4:\n"
                "    if  x % 4 == 0:\n"
                "        print(\"party\")\n"
                "    elif  x - 2 < 0:\n"
                "        print(\"cake\")\n"
                "    elif  x / 3 == 0:\n"
                "        print(\"greeting\")\n"
                "    else:\n"
                "        print(\"birthday\")\n"
                "    x = x + 1\n\n"
                "什麼將會輸出列印到螢幕上？",
    "options": {
        "A": "party     greeting   birthday   cake",
        "B": "party     cake      birthday   birthday",
        "C": "birthday  party      greeting   cake",
        "D": "birthday  greeting   party      cake"
    },
    "answer": ["B"],
    "multi": False
},
 {
    "question": "您正在撰寫一個 Python 程式評估算術公式。\n"
                "此公式描述 a 是先取得一個輸入值，而 b 等於 a 乘以 -1 之後再平方，\n"
                "所以 b 是結果。\n\n"
                "您所建立的程式碼片段如下（加上行號僅為參考之用）：\n"
                "01 a = eval(input(\"Enter a number for the equation: \"))\n"
                "02 b = □ □ □ □ □    （請選擇填空順序）\n\n"
                "程式碼片段：\n"
                "A. -      B. (      C. )      D. **      E. **2      F. 2      G. a",
    "options": {
        "A": "[A B C D E]",
        "B": "[B A G C E]",
        "C": "[B A C G E]",
        "D": "[A G C E F]"
    },
    "answer": ["B"],
    "multi": False
},
{
    "question": "您正在撰寫一個 Python 程式評估算術公式。\n"
                "此公式描述 a 是先取得一個輸入值，而 b 等於 a 乘以 -1 之後再平方，\n"
                "所以 b 是結果。\n\n"
                "您所建立的程式碼片段如下（加上行號僅為參考之用）：\n"
                "01 a = eval(input(\"Enter a number for the equation: \"))\n"
                "02 b = □ □ □ □ □    （請選擇填空順序）\n\n"
                "程式碼片段：\n"
                "A. -      B. (      C. )      D. **      E. **2      F. 2      G. a",
    "options": {
        "A": "[A B C D E]",
        "B": "[B A G C E]",
        "C": "[B A C G E]",
        "D": "[A G C E F]"
    },
    "answer": ["B"],
    "multi": False
},
{
    "question": "在下列的程式碼中：\n"
                "aList = [0, 1, 2, 3, 4]\n"
                "print(4 in aList)\n\n"
                "會輸出列印的內容？",
    "options": {
        "A": "4",
        "B": "5",
        "C": "True",
        "D": "False"
    },
    "answer": ["C"],
    "multi": False
},
{
    "question": "你為公司開發了一個 Python 應用程式，設計了以下的程式碼：\n\n"
                "aList = [\"a\", \"b\", \"c\", \"d\", \"e\"]\n"
                "bList = [1, 2, 3, 4, 5]\n"
                "print(aList is bList)    # False\n"
                "print(aList == bList)    # False\n"
                "aList = bList\n"
                "print(aList is bList)    # True\n"
                "print(aList == bList)    # True\n\n"
                "根據程式碼片段中提供的資訊，請判斷下列每個敘述是否正確：",
    "options": {
        "1": "在第一次 print() 後會顯示 True。",
        "2": "在第二次 print() 後會顯示 True。",
        "3": "在第三次 print() 後會顯示 True。",
        "4": "在第四次 print() 後會顯示 True。"
    },
    "answer": {
        "1": "No",
        "2": "No",
        "3": "Yes",
        "4": "Yes"
    },
    "multi": "yesno"
},
{
    "question": "你同事開發一個將產品名稱輸入到資料庫的程式，但每個存入的名稱字母順序都顛倒了。\n"
                "請你開發一個 Python 函式，將每個產品名稱以正確順序輸出。\n\n"
                "# 函式會反轉字串中的字元。\n"
                "# 以相反的順序返回新字串。\n"
                "def reverse_pname(backwards_pname):\n"
                "    forward_pname = ''\n"
                "    for index in ___(1)___:\n"
                "        forward_pname += ___(2)___\n"
                "    return forward_pname\n\n"
                "print(reverse_pname(\"klim\"))  # test case",
    "options": {
        "A": "(1) A.backwards_pname  (2) A.backwards_pname[index-1]",
        "B": "(1) B.len(backwards_pname)  (2) B.backwards_pname[len(forward_pname)-1]",
        "C": "(1) C.range(0, len(backwards_pname), -1)  (2) C.backwards_pname[len(backward_pname)-len(forward_pname)]",
        "D": "(1) D.range(len(backwards_pname)-1, -1, -1)  (2) D.backwards_pname[index]"
    },
    "answer": ["D"],
    "multi": False
},

{
    "question": "你寫了一段程式碼要練習字串切片：\n\n"
                "alph = \"abcdefghijklmnopqrstuvwxyz\"\n\n"
                "請問下列每個切片操作的結果是什麼？請配對正確的對應關係：\n\n"
                "(1) alph[3:15]         ➝ ？\n"
                "(2) alph[3:15:3]       ➝ ？\n"
                "(3) alph[15:3:-3]      ➝ ？\n"
                "(4) alph[::-3]         ➝ ？",
    "options": {
        "A": "(4) ➝ zwtqnkheb",
        "B": "(3) ➝ pmjg",
        "C": "(1) ➝ defghijklmno",
        "D": "(2) ➝ dgjm"
    },
    "answer": ["A", "B", "C", "D"],
    "multi": True
},
{
        "question": "6. 你為學校設計了一個Python 應用程式，在classroom的清單中包含了60位同學的姓名，最後3名是班上的幹部。你需要分割清單內容顯示除了幹部以外的所有同學，你可以利用以下哪二個程式碼達成？",
        "options": {
            "A": "classroom[0:-2]",
            "B": "classroom[0:-3]",
            "C": "classroom[1:-3]",
            "D": "classroom[:-3]",
            "E": "classroom[1:-3]"
        },
        "answer": ["B", "D"],
        "multi": True
    },
{
        "question": "7. 你開發了一個 Python 應用程式，其中有一個名為month的清單儲存所有月份的英文。你要分割這個清單，取得由第二個月份開始，每間隔一個值的月份名稱，你應該使用哪個程式碼？\n\n#「::2」表示要「間隔2個項目」取值",
        "options": {
            "A": "month[2:2]",
            "B": "month[::2]",
            "C": "month[1::2]",
            "D": "month[1:2]"
        },
        "answer": ["C"],
        "multi": False
    },

    {
        "question": "8. 你設計了一個函式來執行除法，因為除法的除數不能為零，所以在函式中必須要針對這個重點進行檢查。你要如何完成這段程式碼？請在回答區選擇適當的程式碼片段。\n\n"
                    "def safe_divide(numerator, denominator):  # numerator 分子； denominator分母\n"
                    "    ___(1)___\n"
                    "        print(\"A required value is missing.\")\n"
                    "    ___(2)___\n"
                    "        print(\"The denominator is zero.\")\n"
                    "    else:\n"
                    "        return numerator / denominator\n\n"
                    "(A)(1) 選擇：\n"
                    "A. if numerator is None or denominator is None:\n"
                    "B. if numerator is None and denominator is None:\n"
                    "C. if numerator = None or denominator = None:\n"
                    "D. if numerator - None and denominator = None:\n\n"
                    "(A)(2) 選擇：\n"
                    "A. elif denominator == 0:\n"
                    "B. elif denominator = 0:\n"
                    "C. elif denominator != 0:\n"
                    "D. elif denominator in 0:",
        "options": {
            "A1": "if numerator is None or denominator is None:",
            "B1": "if numerator is None and denominator is None:",
            "C1": "if numerator = None or denominator = None:",
            "D1": "if numerator - None and denominator = None:",
            "A2": "elif denominator == 0:",
            "B2": "elif denominator = 0:",
            "C2": "elif denominator != 0:",
            "D2": "elif denominator in 0:"
        },
        "answer": ["A1", "A2"],
        "multi": True
    },
{
        "question": "9. 您建立了下列程式來找出學生並顯示姓名。加上行號僅為參考之用。\n"
                    "01 students = {1: 'Jone', 2: 'Mary'}\n"
                    "02 student = input('Enter the student id: ')\n"
                    "03 if not student in students:   #需轉int；int(student)\n"
                    "04    print('The student does not exist.')\n"
                    "05 else:\n"
                    "06    print(\"The student name is \" + students[student])\n\n"
                    "同事回報指出,這個程式有時候產生的結果不正確，請回答以下問題：\n"
                    "(A)(1)請問哪兩種資料型態儲存在第01行的students中？\n"
                    "A. 整數和字串\n"
                    "B. 整數和浮點數\n"
                    "C. 字串和浮點數\n"
                    "D. 字串和布林值\n\n"
                    "(C)(2)第02行的student是哪種資料型態？\n"
                    "A. int\n"
                    "B. float\n"
                    "C. string\n"
                    "D. bool\n\n"
                    "(B)(3)為什麼第03行找不到學生？\n"
                    "A. 語法不正確\n"
                    "B. 不符合的資料型態\n"
                    "C. 變數命名錯誤",
        "options": {
            "A1": "整數和字串",
            "B1": "整數和浮點數",
            "C1": "字串和浮點數",
            "D1": "字串和布林值",
            "A2": "int",
            "B2": "float",
            "C2": "string",
            "D2": "bool",
            "A3": "語法不正確",
            "B3": "不符合的資料型態",
            "C3": "變數命名錯誤"
        },
        "answer": ["A1", "C2", "B3"],
        "multi": True
    },
 {
        "question": "1. 老師正在設計一個 Python 程式，學生可以使用它來記錄他們考試的平均分數。該程式必須允許使用者輸入他們的名字和當前分數。該程式將輸出使用者名和使用者的平均分數。輸出必須符合以下要求：\n"
                    "- 使用者姓名必須是靠左對齊的。\n"
                    "- 如果使用者姓名少於20個字元，則必須在右側添加額外的空間。\n"
                    "- 平均分數在小數點左方是三位數，小數點右方是二位數。(XXX.XX)\n"
                    "你要如何完成程式碼？請在回答區中選擇適當的程式碼片段。\n\n"
                    "程式碼片段：\n"
                    "print(\"___ (1)___, your average is ___(2)___ \" % (name, average))\n\n"
                    "(D)(1) 選擇：\n"
                    "A. %-20i    B. %-20d    C. %-20f    D. %-20s\n"
                    "(B)(2) 選擇：\n"
                    "A. %1.6s    B. %6.2f    C. %6.2d    D. %2.6f",
        "options": {
            "A1": "%-20i",
            "B1": "%-20d",
            "C1": "%-20f",
            "D1": "%-20s",
            "A2": "%1.6s",
            "B2": "%6.2f",
            "C2": "%6.2d",
            "D2": "%2.6f"
        },
        "answer": ["D1", "B2"],
        "multi": True
    },
   {
       "question": "2. 你正在設計一個函式以讀取資料檔案並將結果列印為格式化表格。資料檔案中包含有關蔬菜的資訊。每個記錄都包含蔬菜的名稱、重量和價格。\n"
                   "你需要列印資料，使其看起來像下面的範例：\n"
                   "Potatos  5.4   2.33\n"
                   "Carrots  2.5   1.50\n"
                   "Corns   5.2   5.96\n\n"
                   "具體地說，列印輸出必須符合以下要求：\n"
                   "- 蔬菜名稱必須印在 10個空格範圍內並靠左對齊。\n"
                   "- 重量必須印在5個空格範圍內並靠右對齊，小數點最多一個位數。\n"
                   "- 價格必須印在7個空格範圍內並右對齊，小數點後最多兩位數。\n\n"
                   "你創建了以下的程式碼。其中包含的行號只是做為參考。\n"
                   "01 def print_table(file):\n"
                   "02     data = open(file,'r')\n"
                   "03     for record in data:\n"
                   "04         fields = record.split(\",\")\n"
                   "05         print(\"{} {} {}\".format(fields[0], eval(fields[1]), eval(fields[2])))  # 這行需改寫\n\n"
                   "請選擇適合完成第05行的程式碼片段，填入print裡面的格式化字串（四個空格分隔）：\n",
       "options": {
           "A": "{0:10}",   # 蔬菜名稱，10格寬靠左(預設左靠)
           "B": " ",        # 空白分隔符號
           "C": "{1:5.1f}", # 重量，5格寬靠右，小數點1位浮點數
           "D": " ",        # 空白分隔符號
           "E": "{2:7.2f}"  # 價格，7格寬靠右，小數點2位浮點數
       },
       "answer": ["A", "B", "C", "D", "E"],
       "multi": True
   },
   {
       "question": "3. 你正在設計一個電子商務程式，它可以接受來自使用者輸入，並以逗號分隔的格式輸出資料。你可以編寫以下程式碼接受資料輸入：\n"
                   "product = input(\"Enter product name: \")\n"
                   "qty = input(\"Input quantity: \")  # qty 是 string\n\n"
                   "輸出必須符合以下要求：\n"
                   "- 字串必須括在雙引號內。\n"
                   "- 數字不得用引號或其他字元括起來。\n"
                   "- 每個產品必須用逗號隔開。\n\n"
                   "你需要完成程式碼以符合要求。你應該使用哪三個程式碼片段？",
       "options": {
           "A": "print('\"{0}\", {1} '.format(product, qty))",
           "B": "print('\"' + product + '\", ' + str(qty))  # qty可以免 str( )，加也不會錯，只是多餘",
           "C": "print('\"%s\", %s' % (product, qty))",
           "D": "print(\"{0}, {1}\".format(product, qty))  # product沒有 '\"'",
           "E": "print(product + ', ' + qty)  # qty 須要改成 str(qty)，但product沒有 '\"'"
       },
       "answer": ["A", "B", "C"],
       "multi": True
   },
   {
        "question": "4. 請檢視下面的程式碼：\n"
                    "x = \"Tiger\"\n"
                    "y = \"Lion\"\n"
                    "z = \"Jaguar\"\n"
                    "animals = \"{1} and {0} and {2}\"\n"
                    "print(animals.format(x, y, z))\n"
                    "輸出的結果為？",
        "options": {
            "A": "Lion and Tiger and Jaguar",
            "B": "Lion and Jaguar and Tiger",
            "C": "Jaguar and Lion and Tiger",
            "D": "Tiger and Lion and Jaguar"
        },
        "answer": ["A"],
        "multi": False
    },
   {
        "question": "5. 你為公司設計 Python 應用程式，需要接受來自使用者的輸入並將該資訊列印到螢幕上。你的程式碼如下：\n"
                    "01 print(\"Enter product name:\")\n"
                    "02 \n"
                    "03 print(product_name)\n"
                    "在02行應該編寫哪個程式碼？",
        "options": {
            "A": "product_name = input()",
            "B": "input(product_name)",
            "C": "input(\"product_name\")",
            "D": "name = product_input"
        },
        "answer": ["A"],
        "multi": False
    },
   {
        "question": "6. 有一個旅行社需要一個簡單的程式用來輸入合作飯店及民宿的調查資料。程式必須接受輸入並返回基於五顆星規模的平均評等。輸出必須四捨五入到小數第二位。你必須完成這個程式碼以符合需求。請在回答區選擇適當的程式碼片段。注意：每個正確的選擇都可獲得一分。\n\n"
                    "sum = count = done = 0\n"
                    "average = 0.0\n"
                    "while (done != -1):\n"
                    "    rating = ___(1)___\n"
                    "    if rating == -1:\n"
                    "        break\n"
                    "    sum += rating\n"
                    "    count += 1\n"
                    "    average = float(sum / count)\n"
                    "    ___(2)___ + ___(3)___\n\n"
                    "(B)(1) 選擇：\n"
                    "A. print(\"Enter next rating (1-5), -1 for done\")\n"
                    "B. float(input(\"Enter next rating (1-5), -1 for done\"))\n"
                    "C. input(\"Enter next rating (1-5), -1 for done\")\n"
                    "D. input \"Enter next rating (1-5), -1 for done\")\n\n"
                    "(D)(2) 選擇：\n"
                    "A. output(\"The average star rating for this hotel is:\")\n"
                    "B. console.input(\"The average star rating for this hotel is:\")\n"
                    "C. printline(\"The average star rating for this hotel is:\")\n"
                    "D. print(\"The average star rating for this hotel is:\")\n\n"
                    "(A)(3) 選擇：\n"
                    "A. format(average, '.2f'))\n"
                    "B. format(average, '.2d'))\n"
                    "C. (average, '.2f')\n"
                    "D. format.average.(2d)",
        "options": {
            "A1": "print(\"Enter next rating (1-5), -1 for done\")",
            "B1": "float(input(\"Enter next rating (1-5), -1 for done\"))",
            "C1": "input(\"Enter next rating (1-5), -1 for done\")",
            "D1": "input \"Enter next rating (1-5), -1 for done\")",
            "A2": "output(\"The average star rating for this hotel is:\")",
            "B2": "console.input(\"The average star rating for this hotel is:\")",
            "C2": "printline(\"The average star rating for this hotel is:\")",
            "D2": "print(\"The average star rating for this hotel is:\")",
            "A3": "format(average, '.2f'))",
            "B3": "format(average, '.2d'))",
            "C3": "(average, '.2f')",
            "D3": "format.average.(2d)"
        },
        "answer": ["B1", "D2", "A3"],
        "multi": True
    },
{
        "question": "7. 你必須開發一個簡單的Python 檔案程式來執行以下動作：\n"
                    "檢查檔案是否存在。\n"
                    "・如果該檔案存在，就顯示檔案內容。\n"
                    "・如果該檔案不存在，就使用指定的名稱新增檔案。\n"
                    "・在檔案最後加入文字：\"End of file\"。\n"
                    "你需要完成程式碼以符合要求。請在回答區選擇適當的程式碼片段。每個正確的選擇可得一分。\n\n"
                    "import os\n"
                    "if ___(1)___:\n"
                    "    file = open('theFile.txt')\n"
                    "    ___(2)___     # 顯示檔案內容\n"
                    "    file.close()\n"
                    "file = ___(3)___     # 開檔\n"
                    "___(4)___ (\"End of file\")\n"
                    "file.close()",
        "options": {
            "A1": "isfile('theFile.txt')",
            "B1": "os.exist('theFile.txt')",
            "C1": "os.find('theFile.txt')",
            "D1": "os.path.isfile('theFile.txt')",

            "A2": "output(theFile.txt')",
            "B2": "print(file.get('theFile.txt'))",
            "C2": "print(file.read())",
            "D2": "print('theFile.txt')",

            "A3": "open('theFile.txt', 'a')",
            "B3": "open('theFile.txt', 'at')",
            "C3": "open('theFile.txt', 'w')",
            "D3": "open('theFile.txt', 'wt')",

            "A4": "Append",
            "B4": "file.add",
            "C4": "file.write",
            "D4": "write"
        },
        "answer": ["D1", "C2", "A3", "C4"],
        "multi": True
    },
{
        "question": "8. 你正在設計一個檔案的函式。如果檔案不存在，則返回”檔案不存在”。如果該檔案存在，則該函式返回第一行的內容。請完成以下程式碼，將程式碼片段按正確順序排列：\n\n"
                    "import os\n"
                    "def get_file_message(file):\n"
                    "    ___(1)___\n"
                    "        ___(2)___\n"
                    "            ___(3)___\n"
                    "    ___(4)___\n"
                    "        ___(5)___\n\n"
                    "程式碼片段選項：\n"
                    "A. with open(file, 'r') as file:\n"
                    "B. return \"File dose not exist\"\n"
                    "C. return file.readline()\n"
                    "D. if os.path.isfile(file):\n"
                    "E. else:",
        "options": {
            "A": "with open(file, 'r') as file:",
            "B": "return \"File dose not exist\"",
            "C": "return file.readline()",
            "D": "if os.path.isfile(file):",
            "E": "else:"
        },
        "answer": ["D", "A", "C", "E", "B"],
        "multi": True
    },
{
        "question": "9. 你設計一個Python 應用程式，需要將資料讀寫到文字檔中。如果檔案不存在，則必須新增它。如果檔案已有內容，則將文字加到最後。你應該使用哪個程式碼？",
        "options": {
            "A": "open(\"file_data\", \"a\")",
            "B": "open(\"file_data\", \"w\")",
            "C": "open(\"file_data\", \"rt\")",
            "D": "open(\"file_data\", \"r\")"
        },
        "answer": ["A"],
        "multi": False
    },
 {
        "question": "10. 你正在設計一個Python 程式來讀取學生資料的檔案，文件中包含了學生的班級、座號和姓名，下面顯示的是檔案中的資料範例：\n"
                    "'1A',  1,  'David'\n"
                    "'1A',  2,  'Mary'\n\n"
                    "程式碼必須符合以下需求：\n"
                    "- 檔案的每一行都必須讀取和列印。\n"
                    "- 如果遇到空行，則必須忽略。\n"
                    "- 在完成所有行的讀取後，必須關閉檔案。\n\n"
                    "你創建了以下程式碼(行號為參考)：\n"
                    "01 students = open(\"students.txt\", 'r')\n"
                    "02 eof = False\n"
                    "03 while eof == False:\n"
                    "04    line = students.readline()\n"
                    "05\n"
                    "06\n"
                    "07            print(line.strip())\n"
                    "08    else:\n"
                    "09        print(\"End of file\")\n"
                    "10        eof = True\n"
                    "11 students.close()\n\n"
                    "請問在05及06行你應該編寫哪些程式碼？",
        "options": {
            "A": "05  if line != '':\n    06  if line != \"\\n\":",
            "B": "05  if line = 'An':\n    06  if line != \"\":",
            "C": "05  if line!= != 'An':\n    06  if line != None:",
            "D": "05  if line != '':\n    06  if line != \"\":"
        },
        "answer": ["A"],
        "multi": False
    },
 
    {
        "question": "11. 某間公司需要有人協助更新他們的檔案系統。您必須建立一個執行下列動作的簡易檔案操作程式：\n"
                    "1. 查看檔案是否存在。\n"
                    "2. 如果檔案存在，則顯示其內容。\n"
                    "請選取正確的程式碼片段以完成程式碼。\n\n"
                    "import os\n"
                    "if ___(1)___:\n"
                    "    file = open('myFile.txt')\n"
                    "    ___(2)___\n"
                    "    file.close()\n",
        "options": {
            "A1": "os.path.isfile('myFile.txt')",
            "B1": "os.path.isexists('myFile.txt')",
            "C1": "os.path.isdir('myFile.txt')",
            "D1": "os.path.exists('myFile.txt')",
            "A2": "print(file.read())",
            "B2": "print(file.write())",
            "C2": "print(file.close())",
            "D2": "print(file,open())"
        },
        "answer": ["A1", "A2"],
        "multi": True
    },
    
    {
        "question": "12. 請問下列陳述式有何功能？\n\n"
                    "data = input()\n",
        "options": {
            "A": "允許使用者在主控台中輸入文字",
            "B": "建立 HTML 輸入元素",
            "C": "顯示電腦上的所有輸入周邊裝置",
            "D": "顯示允許使用者輸入的訊息方塊"
        },
        "answer": ["A"],
        "multi": False
    },
    {
       "question": "1. 你設計了一個程式要依學生的成績來顯示等級，它的規定如下：\n\n"
                   "Percentage range\tLetter grade\n"
                   "90 through 100\t\t\tA\n"
                   "80 through 89\tB\n"
                   "70 through 79\t\tC\n"
                   "60 through 69\t\tD\n"
                   "0 through 59\t\tF\n\n"
                   "例如，如果使用者輸入90，則輸出應該是「你的成績為甲等」，如果使用者輸入89，則輸出應該為「你的成績為乙等」。\n"
                   "你要如何完成這段程式碼？請在回答區選擇適當的程式碼片段。\n\n"
                   "# Letter Grade Converter\n"
                   "grade = int(input(\"Enter a numeric grade\"))\n"
                   "___(1)___   \n"
                   "letter_grade = 'A'\n"
                   "___(2)___   \n"
                   "letter_grade = 'B'\n"
                   "___(3)___   \n"
                   "letter_grade = 'C'\n"
                   "___(4)___   \n"
                   "letter_grade = 'D'\n"
                   "else: \n"
                   "    letter_grade = 'F'\n"
                   "print(\"Your letter grade is :\", letter_grade)",
       "options": {
           "A1": "if grade <= 90:",
           "B1": "if grade >= 90:",
           "C1": "elif grade > 90:",
           "D1": "elif grade >= 90:",
           "A2": "if grade > 80:",
           "B2": "if grade >= 80:",
           "C2": "elif grade > 80:",
           "D2": "elif grade >= 80:",
           "A3": "if grade > 70:",
           "B3": "if grade >= 70:",
           "C3": "elif grade > 70:",
           "D3": "elif grade >= 70:",
           "A4": "if grade > 60:",
           "B4": "if grade >= 60:",
           "C4": "elif grade > 60:",
           "D4": "elif grade >= 60:"
       },
       "answer": ["B1", "D2", "D3", "D4"],
       "multi": True
   },
]


random.shuffle(quiz_data)

current_question_index = 0
current_shuffled_options = []
current_check_vars = {}

def show_question():
    global current_shuffled_options, current_check_vars
    for widget in options_frame.winfo_children():
        widget.destroy()

    question_data = quiz_data[current_question_index]
    options_list = list(question_data["options"].items())
    random.shuffle(options_list)
    current_shuffled_options = options_list
    current_check_vars = {}

    question_label.config(text=question_data["question"])

    if question_data.get("multi") == "yesno":
        # Yes/No 判斷題
        for key, text in options_list:
            frame = tk.Frame(options_frame)
            frame.pack(fill="x", pady=5, anchor="w")
            label = tk.Label(frame, text=f"{key}. {text}", anchor="w", justify="left")
            label.pack(side="left")

            var = tk.StringVar(value="No")  # 預設 No
            yes_btn = tk.Radiobutton(frame, text="Yes", variable=var, value="Yes")
            yes_btn.pack(side="left", padx=10)
            no_btn = tk.Radiobutton(frame, text="No", variable=var, value="No")
            no_btn.pack(side="left")
            current_check_vars[key] = var

    elif question_data.get("multi", False):
        # 多選題
        for i, (key, text) in enumerate(options_list):
            var = tk.BooleanVar()
            chk = tk.Checkbutton(options_frame, text=f"({chr(65+i)}) {text}", variable=var, anchor="w", justify="left")
            chk.pack(fill="x", pady=2)
            current_check_vars[text] = var

    else:
        # 單選題
        selected = tk.StringVar()
        for i, (key, text) in enumerate(options_list):
            rdo = tk.Radiobutton(options_frame, text=f"({chr(65+i)}) {text}", variable=selected, value=text, anchor="w", justify="left")
            rdo.pack(fill="x", pady=2)
        current_check_vars["selected"] = selected


def submit_answer():
    global current_question_index
    question_data = quiz_data[current_question_index]
    is_multi = question_data.get("multi", False)

    if is_multi == "yesno":
        # Yes/No 判斷題
        user_answers = {key: var.get() for key, var in current_check_vars.items()}
        correct_answers = question_data["answer"]

        if user_answers == correct_answers:
            messagebox.showinfo("答題結果", "✅ 全部判斷正確！")
        else:
            wrong = []
            for key in correct_answers:
                if user_answers.get(key) != correct_answers[key]:
                    wrong.append(f"{key}: 正確答案是 {correct_answers[key]}")
            messagebox.showerror("答題結果", f"❌ 有錯誤！\n\n" + "\n".join(wrong))

    elif is_multi:
        # 多選題
        selected = [text for text, var in current_check_vars.items() if var.get()]
        correct_answers = [question_data["options"][key] for key in question_data["answer"]]

        if set(selected) == set(correct_answers):
            messagebox.showinfo("答題結果", "✅ 答對了！")
        else:
            correct_str = "\n".join(correct_answers)
            messagebox.showerror("答題結果", f"❌ 答錯了！\n\n正確答案是：\n{correct_str}")

    else:
        # 單選題
        selected = current_check_vars["selected"].get()
        correct_answer = question_data["options"][question_data["answer"][0]]

        if selected == correct_answer:
            messagebox.showinfo("答題結果", "✅ 答對了！")
        else:
            messagebox.showerror("答題結果", f"❌ 答錯了！\n\n正確答案是：\n{correct_answer}")

    current_question_index += 1
    if current_question_index < len(quiz_data):
        show_question()
    else:
        messagebox.showinfo("完成測驗", "🎉 你已完成所有題目！")
        root.destroy()

root = tk.Tk()
root.title("Python 測驗系統（單選 + 多選 + Yes/No）")
root.geometry("800x600")

question_label = tk.Label(root, text="", wraplength=760, justify="left", font=("Arial", 13))
question_label.pack(pady=20)

options_frame = tk.Frame(root)
options_frame.pack()

submit_btn = tk.Button(root, text="提交答案", command=submit_answer, font=("Arial", 12))
submit_btn.pack(pady=10)

show_question()
root.mainloop()
