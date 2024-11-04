from typing import Dict

TEMPLATES: Dict[str, Dict[str, str]] = {
    'basic': {
        'app/__init__.py': '''
from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
    return app
''',
        'app/routes/__init__.py': '',
        'app/routes/chat_routes.py': '''
from flask import Blueprint, request, jsonify

bp = Blueprint('chat', __name__)

@bp.route('/chat', methods=['POST'])
def chat():
    return jsonify({'message': 'Hello from chat route!'})
''',
        # ... rest of the template files
        'app/services/__init__.py': '',
        'app/services/openai_service.py': '''
class OpenAIService:
    def __init__(self):
        pass
    
    def chat(self):
        pass
''',
        'app/services/anthropic_service.py': '''
class AnthropicService:
    def __init__(self):
        pass
    
    def chat(self):
        pass
''',
        'app/models/__init__.py': '',
        'app/utils/__init__.py': '',
        'app/utils/error_handlers.py': '''
from flask import jsonify

def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Not found'}), 404
''',
        'config/__init__.py': '',
        'config/development.py': '''
class DevelopmentConfig:
    DEBUG = True
    SECRET_KEY = 'dev'
''',
        'config/production.py': '''
class ProductionConfig:
    DEBUG = False
    SECRET_KEY = 'production-key'
''',
        'config/testing.py': '''
class TestingConfig:
    TESTING = True
    DEBUG = True
''',
        'tests/__init__.py': '',
        'tests/test_routes.py': '''
def test_chat_route(client):
    response = client.post('/chat')
    assert response.status_code == 200
''',
        'tests/test_services.py': '''
def test_openai_service():
    pass

def test_anthropic_service():
    pass
''',
        'requirements.txt': '''
flask
flask-cors
python-dotenv
''',
        'run.py': '''
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
''',
        '.env': '''
OPENAI_API_KEY=your-api-key-here
ANTHROPIC_API_KEY=your-api-key-here
''',
        '.gitignore': '''
__pycache__/
*.pyc
.env
venv/
.pytest_cache/
''',
        'README.md': '''
# Flask API Project

## Setup
1. Create virtual environment: `python -m venv venv`
2. Activate virtual environment: `source venv/bin/activate` (Linux/Mac) or `venv\\Scripts\\activate` (Windows)
3. Install dependencies: `pip install -r requirements.txt`
4. Copy `.env.example` to `.env` and fill in your API keys
5. Run the application: `python run.py`
'''
    },
    'full': {},  # Add full template configuration here
    'yn_tools': {
        'input/__init__.py': '',
        'output/__init__.py': '',
        'template/__init__.py': '',
        '如何安装.txt': '''
1. 确保已安装Python 3.8或以上版本
2. 创建虚拟环境: python -m venv venv
3. 激活虚拟环境: 
   - Windows: venv\\Scripts\\activate
   - Linux/Mac: source venv/bin/activate
4. 安装依赖: pip install -r requirements.txt
''',
        '如何运行.txt': '''
方式一:
1. 双击运行小工具.bat文件

方式二:
1. 打开命令行
2. 进入项目目录
3. 执行: python 运营部小工具.py
''',
        'requirements.txt': '''
''',
        '.env': '''
# 环境变量配置
''',
        '运行小工具.bat': '''
''',
        '运营部小工具.py': '''
''',
        'README.md': '''
# 运营部小工具

简单易用的数据处理工具集

## 目录结构

- input/: 输入文件目录
- output/: 输出文件目录
- template/: 模板文件目录
- docs/: 使用说明文档
- run.bat: Windows快捷启动脚本
- run.py: 主程序

## 使用说明

1. 将需要处理的文件放在input目录下
2. 双击run.bat运行程序
3. 处理后的文件将保存在output目录下

## 开发说明

1. 主要逻辑在run.py中
2. 使用click处理命令行
3. 遵循目录约定:
   - input/: 仅存放输入文件
   - output/: 仅存放输出文件
   - template/: 仅存放模板文件
'''
    }
}
