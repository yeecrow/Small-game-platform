from flask import Flask ,render_template,redirect,request,url_for
from flaskext.mysql import MySQL

appt = Flask(__name__,template_folder='template')


@appt.route('/')
def home():
    return  render_template('chosegame.html')
#@appt.route('/')
#def home():
#    return  render_template('index.html')

#@appt.route('/start', methods=['POST'])
#def start():
    # 执行一些逻辑，例如处理用户输入或数据验证等
    # 这里可以添加你需要的其他逻辑

    # 重定向到 chosegame 路由
#    return redirect('/chosegame')

#@appt.route('/chosegame', methods=['GET'])
#def chosegame():
    
#    return render_template('chosegame.html')
if __name__ == '__main__':
    appt.run(debug=True)
