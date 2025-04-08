# Word文档格式化工具

这是一个基于Flask的Web应用，用于格式化Word文档。该工具可以自动处理Word文档中的格式，包括字体、行距、对齐方式等。

## 功能特点

- 支持.docx格式文件上传
- 自动格式化文档样式
- 美观的Web界面
- 支持文件大小限制（16MB）
- 自动下载处理后的文件

## 本地开发环境设置

1. 克隆仓库：
```bash
git clone [你的仓库URL]
cd [项目目录]
```

2. 创建并激活虚拟环境：
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows
```

3. 安装依赖：
```bash
pip install -r requirements.txt
```

4. 运行应用：
```bash
python app.py
```

5. 访问 http://localhost:5000

## LeanCloud部署

1. 安装LeanCloud命令行工具：
```bash
npm install -g lean-cli
```

2. 登录LeanCloud：
```bash
lean login
```

3. 初始化项目：
```bash
lean switch
```

4. 部署应用：
```bash
lean deploy
```

## 项目结构

```
.
├── app.py              # Flask应用主文件
├── format_questions.py # 文档格式化核心逻辑
├── requirements.txt    # 项目依赖
├── templates/          # HTML模板
│   └── index.html     # 主页面模板
└── uploads/           # 文件上传目录（自动创建）
```

## 使用说明

1. 打开网页界面
2. 点击"选择文件"按钮选择要处理的Word文档
3. 点击"上传并处理"按钮
4. 等待处理完成后自动下载格式化后的文件

## 注意事项

- 仅支持.docx格式文件
- 文件大小限制为16MB
- 处理后的文件会自动添加"formatted_"前缀

## 技术栈

- Python 3.x
- Flask
- python-docx
- HTML5/CSS3
- JavaScript

## 许可证

MIT License 