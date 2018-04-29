from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def send():
	if request.method == 'POST':
		url = request.form['url']
	
		return redirect('http://' + url, code= 302)
	return render_template('index.html')

if __name__ == '__main__':

	app.run(host = '0.0.0.0',port = 5000, debug= True)
	