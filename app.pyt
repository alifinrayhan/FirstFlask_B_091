from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == 'POST':
        # Mengambil data dari form
        name = request.form.get('name')
        age = request.form.get('age')
        
        # Membuat hasil
        result = f"Halo {name}, umur anda {age} tahun!"
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)