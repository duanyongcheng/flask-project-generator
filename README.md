# Project Generator Python

A command-line tool to quickly generate Python projects with various templates and project structures.

## Installation

```bash
pip install project-generator-python
```

## Usage

```bash
create-project
```

Follow the interactive prompts to:
1. Enter project name
2. Choose template (basic/yn_tools/etc)
3. Configure project options

## Available Templates

- Basic Flask API project
- YN Tools project structure
- More templates coming soon

## Features

- Multiple project templates
- Docker support (optional)
- Common Python project patterns
- Ready-to-use CLI commands
- Customizable project structure

## Development

1. Clone the repository
2. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or `venv\Scripts\activate` on Windows
   ```
3. Install in development mode:
   ```bash
   pip install -e .
   ```

## License

MIT

## Author

Barry Duan
```

发布步骤：

1. 清理旧的构建文件：
```bash
rm -rf dist/ build/ *.egg-info/
```

2. 构建项目：
```bash
python -m build
```

3. 上传到 PyPI：
```bash
python -m twine upload dist/*
```

项目名称改为 project-generator-python 的优点：
1. 更好的描述性
2. 遵循 Python 包命名约定
3. 易于在 PyPI 上搜索
4. 能清晰表明这是一个 Python 相关的工具

用户可以通过以下方式安装和使用：
```bash
pip install project-generator-python
create-project