import datastructures

def test_initialise_stack():
    stack = datastructures.Stack()

    assert stack is not None
    assert str(stack) == ''
 

def test_stack_methods():
    # Given: a stack (LIFO structure) instance
    stack = datastructures.Stack()

    # When: stack populated
    stack.push('Alpha')
    stack.push('Beta')
    stack.push('Gamma')
    stack.push('Delta')

    # Then: stack operations behave as expected
    assert str(stack) == "Delta->Gamma->Beta->Alpha"
    assert stack.isEmpty() == False
    assert stack.getSize() == 4
    assert stack.peek() == 'Delta'
    assert stack.getSize() == 4

    # And: When entries removed
    assert stack.pop() == 'Delta'
    assert stack.getSize() == 3
    assert str(stack) == "Gamma->Beta->Alpha"
    assert stack.pop() == 'Gamma'
    assert stack.getSize() == 2
    assert stack.pop() == 'Beta'
    assert stack.getSize() == 1

    # When: another item added
    stack.push("Omega")
    assert stack.getSize() == 2
    assert str(stack) == "Omega->Alpha"
    assert stack.pop() == 'Omega'
    
    # And: remaining items as expected
    assert str(stack) == "Alpha"
    assert stack.pop() == 'Alpha'
    assert stack.getSize() == 0
    assert str(stack) == ""
    assert stack.isEmpty() == True
