from flask import Flask, render_template, request
import os
from PIL import Image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    for file in request.files.getlist('file'):
        if file.filename.split('.')[-1].lower() in ('jpg', 'jpeg', 'png'):
            file_name = os.path.splitext(file.filename)[0]
            img = Image.open(file)
            img_converted = img.convert('RGB')
            img_converted.save(f'static/{file_name}.pdf')
    return 'Conversão concluída com sucesso!'

    
if __name__ == '__main__':
    app.run(debug=True)