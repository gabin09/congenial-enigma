from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # 클라이언트의 IP 주소 가져오기
    user_ip = request.remote_addr

    # 서버 로그에 IP 주소 출력
    app.logger.info("사용자의 IP 주소: %s", user_ip)

    return render_template('index.html', user_ip=user_ip)

if __name__ == '__main__':
    app.run(debug=True)
