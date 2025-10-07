print(1+1+2)
print("hello world")
PermissionError
print("hello world")
# Test code to verify functionality
def test_basic_operations():
    assert 1 + 1 + 2 == 4
    
def test_print_output(capsys):
    print("hello world")
    captured = capsys.readouterr()
    assert captured.out == "hello world\n"

def test_permission_error():
    try:
        raise PermissionError
    except PermissionError:
        assert True