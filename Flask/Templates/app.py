from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
    @app.route('/predict', methods=['POST'])
    def predict():
        question = request.form['question']
        # Perform prediction or any other processing here
        tags = getTags(question)
        return jsonify(tags=tags)
        if __name__ == '__main__':
           app.run(debug=True)
        