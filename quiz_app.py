import streamlit as st

# 假設 quiz_data 在此檔案的某處被定義，例如：
quiz_data = [
    {"question": "Python 是一種什麼類型的語言？", "options": {"A": "編譯型", "B": "解釋型", "C": "組合型"}, "answer": ["B"], "multi": False},
    {"question": "以下哪些是 Python 的資料結構？", "options": {"A": "列表", "B": "字典", "C": "集合", "D": "陣列"}, "answer": ["A", "B", "C"], "multi": True},
    {"question": "以下哪個是 Python 的套件管理工具？", "options": {"A": "npm", "B": "pip", "C": "maven"}, "answer": ["B"], "multi": False},
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
       "question": "你設計了一個比較數字的 Python程式，内容如下：\n"
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
        "question": "你為學校設計了一個Python 應用程式，在classroom的清單中包含了60位同學的姓名，最後3名是班上的幹部。你需要分割清單內容顯示除了幹部以外的所有同學，你可以利用以下哪二個程式碼達成？",
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
        "question": "你開發了一個 Python 應用程式，其中有一個名為month的清單儲存所有月份的英文。你要分割這個清單，取得由第二個月份開始，每間隔一個值的月份名稱，你應該使用哪個程式碼？\n\n#「::2」表示要「間隔2個項目」取值",
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
        "question": "你設計了一個函式來執行除法，因為除法的除數不能為零，所以在函式中必須要針對這個重點進行檢查。你要如何完成這段程式碼？請在回答區選擇適當的程式碼片段。\n\n"
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
        "question": "您建立了下列程式來找出學生並顯示姓名。加上行號僅為參考之用。\n"
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
        "question": "老師正在設計一個 Python 程式，學生可以使用它來記錄他們考試的平均分數。該程式必須允許使用者輸入他們的名字和當前分數。該程式將輸出使用者名和使用者的平均分數。輸出必須符合以下要求：\n"
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
       "question": "你正在設計一個函式以讀取資料檔案並將結果列印為格式化表格。資料檔案中包含有關蔬菜的資訊。每個記錄都包含蔬菜的名稱、重量和價格。\n"
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
       "question": "你正在設計一個電子商務程式，它可以接受來自使用者輸入，並以逗號分隔的格式輸出資料。你可以編寫以下程式碼接受資料輸入：\n"
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
        "question": "請檢視下面的程式碼：\n"
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
        "question": "你為公司設計 Python 應用程式，需要接受來自使用者的輸入並將該資訊列印到螢幕上。你的程式碼如下：\n"
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
        "question": "有一個旅行社需要一個簡單的程式用來輸入合作飯店及民宿的調查資料。程式必須接受輸入並返回基於五顆星規模的平均評等。輸出必須四捨五入到小數第二位。你必須完成這個程式碼以符合需求。請在回答區選擇適當的程式碼片段。注意：每個正確的選擇都可獲得一分。\n\n"
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
        "question": "你必須開發一個簡單的Python 檔案程式來執行以下動作：\n"
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
        "question": "你正在設計一個檔案的函式。如果檔案不存在，則返回”檔案不存在”。如果該檔案存在，則該函式返回第一行的內容。請完成以下程式碼，將程式碼片段按正確順序排列：\n\n"
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
        "question": "你設計一個Python 應用程式，需要將資料讀寫到文字檔中。如果檔案不存在，則必須新增它。如果檔案已有內容，則將文字加到最後。你應該使用哪個程式碼？",
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
        "question": "你正在設計一個Python 程式來讀取學生資料的檔案，文件中包含了學生的班級、座號和姓名，下面顯示的是檔案中的資料範例：\n"
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
        "question": "某間公司需要有人協助更新他們的檔案系統。您必須建立一個執行下列動作的簡易檔案操作程式：\n"
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
       "question": "你設計了一個程式要依學生的成績來顯示等級，它的規定如下：\n\n"
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
    {
       "question": "你要設計一款以使用者年齡進行電影分級的程式，必須符合以下要求：\n"
                   "・任何 18 歲或以上的人會顯示「限制級」的訊息。\n"
                   "・任何 13 歲或以上但小於 18 歲的人會顯示「輔導級」的訊息。\n"
                   "・任何 12 歲或更年輕的人會顯示「普通級」的訊息。\n"
                   "・如果年齡未知，則會顯示「未知」的訊息。\n\n"
                   "請完成下列程式碼邏輯：\n\n"
                   "def get_rating(age):\n"
                   "    rating = \"\"\n"
                   "    if ___(1)___\n"
                   "        rating = \"未知\"\n"
                   "    elif ___(2)___\n"
                   "        rating = \"普通級\"\n"
                   "    elif ___(3)___\n"
                   "        rating = \"輔導級\"\n"
                   "    else ___(4)___\n"
                   "        rating = \"限制級\"\n"
                   "    return rating",
       "options": {
           "A1": "age < 13",
           "B1": "age < 18",
           "C1": ":",
           "D1": "age == None",

           "A2": "age < 13",
           "B2": "age < 18",
           "C2": ":",
           "D2": "age == None",

           "A3": "age < 13",
           "B3": "age < 18",
           "C3": ":",
           "D3": "age == None",

           "A4": "age < 13",
           "B4": "age < 18",
           "C4": ":",
           "D4": "age == None"
       },
       "answer": ["D1", "A2", "B3", "C4"],
       "multi": True
   },
    {
       "question": "你用學生的成績 (`grade`) 及排名 (`rank`) 編寫程式碼來決定最後成績：\n\n"
                   "```python\n"
                   "if grade > 80 and rank >= 3:\n"
                   "    grade += 10\n"
                   "if grade > 70 and rank > 3:\n"
                   "    grade += 5\n"
                   "else:\n"
                   "    grade -= 5  # 符合 76-5=71\n"
                   "```\n"
                   "當 `grade = 76`，`rank = 3` 時，執行程式碼的輸出值是？",
       "options": {
           "A": "71",
           "B": "76",
           "C": "81",
           "D": "86"
       },
       "answer": ["A"],
       "multi": False
   },
    {
        "question": "你正在編寫一個函式來判別負數與非負數。這個函式必須符合以下要求：\n"
                    "• 如果 `a` 是負數，則回傳 \"The result is a negative number\"\n"
                    "• 如果 `a` 不是負數，則為非負數，再繼續判別：\n"
                    "　‧ 如果 `a > 0`，則回傳 \"The result is a positive number\"\n"
                    "　‧ 否則回傳 \"The result is a zero\"\n\n"
                    "請完成下列函式內容：\n\n"
                    "```python\n"
                    "def reResult(a):\n"
                    "    ___(1)___\n"
                    "        answer = \"The result is a negative number\"\n"
                    "    ___(2)___\n"
                    "        ___(3)___\n"
                    "            answer = \"The result is a positive number\"\n"
                    "        ___(4)___\n"
                    "            answer = \"The result is a zero\"\n"
                    "    return answer\n"
                    "```\n",
        "options": {
            "A1": "if a < 0:",
            "B1": "if a > 0:",
            "C1": "else:",
            "D1": "elif:",

            "A2": "if a < 0:",
            "B2": "if a > 0:",
            "C2": "else:",
            "D2": "elif:",

            "A3": "if a < 0:",
            "B3": "if a > 0:",
            "C3": "else:",
            "D3": "elif:",

            "A4": "if a < 0:",
            "B4": "if a > 0:",
            "C4": "else:",
            "D4": "elif:"
        },
        "answer": ["A1", "C2", "B3", "C4"],
        "multi": True
    },
    {
       "question": "你設計了一個電影票收費的函式，票價的規則如下：\n"
                   "• 5歲以下 → 免費入場\n"
                   "• 5歲及以上的學生 → 60元\n"
                   "• 5歲到17歲但不是學生 → 120元\n"
                   "• 17歲以上但不是學生 → 180元\n\n"
                   "你要如何完成這段程式碼？請在回答區選擇適當的程式碼片段。\n\n"
                   "```python\n"
                   "def ticket_fee(age, school):\n"
                   "    fee = 0                # 5歲以下\n"
                   "    ___(1)___              # 若 5歲以上且是學生 → 60元\n"
                   "        fee = 60\n"
                   "    ___(2)___              # 若 5歲以上但不是學生：\n"
                   "        ___(3)___          # 若年齡小於等於17歲 → 120元\n"
                   "            fee = 120\n"
                   "        else:\n"
                   "            fee = 180\n"
                   "    return fee\n"
                   "```",
       "options": {
           "A1": "if age >= 5 and school == True:",
           "B1": "if age >= 5 and school == False:",
           "C1": "if age <= 17",

           "A2": "if age >= 5 and school == True:",
           "B2": "if age >= 5 and school == False:",
           "C2": "if age <= 17",

           "A3": "if age >= 5 and school == True:",
           "B3": "if age >= 5 and school == False:",
           "C3": "if age <= 17"
       },
       "answer": ["A1", "B2", "C3"],
       "multi": True
   },
 {
        "question": "你在設計一個 Python 程式遊戲，讓參加者從 1 到 100 之間猜一個數字，最多有三次機會。\n"
                    "以下是程式碼（部分內容不完整）：\n\n"
                    "01 from random import randint\n"
                    "02 target = randint(1, 100)\n"
                    "03 chance = 1\n"
                    "04 print(\"Guess an integer from 1 to 100. You will have 3 chances.\")\n"
                    "05 ___(A)___\n"
                    "06     guess = int(input(\"Guess an integer:\"))\n"
                    "07     if guess > target:\n"
                    "08         print(\"Guess is too high\")\n"
                    "09     elif guess < target:\n"
                    "10         print(\"Guess is too low\")\n"
                    "11     else:\n"
                    "12         print(\"Guess is just right\")\n"
                    "13         ___(B)___\n"
                    "14     ___(C)___\n\n"
                    "你應該如何完成第 05、13、14 行的程式碼？",
        "options": {
            "A": "while chance <= 3:",
            "B": "break",
            "C": "chance += 1",
            "D": "pass",
            "E": "while chance < 3",
            "F": "chance = 2"
        },
        "answer": ["A", "B", "C"],
        "multi": True
    },
{
        "question": "在以下的程式碼中，要加入哪些程式碼片段讓 `print()` 語法可以正確執行？\n"
                    "你要如何完成程式碼讓 `print()` 是有條件的正確輸出？請選出正確的條件控制語法片段。\n\n"
                    "```python\n"
                    "aList = [1, 2, 3]\n"
                    "bList = [\"a\", \"b\", \"c\"]\n"
                    "___(1)___\n"
                    "print(\"aList is equal to bList\")\n"
                    "___(2)___\n"
                    "print(\"aList is not equal to bList\")\n"
                    "```",
        "options": {
            "A1": "if aList == bList:",
            "B1": "if alist -= blist",
            "C1": "else:",
            "D1": "else",

            "A2": "if aList == bList:",
            "B2": "if alist == blist",
            "C2": "else:",
            "D2": "else"
        },
        "answer": ["A1", "C2"],
        "multi": True
    },
 {
        "question": "你設計了一個 Python 程式，用來檢查使用者輸入的英文姓名大小寫類型。\n"
                    "請從下列程式碼片段中選出 4 段，並按正確順序完成程式邏輯（檢查全大寫、全小寫或混合）。\n\n"
                    "程式碼片段：\n"
                    "A. name = input(\"Enter your English name:\")\n"
                    "B. elif name.lower() == name:\n    print(name, \"is all lower case.\")\n"
                    "C. else:\n    print(name, \"is upper case.\")\n"
                    "D. else:\n    print(name, \"is mixed case.\")\n"
                    "E. if name.upper() == name:\n    print(name, \"is all upper case.\")\n"
                    "F. else:\n    print(name, \"is lower case.\")\n\n"
                    "請選出正確的程式碼順序。",
        "options": {
            "A": "A. name = input(\"Enter your English name:\")",
            "B": "B. elif name.lower() == name:\n    print(name, \"is all lower case.\")",
            "C": "C. else:\n    print(name, \"is upper case.\")",
            "D": "D. else:\n    print(name, \"is mixed case.\")",
            "E": "E. if name.upper() == name:\n    print(name, \"is all upper case.\")",
            "F": "F. else:\n    print(name, \"is lower case.\")"
        },
        "answer": ["A", "E", "B", "D"],
        "multi": True
    },
   {
        "question": "公司決定要幫所有年薪不到50萬的員工調升基本工資5%，並給予獎金1萬元。\n"
                    "新工資 = 目前工資 × 1.05 + 10000。\n"
                    "程式會將每個人調整後的年薪資料存入 salaryList 清單中。\n"
                    "請完成下列程式碼片段：\n\n"
                    "```python\n"
                    "___(1)___            # for index in range(len(salary_list)):\n"
                    "if salaryList[index] >= 500000:\n"
                    "    ___(2)___        # continue\n"
                    "salaryList[index] = (salaryList[index] * 1.05) + 10000\n"
                    "```",
        "options": {
            "A1": "for index in range(len(salary_list) + 1):",
            "B1": "for index in range(len(salary_list) - 1):",
            "C1": "for index in range(len(salary_list)):",
            "D1": "for index in salary_list:",

            "A2": "exit()",
            "B2": "continue",
            "C2": "break",
            "D2": "end"
        },
        "answer": ["C1", "B2"],
        "multi": False
    },
        {
        "question": "你設計了一個函式 `times_tables()`，要列出從 2 到 9 的九九乘法表。\n"
                    "你需要選出正確的 `for` 迴圈條件來完成這段程式碼：\n\n"
                    "```python\n"
                    "# Displays times tables 2 - 9\n"
                    "def times_tables():\n"
                    "    ___(1)___            # for col in range(2, 10):\n"
                    "        ___(2)___        # for row in range(2, 10):\n"
                    "            print(row * col, end=\" \")\n"
                    "        print()\n"
                    "# main\n"
                    "times_tables()\n"
                    "```",
        "options": {
            "A1": "for col in range(9):",
            "B1": "for col in range(2, 10):",
            "C1": "for col in range(2, 9, 1):",
            "D1": "for col in range(10):",

            "A2": "for row in range(9):",
            "B2": "for row in range(2, 9, 1):",
            "C2": "for row in range(2, 10):",
            "D2": "for row in range(10):"
        },
        "answer": ["B1", "C2"],
        "multi": True
    },
        {
        "question": "你設計了一個 Python 程式來顯示 2 到 100 中的所有質數，請將左方程式碼片段依正確順序排列到右方回答區。\n\n"
                    "程式碼片段：\n"
                    "A. n = 2\n   is_prime = True\n   while n <= 100:\n"
                    "B. n = 2\n   while n <= 100:\n   is_prime = True\n"
                    "C. break\n"
                    "D. continue\n"
                    "E. n += 1\n"
                    "F. for i in range(2, n):\n       if n / i == 0:\n           is_prime = False\n"
                    "G. for i in range(2, n):\n       if n % i == 0:\n           is_prime = False\n\n"
                    "請排列回答區的正確順序（例如：B G C E）",
        "options": {
            "A": "A. n = 2\n   is_prime = True\n   while n <= 100:",
            "B": "B. n = 2\n   while n <= 100:\n   is_prime = True",
            "C": "C. break",
            "D": "D. continue",
            "E": "E. n += 1",
            "F": "F. for i in range(2, n):\n       if n / i == 0:\n           is_prime = False",
            "G": "G. for i in range(2, n):\n       if n % i == 0:\n           is_prime = False"
        },
        "answer": ["B", "G", "C", "E"],
        "multi": False
    },
        {
        "question": "你用 Python 設計一個比大小函式，功能如下：\n"
                    "• 有兩個參數，一個是整數清單 nums，一個是整數 num。\n"
                    "• 檢查清單中是否有比 num 大的整數，找到即印出訊息並停止搜尋。\n"
                    "• 若找不到比 num 大的數，印出找不到的訊息。\n\n"
                    "請依正確順序排列下列程式碼片段完成此函式：\n",
        "options": {
            "A": "for i in range(len(nums)):",
            "B": "if nums[i] > num:\n    print(\"A value greater than {0} is found in the list of {1}\".format(num, nums))",
            "C": "else:\n    print(\"A value greater than {0} cannot be found in the list of {1}\".format(num, nums))",
            "D": "break",
            "E": "def search(nums, num):"
        },
        "answer": ["E", "A", "B", "D", "C"],
        "multi": False
    },
      {
        "question": "你正在設計一個 Python 程式驗證產品編號。產品編號格式必須是 dd-dddd，只能包含數字和破折號。\n"
                    "如果格式正確，印出 True，否則印出 False。\n"
                    "請選擇正確的程式碼片段完成程式：\n\n"
                    "___(1)___         # product_no = \"sentinel\"\n"
                    "parts = \"\"\n"
                    "___(2)___         # while product_no != \"\":\n"
                    "___(3)___         # valid = False\n"
                    "product_no = input(\"Enter product number (dd-dddd): \")\n"
                    "parts = product_no.split('-')\n"
                    "if len(parts) == 2:\n"
                    "    if len(parts[0]) == 2 and len(parts[1]) == 4:\n"
                    "        if parts[0].isdigit() and parts[1].isdigit():\n"
                    "            ___(4)___   # valid = True\n"
                    "print(valid)",
        "options": {
            "A1": "product_no = \"\"",
            "B1": "product_no = \"sentinel\"",
            "A2": "while product_no != \"\" :",
            "B2": "while product_no != \"sentinel\" :",
            "A3": "valid = False",
            "B3": "valid = True",
            "A4": "valid = False",
            "B4": "valid = True"
        },
        "answer": ["B1", "A2", "A3", "B4"],
        "multi": True
    },
      {
        "question": "你設計 Python 程式，要從清單中逐一查看數字，遇到4時跳出迴圈。\n"
                    "請選擇正確的程式碼片段完成下列程式碼：\n\n"
                    "nList = [0, 1, 2, 3, 4, 5, 6, 6, 7, 8, 9]\n"
                    "index = 0\n"
                    "___(1)___ (index < 10):  # while\n"
                    "    print(nList[index])\n"
                    "    if nList[index] == 4:\n"
                    "        ___(2)___  # break\n"
                    "    else:\n"
                    "        ___(3)___  # index += 1\n",
        "options": {
            "A1": "while",
            "B1": "for",
            "C1": "if",
            "D1": "break",

            "A2": "while",
            "B2": "for",
            "C2": "if",
            "D2": "break",

            "A3": "continue",
            "B3": "break",
            "C3": "index += 1",
            "D3": "index = 1"
        },
        "answer": ["A1", "D2", "C3"],
        "multi": True
    },
      {
       "question": "您正在撰寫程式碼使用星號建立E字形。請選出適當的數字完成迴圈範圍，輸出為：\n"
                   "****\n*\n****\n*\n****\n\n"
                   "程式碼片段如下：\n\n"
                   "result_str = \"\"\n"
                   "for row in range(1, ___(1)___):\n"
                   "    for column in range(1, ___(2)___):\n"
                   "        if (row == 1 or row == 3 or row == 5):\n"
                   "            result_str = result_str + \"*\"\n"
                   "        elif column == 1:\n"
                   "            result_str = result_str + \"*\"\n"
                   "    result_str = result_str + \"\\n\"\n"
                   "print(result_str)",
       "options": {
           "A1": "3",
           "B1": "4",
           "C1": "5",
           "D1": "6",

           "A2": "3",
           "B2": "4",
           "C2": "5",
           "D2": "6"
       },
       "answer": ["D1", "C2"],
       "multi": True
   },

    {
        "question": "根據成績 grade (0~100)，傳回對應的字母成績：\n"
                    "90~100=A，80~89=B，70~79=C，其餘不及格。\n"
                    "請選擇正確的程式碼片段完成下列程式碼：\n\n"
                    "___(1)___ grade <= 100 and grade >= 0:\n"
                    "___(2)___ grade >= 90:\n"
                    "    print(\"Your grade is A.\")\n"
                    "___(3)___ grade >= 80:\n"
                    "    print(\"Your grade is B.\")\n"
                    "___(4)___ grade < 80 and grade > 69:\n"
                    "    print(\"Your grade is C.\")\n"
                    "___(5)___\n"
                    "    print(\"Your grade is failing.\")\n"
                    "___(6)___\n"
                    "    print(\"Invalid grade entered.\")",
        "options": {
            "A1": "if",
            "B1": "elif",
            "C1": "else if",
            "D1": "else",

            "A2": "if",
            "B2": "else",
            "C2": "elif",
            "D2": "else if",

            "A3": "if",
            "B3": "else",
            "C3": "elif",
            "D3": "else if",

            "A4": "if",
            "B4": "else",
            "C4": "elif",
            "D4": "else if",

            "A5": "if",
            "B5": "else",
            "C5": "elif",
            "D5": "else if",

            "A6": "if",
            "B6": "else",
            "C6": "elif",
            "D6": "else if"
        },
        "answer": ["A1", "C2", "C3", "C4", "B5", "B6"],
        "multi": True
    },
    {
       "question": "出版社想要檢查出版物中特定字母的數量，請完成以下函式，計算特定字母在字串清單中出現的次數。\n\n"
                   "# Function accepts list of words from a file\n"
                   "# word_list = [\"apple\", \"banana\", \"peach\", \"grape\"]\n"
                   "# and letter to search for.\n"
                   "# Returns count of a particular letter in that list.\n"
                   "def count_letter(letter_list, word_list):\n"
                   "    count = 0\n"
                   "    for ___(1)___:       # word in letter_list:\n"
                   "        if ___(2)___:    # letter in word:\n"
                   "            count += 1\n"
                   "    return count\n\n"
                   "word_list = []\n"
                   "# word_list is populated from a file. Code not shown.\n"
                   "letter = input(\"which letter would you like to count\")\n"
                   "letter_count = count_letter(letter, word_list)\n"
                   "print(\"There are: \", letter_count, \"instances of \" + letter)\n",
       "options": {
           "A1": "letter_list in word",
           "B1": "word in letter_list",
           "C1": "word == letter_list",
           "D1": "word is letter_list",

           "A2": "word is letter",
           "B2": "letter is word",
           "C2": "word in letter",
           "D2": "letter in word"
       },
       "answer": ["B1", "D2"],
       "multi": True
   },
   {
        "question": "學校要求你除錯以下程式碼，計算分數清單的總分與平均分。\n"
                    "已宣告：\n"
                    "scores = [80, 90, 75, 85]\n"
                    "count = 0\n"
                    "sum = 0\n\n"
                    "程式碼片段：\n"
                    "for index in range(__ (1) __):\n"
                    "    count += 1\n"
                    "    sum += scores[index]\n"
                    "average = ___(2)___\n"
                    "print(\"The total scores is:\", sum)\n"
                    "print(\"The average scores is:\", average)\n\n"
                    "請選擇正確的程式碼片段修正錯誤：",
        "options": {
            "A1": "size(scores):",
            "B1": "size(scores)-1:",
            "C1": "len(scores)+1:",
            "D1": "len(scores):",

            "A2": "sum/count",
            "B2": "sum**count",
            "C2": "sum*count",
            "D2": "sum//count"
        },
        "answer": ["D1", "A2"],
        "multi": True
    }, 
   {
       "question": "您正在撰寫一段程式碼，需求如下：\n"
                   "1. 允許使用者不斷輸入字詞。\n"
                   "2. 輸出每個字詞的字元數。\n"
                   "請選取正確的程式碼片段完成程式：\n\n"
                   "x = \"Hello World\"\n"
                   "___(1)___ x != \"QUIT\":\n"
                   "    num = 0\n"
                   "    ___(2)___ char ___(3)___ x:\n"
                   "        num += 1\n"
                   "    print(num)\n"
                   "    x = input(\"Enter a new word or QUIT to exit: \")",
       "options": {
           "A1": "while",
           "B1": "for",
           "C1": "if",
           "D1": "in",

           "A2": "while",
           "B2": "for",
           "C2": "if",
           "D2": "in",

           "A3": "while",
           "B3": "for",
           "C3": "if",
           "D3": "in"
       },
       "answer": ["A1", "B2", "D3"],
       "multi": True
   },
   {
        "question": "你在測試以下程式碼時發現錯誤。其中行號為參考：\n"
                    "01 numList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\n"
                    "02 i = 0\n"
                    "03 while (i < 10)\n"
                    "04   print(numList[i])\n"
                    "05\n"
                    "06   if numList[i] = 6\n"
                    "07       break\n"
                    "08    else:\n"
                    "09       i +=1\n\n"
                    "你需要更正 03 行和 06 行的程式碼。請選擇正確的程式碼片段：",
        "options": {
            "(1)03": {
                "A": "while (i < 10) :",
                "B": "while [i < 10]",
                "C": "while (i < 5) :",
                "D": "while [i < 5]"
            },
            "(2)06": {
                "A": "if numList[i] == 6",
                "B": "if numList[i] == 6:",
                "C": "if numList(i) = 6 :",
                "D": "if numList(i) !  6"
            }
        },
        "answer": {
            "(1)03": "A",
            "(2)06": "B"
        },
        "multi": False
    },
   {
        "question": "公司正將過去的進銷存程式碼轉移到 Python，以下哪個是正確的註解語法？",
        "options": {
            "A": "// Return the current revenue\ndef get_saletotal():\n    return saletotal",
            "B": "/* Return the current revenue */\ndef get_saletotal():\n    return saletotal",
            "C": "'Return the current revenue\ndef get_saletotal():\n    return saletotal",
            "D": "# Return the current revenue  #正確註解\ndef get_saletotal():\n    return saletotal"
        },
        "answer": ["D"],
        "multi": False
    },
   {
        "question": "你設計一個函式計算矩形面積，下列敘述判斷正確與否：\n"
                    "A. 第1到4行為註解，執行時會被忽略。\n"
                    "B. 第2和3行中的 # 符號非必填。\n"
                    "C. 第6行中的字串會被解釋為註解。\n"
                    "D. 第7行包含內嵌註解。\n\n"
                    "請針對每個敘述回答 Yes 或 No。",
        "options": {
            "A": ["Yes", "No"],
            "B": ["Yes", "No"],
            "C": ["Yes", "No"],
            "D": ["Yes", "No"]
        },
        "answer": {
            "A": "Yes",
            "B": "No",
            "C": "No",
            "D": "Yes"
        },
        "multi": False
    },
   {
       "question": "一家運動器材公司設計程式記錄跑步距離，以下為程式片段：\n"
                   "01 def get_name():\n"
                   "02    name = input(\"What is your name?\")\n"
                   "03    return name\n"
                   "04 def calc_calories(kms, calories_per_km):\n"
                   "05    calories = kms * calories_per_km\n"
                   "07    return calories\n"
                   "08 distance = int(input(\"How many kilometers did you run this week?\"))\n"
                   "09 burn_rate = 80  # 每公里燃燒卡路里數\n"
                   "10 runner = get_name()\n"
                   "11 calories_burned = calc_calories(distance, burn_rate)\n"
                   "12 print(runner, \", you burned about \", calories_burned, \"calories.\")\n\n"
                   "請問你會如何定義第01行與第04行的函式名稱與參數？",
       "options": {
           "A": "01 def get_name():",
           "B": "01 def get_name(runner):",
           "C": "01 def get name (name):",
           "D": "04 def calc_calories():",
           "E": "04 def calc calories(kms, burn_rate):",
           "F": "04 def calc_calories(kms, calories_per_km):"
       },
       "answer": ["A", "F"],
       "multi": True
   },
   {
        "question": "設計函式 calc_score，要求：\n"
                    "- 接收兩個參數：目前分數 current 和一個值 value\n"
                    "- 將 value 加到 current\n"
                    "- 返回新分數\n\n"
                    "請選擇正確的程式碼片段完成函式：\n\n"
                    "____(1)____   ____(2)____\n"
                    "    current += value\n"
                    "_____(3)_____",
        "options": {
            "(1)": {
                "A": "calc_score",
                "B": "def calc_score",
                "C": "return calc_score"
            },
            "(2)": {
                "A": "(current, value):",
                "B": "():",
                "C": "(current, value)",
                "D": "()"
            },
            "(3)": {
                "A": "pass current",
                "B": "return current",
                "C": "return",
                "D": "pass"
            }
        },
        "answer": {
            "(1)": "B",
            "(2)": "A",
            "(3)": "B"
        },
        "multi": False
    },
   {
       "question": "你設計一個函式用來增加遊戲中玩家得分。函式需求：\n"
                   "- points 如果未指定，預設為 1\n"
                   "- plus 是 True 時，points 需加倍\n\n"
                   "程式碼片段與敘述：\n"
                   "01 def add_score(score, plus, points): # 需修改\n"
                   "02    if plus == True:\n"
                   "03       points = points * 2\n"
                   "04    score = score + points\n"
                   "05    return score\n"
                   "06 points = 5\n"
                   "07 score = 10\n"
                   "08 new_score = add_score(score, True, points)\n\n"
                   "請判斷下列敘述正確與否：",
       "options": {
           "A": ["Yes", "No"],
           "B": ["Yes", "No"],
           "C": ["Yes", "No"],
           "D": ["Yes", "No"]
       },
       "answer": {
           "A": "Yes",
           "B": "Yes",
           "C": "No",
           "D": "No"
       }
   },
   {
        "question": "以下是計算薪水的函式 getpay，請判斷敘述是否正確：\n\n"
                    "def getpay(hours=40, rate=25, qty=0, qtyrate=0, salary=0):\n"
                    "    overtime = 0\n"
                    "    if qty > 0:\n"
                    "        return qty * qtyrate\n"
                    "    if salary > 0:\n"
                    "        pass\n"
                    "    if hours > 40:\n"
                    "        overtime = (hours - 40) * (1.5 * rate)\n"
                    "        return overtime + (40 * rate)\n"
                    "    else:\n"
                    "        return hours * rate\n\n"
                    "判斷以下敘述的正確性：",
        "options": {
            "A": ["Yes", "No"],  # 呼叫 getpay() 是否會發生錯誤
            "B": ["Yes", "No"],  # getpay(salary=5000) 不會回傳任何值
            "C": ["Yes", "No"]   # getpay(qty=500, qtyrate=4) 回傳值為 2000
        },
        "answer": {
            "A": "No",
            "B": "No",
            "C": "Yes"
        }
    },
   {
        "question": "請從下列選項選出正確答案，有關 Python 程式碼文件字串（docstring）\n\n"
                    "(1) 哪些字元代表文件字串的開頭和結尾？\n"
                    "A. 單引號 (')\n"
                    "B. 雙引號 (\")\n"
                    "C. 兩個雙引號 (\"\")\n"
                    "D. 三個雙引號 (\"\"\")\n\n"
                    "(2) 文件字串的標準位置在哪裡？\n"
                    "A. 在函式宣告區塊前\n"
                    "B. 緊接在函式標頭後面\n"
                    "C. 在函式宣告區塊後\n"
                    "D. 在程式的最後\n\n"
                    "(3) 如何列印函式的文件字串？\n"
                    "A. print(__doc__)\n"
                    "B. print(cube(doc))\n"
                    "C. print(cube.__doc__)\n"
                    "D. print(cube(docstring))",
        "options": {
            "1": ["A", "B", "C", "D"],
            "2": ["A", "B", "C", "D"],
            "3": ["A", "B", "C", "D"]
        },
        "answer": {
            "1": "D",
            "2": "B",
            "3": "C"
        },
        "multi": False
    },
   {
        "question": "請檢閱以下程式碼並判斷敘述正確與否：\n\n"
                    "01 def petstore(category, species, breed = \"none\"):\n"
                    "02     \"\"\"Display information about a pet.\"\"\"\n"
                    "03     print (f\"\\nYou have selected an animal from the {category} category.\")\n"
                    "04     if breed == \"none\":\n"
                    "05         print(f\"The {category} you selected is a {species}\")\n"
                    "06     else:\n"
                    "07         print(f\"The {category} you selected is a {species} {breed}\")\n"
                    "08         print(f\"\\nThe {category} would make a great pet!\")\n"
                    "...\n"
                    "14     petstore(category, species, breed)\n"
                    "17     petstore(breed = \"Maltese\", species = \"Canine\", category = \"dog\")\n"
                    "18     petstore(\"bird\", species=\"Scarlet Macaw\")\n\n"
                    "判斷下列敘述：\n"
                    "A. 此函式會傳回一個值。 \n"
                    "B. 第14和17行的函式呼叫無效。\n"
                    "C. 第16和18行的函式呼叫會產生錯誤。",
        "options": {
            "A": ["Yes", "No"],
            "B": ["Yes", "No"],
            "C": ["Yes", "No"]
        },
        "answer": {
            "A": "No",
            "B": "No",
            "C": "No"
        }
    },
   {
       "question": "學校活動夜的函式 roomAssignment 用來指派學生前往不同教室。\n"
                   "函式定義：\n"
                   "def roomAssignment(student, year):\n"
                   "    \"\"\"Assign rooms to students\"\"\"\n"
                   "    if year == 1:\n"
                   "        print(f\"\\n{student.title()}, please report to room 115\")\n"
                   "    elif year == 2:\n"
                   "        print(f\"\\n{student.title()}, please report to room 210\")\n"
                   "    elif year == 3:\n"
                   "        print(f\"\\n{student.title()}, please report to room 320\")\n"
                   "    elif year == 4:\n"
                   "        print(f\"\\n{student.title()}, please report to room 405\")\n"
                   "    elif year == 5:\n"
                   "        print(f\"\\n{student.title()}, please report to room 515\")\n"
                   "    else:\n"
                   "        print(f\"\\n{student.title()}, please report to room 625\")\n\n"
                   "以下哪些呼叫方式是正確的？請選擇兩個答案。",
       "options": {
           "A": "name = input(\"What is your name?\")\ngrade = 0\nwhile grade not in (1,2,3,4,5,6):\n    grade = int(input(\"What grade are you in (1-6)?\"))\nroomAssignment(name, year=grade)",
           "B": "name = input(\"What is your name?\")\ngrade = 0\nwhile grade not in (1,2,3,4,5,6):\n    grade = int(input(\"What grade are you in (1-6)?\"))\nroomAssignment(student, year)",
           "C": "roomAssignment(\"Sherlock Sassafrass\", 4)",
           "D": "roomAssignment(year=6, name=\"Minnie George\")"
       },
       "answer": ["A", "C"],
       "multi": True
   },
   {
        "question": "您為公司開發Python應用程式，想加入附註方便團隊成員了解。請問應採取哪種做法？",
        "options": {
            "A": "在任何程式碼片段的<!--和-->之間放置附註。",
            "B": "在任何一行的#後面放置附註。",
            "C": "在任何一行的//後面放置附註。",
            "D": "在任何程式碼片段的/**/之間置附註"
        },
        "answer": "B",
        "multi": False
    },
   {
        "question": "在程式中要使用 datetime 模組中 datetime 函式，並設定為替代名稱 dt，應該使用哪個導入語句？",
        "options": {
            "A": "from datetime as dt",
            "B": "from datetime import datetime as dt",
            "C": "import datetime from datetime as dt",
            "D": "import datetime.datetime as dt"
        },
        "answer": "B",
        "multi": False
    },
   {
        "question": "你設計一個讀取檔案後將檔案中的每一行列印出來的函式。程式碼如下：\n"
                    "01 def print_file(filename):\n"
                    "02    line = None\n"
                    "03    if os.path.isfile(filename):\n"
                    "04       data = open(filename, 'r')\n"
                    "05       for line in data:\n"
                    "06           print(line)\n\n"
                    "執行時，收到第03行的錯誤，原因是什麼？",
        "options": {
            "A": "你需導入os 模組。",
            "B": "path方法並不存在os模組中。",
            "C": "path物件中不存在isfile方法。",
            "D": "isfile 方法不接受一個參數。"
        },
        "answer": "A",
        "multi": False
    },
   {
       "question": "設計程式碼用來生成隨機整數，最小值為11，最大值為20。請選出可以達成此功能的兩種函式。",
       "options": {
           "A": "random.randrange(11, 21, 1)",
           "B": "random.randrange(11, 20, 1)",
           "C": "random.randint(11, 20)",
           "D": "random.randint(11, 21)"
       },
       "answer": ["A", "C"],
       "multi": True
   },
   {
       "question": "設計程式碼用來生成隨機整數，範圍是0到10（含0與10）。你應該使用哪個語法？",
       "options": {
           "A": "random.random()",
           "B": "random.randrange(0.0, 1.0)",
           "C": "random.randrange()",
           "D": "random.randint(0, 10)"
       },
       "answer": "D",
       "multi": False
   },
   {
        "question": "你設計程式碼來產生符合以下要求的隨機數字：\n"
                    "- 是2的倍數\n"
                    "- 最低數字為2\n"
                    "- 最高數字為50\n"
                    "請選出符合要求的兩個程式碼片段。",
        "options": {
            "A": "from random import randint\nprint(randint(1, 25) * 2)",
            "B": "from random import randint\nprint(randint(1, 50))",
            "C": "from random import randrange\nprint(randrange(2, 50, 2))  # 50改成51才包含50",
            "D": "from random import randrange\nprint(randrange(2, 50, 1))"
        },
        "answer": ["A", "C"],
        "multi": True
    },
   {
        "question": "你正在設計一個處理數字的函式。要求：\n"
                    "- 將浮點數傳遞到函式中\n"
                    "- 取浮點數的絕對值\n"
                    "- 無條件進位到整數\n"
                    "請問你應該使用哪兩個數學函式？",
        "options": {
            "A": "math.fabs(x)",
            "B": "math.floor(x)",
            "C": "math.fmod(x)",
            "D": "math.ceil(x)",
            "E": "math.frexp(x)"
        },
        "answer": ["A", "D"],
        "multi": True
    },
   {
        "question": "您正在撰寫一個程式來顯示 My Healthy Eats Delivery 的特價優惠。\n\n"
                    "請選出正確的語法以完成程式碼第 04、05、15 行：\n"
                    "程式部分如下：\n"
                    "01 import datetime\n"
                    "02 dailySpecials = (\"Spaghetti\", \"Macaroni & Cheese\", \"Meatloaf\", \"Fried Chicken\")\n"
                    "03 weekendSpecials = (\"Lobster\", \"Prime Rib\", \"Parmesan-Crusted Cod\")\n"
                    "04 ___(1)___  # 擷取目前的日期時間\n"
                    "05 ___(2)___  # 擷取今天是星期幾\n"
                    "...\n"
                    "15 ___(3)___  # 計算本週剩餘天數",
        "options": {
            "A": "04行 ➜ now = datetime.datetime.now()",
            "B": "04行 ➜ now = datetime.datetime.today()",
            "C": "04行 ➜ now = datetime.datetime.day()",
            "D": "04行 ➜ now = datetime.datetime()",
            "E": "05行 ➜ today = now.strftime(\"%A\")",
            "F": "05行 ➜ today = now.strftime(\"%B\")",
            "G": "05行 ➜ today = now.strftime(\"*\")",
            "H": "05行 ➜ today = now.strftime(\"SY\")",
            "I": "15行 ➜ daysLeft = now.weekday()",
            "J": "15行 ➜ daysLeft = 6 - now.weekday()",
            "K": "15行 ➜ daysLeft = 6 + now.weekday()",
            "L": "15行 ➜ daysLeft = 6 + now.week()"
        },
        "answer": ["A", "E", "J"],  # 對應 04, 05, 15 行
        "multi": True
    },
   {
       "question": "你設計一個指派房間與組別的 Python 程式：\n\n"
                   "import random\n\n"
                   "roomsAssigned = [1]\n"
                   "room_number = 1\n"
                   "groupList = [\"Ropes\", \"Rafting\", \"Obstacle\", \"Wellness\"]\n"
                   "...\n"
                   "while room_number in roomsAssigned:\n"
                   "    ___(1)___\n"
                   "...\n"
                   "group = ___(2)___\n\n"
                   "你應該如何完成這段程式碼？",
       "options": {
           "A": "(1) room_number = random.randint(1, 50)",
           "B": "(1) room_number = random.random(1, 50)",
           "C": "(2) random.choice(groupList)",
           "D": "(2) random.shuffle(groupList)"
       },
       "answer": ["A", "C"],
       "multi": True
   },
   {
        "question": "在下列的語法敘述中，如果是正確的就選擇 Yes，否則請選擇 No：\n\n"
                    "A. 在 try 語法中可以有不只一個 except 子句。\n"
                    "B. 在 try 語法中可以不加 except 子句。\n"
                    "C. 在 try 語法中可以有一個 finally 子句與 except 子句。\n"
                    "D. 在 try 語法中可以有不只一個 finally 子句。",
        "options": {
            "A": "A. 是 Yes",
            "B": "B. 是 Yes",
            "C": "C. 是 Yes",
            "D": "D. 是 No"
        },
        "answer": ["A", "B", "C", "D"],
        "multi": True
    },
   {
        "question": "你製作一個程式詢問使用者家中有多少個小孩，使用者必須輸入整數。\n"
                    "如果輸入值不是整數，程式碼必須指出並要求重新輸入。\n"
                    "你要如何完成程式碼？請選擇適當的程式碼片段完成下列程式碼：\n\n"
                    "while True:\n"
                    "    ___(1)___\n"
                    "        x = int(input(\"How many children do you have? \"))\n"
                    "        break\n"
                    "    ___(2)___ ValueError:\n"
                    "        print(\"Please make sure you entered an integer, please try again...\")",
        "options": {
            "A": "(1) try:",
            "B": "(1) else:",
            "C": "(2) except",
            "D": "(2) raise",
            "E": "(1) finally:"
        },
        "answer": ["A", "C"],
        "multi": True
    },
   {
        "question": "關於 `assert` 方法的敘述，請選擇正確的配對方式：\n\n"
                    "(1) 若要測試變數 x 與 y 的值是否相同，可以使用：？\n"
                    "(2) 若要測試物件 x 與 y 是否為同一個實體，可以使用：？\n"
                    "(3) 若要測試清單中是否存在某個值，可以使用：？",
        "options": {
            "A": "(1) ➝ assertEqual(x, y)",
            "B": "(2) ➝ assertIs(x, y)",
            "C": "(3) ➝ assertIn(x, y)",
            "D": "(1) ➝ assertIsInstance(x, y)",
            "E": "(2) ➝ assertEqual(x, y)"
        },
        "answer": ["A", "B", "C"],
        "multi": True
    },
   {
        "question": "你需要測試某個物件是否為特定類別的執行個體，請問如何進行單元測試？\n"
                    "請依照下列註解提示選出正確的程式碼片段配對：\n\n"
                    "___(1)___ unittest      # 導入 unittest 模組\n"
                    "class TestIsInstance(___(2)___):  # 所有單元測試的類別應繼承 unittest.TestCase\n"
                    "    def ___(3)___:   # 測試方法名稱應以 test_ 開頭\n"
                    "        ___(4)___    # 測試是否為指定類別的實例\n"
                    "if __name__ == \"__main__\":\n"
                    "    unittest.main()",
        "options": {
            "A": "(1) ➝ from",
            "B": "(1) ➝ include",
            "C": "(1) ➝ import",
            "D": "(1) ➝ use",
            "E": "(2) ➝ TestCase",
            "F": "(2) ➝ unittest.TestCase",
            "G": "(2) ➝ unittest",
            "H": "(2) ➝ TestCase.unittest",
            "I": "(3) ➝ test isInstance()",
            "J": "(3) ➝ isInstance()",
            "K": "(3) ➝ test_isInstance(self)",
            "L": "(3) ➝ isInstance(self)",
            "M": "(4) ➝ assertIsInstance(obj, cls, msg=None)",
            "N": "(4) ➝ self.assertIsInstance(obj, cls, msg-None)",
            "O": "(4) ➝ assertIsInstance(obj, cls)",
            "P": "(4) ➝ self.assertIsInstance(obj, cls)"
        },
        "answer": ["C", "F", "K", "P"],
        "multi": True
    },
   {
        "question": "您需要撰寫執行下列工作的程式碼：\n"
                    "1. 呼叫 process() 函式。\n"
                    "2. 如果 process() 函式回傳錯誤，則呼叫 logError() 函式。\n"
                    "3. 呼叫 process() 函式之後一律呼叫 displayResult() 函式。\n"
                    "請選擇正確的程式碼區塊標籤以完成以下程式碼：\n\n"
                    "___(1)___:\n"
                    "    process()\n"
                    "___(2)___:\n"
                    "    logError()\n"
                    "___(3)___:\n"
                    "    displayResult()",
        "options": {
            "A": "(1) assert\n(2) raise\n(3) finally",
            "B": "(1) raise\n(2) except\n(3) try",
            "C": "(1) except\n(2) try\n(3) finally",
            "D": "(1) try\n(2) except\n(3) finally",
            "E": "(1) finally\n(2) except\n(3) try"
        },
        "answer": ["D"],
        "multi": False
    },
   {
        "question": "下列函式會計算使用指數之運算式的值。加上行號僅為參考之用：\n\n"
                    "01 def calc_power(a, b):\n"
                    "02    return a**b\n"
                    "03 base = input(\"Enter the number for the base: \")         #需加eval(…) 或 int( …)\n"
                    "04 exponent = input(\"Enter the number for the exponent: \")  #需加eval(…) 或 int( …)\n"
                    "05 result = calc_power(base, exponent)\n"
                    "06 print(\"The result is \" + result)  #加 str()\n\n"
                    "針對下列敘述，請判斷是否正確：\n",
        "options": {
            "A": "第02行會造成執行階段錯誤。",
            "B": "第06行會造成執行階段錯誤。",
            "C": "eval函式應該用於第03和04行"
        },
        "answer": ["A", "B", "C"],
        "multi": True,
        "option_type": "YesNo"  # 表示選項需用 Yes / No 判斷 (可在UI中調整呈現)
    },
   {
        "question": 
            "您撰寫了以下這段程式碼：\n\n"
            "import sys\n"
            "try:\n"
            "    file_in = open(\"in.txt\", 'r')       \n"
            "    file_out = open(\"out.txt\", 'w+')  \n"
            "except IOError:\n"
            "    print('cannot open', file_name)\n"
            "else:\n"
            "    i = i + 1\n"
            "    for line in file_in:\n"
            "        print (line.rstrip())  \n"
            "        file_out.write(\"line \"+ str(i) + \": \"+ line)  \n"
            "        i = i + 1\n"
            "    file_in.close ()\n"
            "    file_out.close ()\n"
            "\n"
            "假設 out.txt 檔案不存在，執行此程式碼，請判斷以下敘述是否正確？\n"
            "請針對每個敘述選擇 Yes 或 No。\n",
        "options": {
            "A": "此程式碼將正常執行，不會發生錯誤。",
            "B": "此程式碼將執行，但會產生邏輯錯誤。",
            "C": "此程式碼將產生執行階段錯誤。",
            "D": "此程式碼將產生語法錯誤。"
        },
        "answer": ["A"],  # 根據你的標示，A 是正確，其他均為錯誤
        "multi": True,
        "option_type": "YesNo"
    }   
]

def main():
    st.title("Python 程式測驗系統")

    if "score" not in st.session_state:
        st.session_state.score = 0
    if "q_index" not in st.session_state:
        st.session_state.q_index = 0
    if "answered" not in st.session_state:
        st.session_state.answered = False

    if st.session_state.q_index >= len(quiz_data):
        st.success(f"你已完成全部測驗！總分：{st.session_state.score} / {len(quiz_data)}")
        if st.button("重新開始"):
            st.session_state.q_index = 0
            st.session_state.score = 0
            st.session_state.answered = False
        return

    question = quiz_data[st.session_state.q_index]

    st.markdown(f"### 題目 {st.session_state.q_index + 1}:")
    st.write(question["question"])

    user_answers = []

    if question.get("multi", False):
        # 多選題: checkbox
        for key, option_text in question["options"].items():
            checked = st.checkbox(f"{key}: {option_text}", key=f"{st.session_state.q_index}_{key}")
            if checked:
                user_answers.append(key)
    else:
        # 單選題: radio
        choice = st.radio(
            "請選擇答案:",
            options=list(question["options"].keys()),
            format_func=lambda x: f"{x}: {question['options'][x]}",
            key=f"{st.session_state.q_index}_radio"
        )
        user_answers = [choice]

    if st.button("提交答案") and not st.session_state.answered:
        # 檢查答案
        correct_answers = set(question["answer"])
        user_answers_set = set(user_answers)

        if correct_answers == user_answers_set:
            st.success("答對了！")
            st.session_state.score += 1
        else:
            st.error(f"答錯了！正確答案是：{', '.join(correct_answers)}")

        st.session_state.answered = True

    if st.button("下一題"):
        st.session_state.q_index += 1
        st.session_state.answered = False
        st.experimental_rerun()
        return  # 🔁 安全退出函式，避免 rerun 報錯


if __name__ == "__main__":
    main()



