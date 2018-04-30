from flask import Flask, render_template, request, url_for, redirect
import urllib.request

app = Flask(__name__)

@app.route('/',methods = ['GET' , 'POST'])
def send():
	if request.method == 'POST' :
		url = request.form['url']
		return redirect("http://"+url , code=302)
		

	return render_template('index.html')


@app.route('/howitworks', methods=['GET', 'POST'])
def howitworks():
	return render_template('howitworks.html')


@app.route('/about', methods=['GET', 'POST'])
def about():
	return render_template('about.html')


if __name__ == '__main__':

	app.run(host = '192.168.0.114',port = 8000, debug= True)
	