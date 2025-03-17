import os
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'pluto_is_planet_and_cuba_is_free'
cnt = 0


@app.route('/galery', methods=['POST', 'GET'])
def answer():
    global cnt
    if request.method == 'GET':
        for el in os.walk(os.path.join(os.getcwd(), 'static\\img')):
            images = [i for i in el[-1]]
            break
        return render_template('1.html', data=images)
    if request.method == 'POST':
        f = request.files['file']
        f.save(f'static/img/image{cnt}.png')
        cnt += 1
        for el in os.walk(os.path.join(os.getcwd(), 'static\\img')):
            images = [i for i in el[-1]]
            break
        return render_template('1.html', data=images)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
