基本上前端要改的就是網頁呈現出來的部分應該要盡量跟figma上設計的一樣 具體怎麼做可能要自己上網查一下或去問一下老師

連接資料庫我有找到的方法是:先pip install flask-mysql

然後改寫主程式加入這些東西:(這目前只有登入的部分 排行榜的可能要自己嘗試)
from flask import Flask, render_template, redirect, request
from flaskext.mysql import MySQL

app = Flask(__name__, static_folder='static', template_folder='template')

# MySQL配置
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = 'your_username'
app.config['MYSQL_DATABASE_PASSWORD'] = 'your_password'
app.config['MYSQL_DATABASE_DB'] = 'your_database_name'

# 初始化MySQL扩展
mysql = MySQL(app)

# 路由和视图函数
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    # 执行一些逻辑，例如处理用户输入或数据验证等
    # 这里可以添加你需要的其他逻辑

    # 获取表单数据
    username = request.form['username']
    password = request.form['password']

    # 连接到MySQL数据库
    conn = mysql.connect()
    cursor = conn.cursor()

    # 执行查询语句
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    result = cursor.fetchone()

    if result:
        # 登录成功，重定向到chosegame路由
        return redirect('/chosegame')
    else:
        # 登录失败，重定向到其他页面或返回错误信息
        return redirect('/login_failed')

@app.route('/chosegame')
def chosegame():
    return render_template('chosegame.html')

if __name__ == '__main__':
    app.run(debug=True)

另外昨天的那個比大小的程式碼整個我會丟進這個資料夾:「testgame」
我之後到周日才會有時間繼續弄讀取圖片跟嵌入其他遊戲你們弄得如何希望可以周日丟進群組
如果可以的話也能先上傳到github之後再更新就好