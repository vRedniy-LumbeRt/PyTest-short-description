# Пример запуска тестов

Помимо удобства использования особенностей библиотеки PyTest, описанной в PyTest.md, данная библиотека также предоставляет удобный функционал для отладки и тестирования.

Для начала, опишем возможные варианты запуска тестов.

Базовые варианты запуска тестов:

* Запуск одного файла: ```pytest test_mod.py```
* Запуск всех тестов в директории: ```pytest testing/```
* Запуск конкретного теста: ```pytest test_mod.py::test_func```

### Запуск одного теста

Для запуска одного теста создадим файл ```try_pytest_features.py```, в котором будут находиться некоторые тесты из файла ```PyTest.md``` (работаем в папке ```Pytest_overview```).


Файл ```try_pytest_features.py```
```python
import pytest


# Пример с использованием параметризации
@pytest.mark.parametrize("input_val, expected", [
    ("hello", 5),
    ("world", 5),
    ("pytest", 6)
])
def test_length(input_val: str, expected: int):
    assert len(input_val) == expected


# Пример тестов с использованием фикстур
@pytest.fixture
def numbers() -> list:
    return [1, 2, 3]


def test_length_2(numbers: list):
    assert len(numbers) == 3


def test_sum(numbers: list):
    assert sum(numbers) == 6

```

Далее из терминала запустим команду 
```
pytest try_pytest_features.py
```

Результатом работы программы будет:
```
(venv) PS C:\Users\stepa\PycharmProjects\train_pr> pytest try_pytest_features.py            
========================================================================================================= test session starts =========================================================================================================
platform win32 -- Python 3.10.2, pytest-8.3.4, pluggy-1.5.0
rootdir: C:\Users\stepa\PycharmProjects\train_pr
collected 5 items                                                                                                                                                                                                                       

try_pytest_features.py .....                                                                                                                                                                                                     [100%]

========================================================================================================== 5 passed in 0.01s ========================================================================================================== 
(venv) PS C:\Users\stepa\PycharmProjects\train_pr> 
```

Тесты успешно выполнились.

### Запуск конкретного теста

Для запуска конкретного теста необходимо через два двоеточия указать, какой именно тест необходимо выполнить.
```
pytest try_pytest_features.py::test_sum
```

Получим следующий вывод:
```
(venv) PS C:\Users\stepa\PycharmProjects\train_pr> pytest try_pytest_features.py::test_sum  
========================================================================================================= test session starts =========================================================================================================
platform win32 -- Python 3.10.2, pytest-8.3.4, pluggy-1.5.0
rootdir: C:\Users\stepa\PycharmProjects\train_pr
collected 1 item                                                                                                                                                                                                                        

try_pytest_features.py .                                                                                                                                                                                                         [100%] 

========================================================================================================== 1 passed in 0.01s ========================================================================================================== 
(venv) PS C:\Users\stepa\PycharmProjects\train_pr> 
```

Как и было необходимо, выполнился только нужный нам тест.

### Запуск всех тестов в дирректории

Для демонстрации данного примера создадим папку ```tests_dir```, в которой создадим два файла с тестами.

Файл ```tests_dir/test_n1.py```
```python
import pytest


def add(a: int, b: int) -> int:
    return a + b


def test_1():
    assert add(1, 1) == 2
```

Файл ```tests_dir/test_n2.py```
```python
import pytest


def mult(a: int, b: int) -> int:
    return a * b


def test_1():
    assert mult(2, 3) == 6

```

Запустим проверку тестов в каждом файле директории:
```
pytest tests_dir/
```

Изучим вывод:
```
(venv) PS C:\Users\stepa\PycharmProjects\train_pr> pytest tests_dir/                        
========================================================================================================= test session starts =========================================================================================================
platform win32 -- Python 3.10.2, pytest-8.3.4, pluggy-1.5.0
rootdir: C:\Users\stepa\PycharmProjects\train_pr
collected 2 items                                                                                                                                                                                                                       

tests_dir\test_n1.py .                                                                                                                                                                                                           [ 50%] 
tests_dir\test_n2.py .                                                                                                                                                                                                           [100%] 

========================================================================================================== 2 passed in 0.01s ========================================================================================================== 
(venv) PS C:\Users\stepa\PycharmProjects\train_pr> 

```

Тесты в обоих файлах директории были успешно запущены и выполнены.

## Итог

PyTest предоставляет простой и гибкий способ запуска тестов через командную строку, позволяя выбирать между запуском отдельных файлов (```pytest test_mod.py```), директорий (```pytest testing/```) и конкретных тестов (```pytest test_mod.py::test_func```), что делает процесс тестирования удобным и эффективным.