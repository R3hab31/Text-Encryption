from flask import Flask, render_template, request
from Encrypt import (rsa_encrypt,aes_encrypt,des_encrypt,hybrid_encrypt)
app =Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/rsa", methods=["GET","POST"])
def rsa():
    output=""
    if request.method=="POST":
        msg=request.form["message"]
        output=rsa_encrypt(msg)
    return render_template("rsa.html",output=output)

@app.route("/des", methods=["GET","POST"])
def des():
    output=""
    if request.method=="POST":
        msg=request.form["message"]
        output=rsa_encrypt(msg)
    return render_template("des.html",output=output)

@app.route("/aes", methods=["GET","POST"])
def aes():
    output=""
    if request.method=="POST":
        msg=request.form["message"]
        output=rsa_encrypt(msg)
    return render_template("aes.html",output=output)

@app.route("/hybrid", methods=["GET","POST"]) 
def hybrid():
    data=""
    key=""
    if request.method=="POST":
        msg=(request.form["message"])
        algo=(request.form.get("algo"))
        if not algo:
             return render_template("hybrid.html",output="",enc_key="",error="Select an option")
        data,key=(hybrid_encrypt(msg,algo))
    return render_template("hybrid.html",output=data,enc_key=key)
    

if __name__ == "__main__":
    app.run(debug=True)
