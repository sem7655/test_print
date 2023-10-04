import subprocess

def test_print_hello_world():
    try:
        # Запускаем main.py и захватываем его вывод
        result = subprocess.run(['python', 'main.py'], capture_output=True, text=True)

        # Получаем вывод
        output = result.stdout.strip()

        # Проверяем, что вывод соответствует ожидаемому
        assert output == 'Hello_world'

    except Exception as e:
        # Если возникают ошибки, то тест не проходит
        raise AssertionError(f"Тест не прошел. Ошибка: {e}")

# Запускаем тест
test_print_hello_world()
