import sqlite3

db_name = "victorina.qlite"
conn = None 
cursor = None

def open():
    global conn,cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor


def close():
    cursor.close()
    conn.close()


def do(query,params = None):
    if params is None:
        cursor.execute(query)
    else:
        cursor.execute(query.params)
    conn.commit()

def clear_db():
    open()
    do("DROP TABLE IF EXISTS quiz")
    do("DROP TABLE IF EXISTS quiz_content")
    do("DROP TABLE IF EXISTS question")
    close()


def create():
    open()
    cursor.execute("PRAGMA foreign_keys = ON")
    do('''CREATE TABLE iF NOT EXISTS  quiz(
       id INTEGER PRIMARY KEY, 
       name VARHAR)''')
    
    do('''CREATE TABLE IF NOT EXISTS question (
            id INTEGER PRIMARY KEY,
            question VARCHAR,
            answer VARCHAR,
            wrong1 VARCHAR,
            wrong2 VARCHAR,
            wrong3 VARCHAR)''')

    do('''CREATE TABLE IF NOT EXISTS quiz_content (
            id INTEGER PRIMARY KEY,
            quiz_id INTEGER,
            question_id INTEGER,
            FOREIGN KEY (quiz_id) REFERENCES quiz (id),
            FOREIGN KEY (question_id) REFERENCES question (id))''')


def add_questions():
    questions = [
        ('Скільки місяців на рік мають 28 днів?', 'Всі', 'Один', 'Жодного', 'Два'),
        ('Яким стане зелена скеля, якщо впаде в Червоне море?', 'Мокрим', 'Червоним', 'Не зміниться', 'Фіолетовим'),
        ('Якою рукою краще розмішувати чай?', 'Ложкою', 'Правою', 'Лівою', 'Любою'),
        ('Що не має довжини, глибини, ширини, висоти, а можна виміряти?', 'Час', 'Дурість', 'Море', 'Повітря'),
        ('Коли сіткою можна витягнути воду?', 'Коли вода замерзла', 'Коли немає риби', 'Коли спливла золота рибка', 'Коли сітка порвалася'),
        ('Що більше слона і нічого не важить?', 'Тінь слона', 'Повітряна куля', 'Парашут', 'Хмара')
    ]
    open()
    cursor.executemany('''INSERT INTO question (question, answer, wrong1
                       wrong2, wrong3) VALUES (?,?,?,?,?)''', questions) 
    conn.commit()
    close()


def add_quiz():
    quizzez = [
        ("Своя гра"),
        ("Хто хоче стати мільйонером?"),
        ("Найрозумніший"),
    ]
    open()
    cursor.executemany('''INSERT INTO quiz(name) VALUES (?)''', quizzez)
    conn.commit()
    close()
    
def show(table):
    query = "SELECT  * FROM" + table
    open()
    cursor.execute(query)
    print(cursor.fetchall())
    close() 


def show_table():
    show("question")
    show("quiz")
    show("quiz_content")

