from flask import Flask, render_template

app = Flask(__name__)


@app.route("/show/info")
def index():
    # return "chain"
    # Flask内部会自动打开这个文件,并且读取文件内容,将内容返回给用户
    # 默认去当前项目目录中的templates文件夹中找
    # 在文件里面写html文档
    return render_template("index.html")


if __name__ == '__main__':
    app.run()