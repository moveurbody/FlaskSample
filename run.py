from flask import Flask, jsonify, render_template, request, make_response

app = Flask(__name__)


@app.route("/")
def hello_word():
    return "hello word"


@app.route("/temp_change", methods=["GET", "POST"])
def temp_change():
    if request.method == "GET":
        get_web = """
        <form method='post' actioin='temp_change'>
            攝氏溫度:<input type='text' value='0' name='celsius'><br>
            華氏溫度:<input type='text' value='0' name='fah'><br>
            <button type='submit'>送出</button>
        </form>
        """
        return get_web
    elif request.method == "POST":
        try:
            celsius = float(request.values['celsius'])
            fah = float(request.values['fah'])
            # 優先換算攝氏
            if celsius != 0 or (celsius == 0 and fah == 0):
                temp = celsius * (9 / 5) + 32
                return "攝氏 %s 度為華氏 %s度" % (celsius, temp)
            else:
                temp = (fah - 32) * (5 / 9)
                return "華氏 %s 度為攝氏 %s度" % (fah, temp)
        except Exception as e:
            print(e)
            return "please input numerical values!"


@app.route("/temp_change_beauty", methods=["GET", "POST"])
def temp_change_beauty():
    if request.method == "GET":
        return render_template('get_web.html')
    elif request.method == "POST":
        try:
            celsius = float(request.values['celsius'])
            fah = float(request.values['fah'])
            # 優先換算攝氏
            if celsius != 0 or (celsius == 0 and fah == 0):
                temp = celsius * (9 / 5) + 32
                fah = temp
                return render_template('post_web.html', celsius=celsius, fah=fah)
            else:
                temp = (fah - 32) * (5 / 9)
                celsius = temp
                return render_template('post_web.html', celsius=celsius, fah=fah)
        except Exception as e:
            print(e)
            return "please input numerical values!"


@app.route("/api/<temp>")
def api(temp):
    try:
        temp = float(temp)
        celsius = temp * (9 / 5) + 32
        fah = (temp - 32) * (5 / 9)
        response = {
            "statusCode": 200,
            "result": {
                "celsius": celsius,
                "fah": fah
            }
        }
        return make_response(jsonify(response), 200)
    except Exception as e:
        response = {
            "statusCode": 400,
            "result": str(e)
        }
        return make_response(jsonify(response), 400)


if __name__ == '__main__':
    app.run(debug=True)
