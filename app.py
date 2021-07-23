from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        numero_decimal = int(request.form['numero_decimal'])
        numero_binario = bin(numero_decimal)
        return render_template("index.html", numero_decimal=numero_decimal, numero_binario=numero_binario)
       
    return render_template("index.html")

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(host='0.0.0.0',port=5000,debug=True)
