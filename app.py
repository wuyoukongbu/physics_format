from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import os
from format_questions import format_questions

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# 确保上传文件夹存在
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return '没有文件被上传', 400
    
    file = request.files['file']
    if file.filename == '':
        return '没有选择文件', 400
    
    if not file.filename.endswith('.docx'):
        return '请上传.docx格式的文件', 400
    
    # 保存上传的文件
    input_filename = secure_filename(file.filename)
    input_path = os.path.join(app.config['UPLOAD_FOLDER'], input_filename)
    file.save(input_path)
    
    # 生成输出文件名
    output_filename = 'formatted_' + input_filename
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
    
    try:
        # 处理文件
        format_questions(input_path, output_path)
        
        # 返回处理后的文件
        return send_file(output_path, as_attachment=True, download_name=output_filename)
    except Exception as e:
        return f'处理文件时出错: {str(e)}', 500
    finally:
        # 清理临时文件
        if os.path.exists(input_path):
            os.remove(input_path)
        if os.path.exists(output_path):
            os.remove(output_path)

if __name__ == '__main__':
    app.run(debug=True) 