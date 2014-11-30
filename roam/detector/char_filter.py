class CharFilter():
    def __init__(self, *args):
        super().__init__()
        self._tuple = args
        self.seq = 0

    def lower(self):
        return CharFilter(*tuple(map(lambda e: str(e).lower(), self._tuple)))

    def remove_dot(self):
        return self.remove_char('.')

    def remove_whitespace(self):
        return self.remove_char(' ')

    def remove_underbar(self):
        return self.remove_char('_')

    def remove_dash(self):
        return self.remove_char('-')

    def remove_special(self):
        return self.remove_char('~!@#$%^&*(),:;`<>/[]?{}=+"\'\\')

    def remove_basic(self):
        return self.remove_char('. _-')

    def remove_advanced(self):
        return self.remove_basic().remove_special()

    def remove_char(self, char):

        elements = []
        for e in self._tuple:
            for c in char:
                e = str(e).replace(c, '')
            elements.append(e)

        return CharFilter(*elements)

    def get(self, seq):
        self.seq = seq
        return self._tuple[seq]

    def get_tuple(self):
        return self._tuple

    def next(self):
        self.seq += 1
        try:
            return self._tuple[self.seq]
        except:
            self.seq -= 1
            raise

    def first(self):
        return self.get(0)
