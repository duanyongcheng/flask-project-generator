import os
import click
import questionary
from pathlib import Path
from python_generator.templates import TEMPLATES  # 修改导入路径
from typing import Union, Optional

def write_file(path: Union[str, Path], content: Optional[str] = '') -> None:
    """Write content to file, creating parent directories if needed"""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(str(content).lstrip(), encoding='utf-8')

@click.command()
@click.option('--path', default='.', help='Path where the project will be created')
def create_project(path: str) -> None:
    """Create a new Flask project with AI API integration."""
    project_name = questionary.text("Enter project name:", default="flask_project").ask()

    template = questionary.select(
        "Choose a template:",
        choices=list(TEMPLATES.keys()),
        default="basic"
    ).ask()

    with_docker = questionary.confirm("Include Docker files?", default=False).ask()

    base_dir = Path(path) / project_name

    # Create files from template
    for file_path, content in TEMPLATES[template].items():
        full_path = base_dir / file_path
        write_file(full_path, content)

    if with_docker:
        dockerfile_content = '''
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "run.py"]
'''
        write_file(base_dir / 'Dockerfile', dockerfile_content)

        docker_compose_content = '''
version: '3'
services:
  web:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - .:/app
    environment:
      - FLASK_ENV=development
'''
        write_file(base_dir / 'docker-compose.yml', docker_compose_content)

    click.echo(f"✨ Project '{project_name}' created successfully at {base_dir}")

def main():
    create_project()

if __name__ == '__main__':
    main()
