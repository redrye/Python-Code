stack = []
class error(Exception): pass

def push(x):
  global stack
  stack = [x] + stack
  
def pop():
  global stack
  if not stack:
    raise error('error underflow')
  top, *stack = stack
  return top
  
def top():
  if not stack
    raise error('error underflow')
  return stack[0]

def empty():
  return not stack

def member(x):
  return x in stack

def item(x):
  return stack[x]

def length:
  return len(stack)

def dump():
  print('<Stack:%s>' % stack)
