# Color constants
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
RESET = '\033[0m'


class Progression:
    def __init__(self, start=0,adv=1):
        self._current = start
        self._adv = adv

    def _advance(self):
        self._current+=self._adv
 
    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self

    def print_progression(self,n):
        for _ in range(n):
            val = next(self)
            color = GREEN if val%2==0 else YELLOW
            print(f'{RESET}{color}'.join(str(val)))