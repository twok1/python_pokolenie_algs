import os
import io
import sys
import json
import importlib.util
from dataclasses import dataclass, asdict
from contextlib import redirect_stdout
from tempfile import TemporaryDirectory
from zipfile import ZipFile
from pathlib import Path
import requests
import pytest


@dataclass
class Conf:
    url: str = ''
    script: str = ''


if os.path.isfile('check.conf'):
    with open('check.conf', 'r') as f:
        conf = Conf(**json.load(f))
else:
    conf = Conf()

# по-умолчанию используем значения от предыдущего запуска
url = input(f'\nURL [{conf.url}]: ').strip() or conf.url
script = input(f'Script [{conf.script}]: ').strip() or conf.script
with open('check.conf', 'w') as f:
    json.dump(asdict(Conf(url, script)), f)

# скачиваем файл тестов, если ещё не скачан
filename = Path(url).name
filepath = os.path.join('tests', filename)
if not os.path.exists(filepath):
    os.makedirs('tests', exist_ok=True)
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    with open(filepath, 'wb') as f:
        f.write(resp.content)

# ищем файл в текущей директории и её подпапках
script_location = next(Path.cwd().rglob(f'{script}.py'), None)
if not script_location:
    raise FileNotFoundError(f'{script}.py')

# загружаем скрипт решения, и не важно если файл назван, например, 1.2.3.py
spec = importlib.util.spec_from_file_location(
    name='solution',
    location=script_location,
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

test_fixtures = []
with TemporaryDirectory() as td:
    with ZipFile(filepath, 'r') as zf:
        files = zf.filelist
        for i in range(0, len(files), 2):
            with (
                zf.open(files[i]) as reply,
                zf.open(files[i + 1]) as clue,
            ):
                reply = reply.read().decode('u8')
                clue = clue.read().decode('u8')
                test_fixtures.append((reply, clue))


@pytest.mark.parametrize('test_input,expected', test_fixtures)
def test_exec(test_input, expected):
    with redirect_stdout(io.StringIO()):
        exec(test_input, module.__dict__)
        result = sys.stdout.getvalue().strip()
        assert result == expected
