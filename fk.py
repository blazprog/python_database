import re

#foreignkey_pattern = r"""
#    \s+fk\s*
#    \(\s*(?P<table_name>\w+)\)
#    \s+ 
#    (?P<field_name>\w+)\)
#"""


foreignkey_pattern = r"""
    \s+fk\s*
    \(\s*(?P<table_name>\w+)
    -> 
    (?P<field_name>\w+)\)
"""
#foreignkey_pattern = r"""
#    \s+fk\s*
#    \(\s*(?P<table_name>\w+)
#    ->
#    (?P<field_name>\w+)\)
#"""
re_foreignkey_pattern = re.compile(foreignkey_pattern,re.VERBOSE)



str = "director_id integer not nul fk(directors->director_id)"

m = re_foreignkey_pattern.search(str)
if m:
    print("Nasek sem nekaj")
    print(m.group("table_name"))
    print(m.group("field_name"))


class Fibonacci:
    """Итератор последовательности Фибоначчи до N"""
      def __init__(self, N):
        self.n, self.a, self.b, self.max = 0, 0, 1, N
      def __iter__(self):
        # сами себе итератор: в классе есть метод next()
         return self
      def next(self):
         if self.n < self.max:
           a, self.n, self.a, self.b = self.a, self.n+1, self.b, self.a+self.b
           return a
         else:
           raise StopIteration
# Использование:
for i in Fibonacci(100):
  print i,   
