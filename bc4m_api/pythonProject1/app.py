from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return {"msg": "BC4M"}
@app.route("/health")
def health_check():
    return {"STATUS": "OK"}
@app.route("/",methods=["POST"])
def echo():
    #bodyden gelen istek JSON ise
    if request.is_json:
        data = request.get_json()
        return jsonify(data)

    #bodyden gelen veri form ise (x-www-form-urlencoded veya form-data)
    elif request.form:
        #form verilerini Python sözlüğüne dönüştürme
        data = request.form.to_dict()
        #veriyi Json ile geri gönderme
        return jsonify(data)

    #bodyden gelen veri raw ise
    else:
        # bu veriyi utf 8 stringine dönüştürme
        data = request.data.decode('utf-8')
        #veriyi Json ile geri gönderme
        return jsonify({"raw_data": data})

if __name__ == "__main__":
    #uygulamaya dışardan erişilebilmesi adına verdiğim ip aralığı ve flask uygulamasının çalışacığı port
    app.run(debug=True,host="0.0.0.0", port=5000)