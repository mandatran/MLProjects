from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/netflix-rec', methods=['POST'])
def getValue():
    title = request.form['titleName']
    result = get_recommendations(title, cosine_sim)
    return render_template('home.html', ttl = title)

if __name__ == '__main__':
    app.run(debug=True)
