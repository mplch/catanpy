class Matrix:
    n: int
    m: int
    nm : tuple[int, int]
    table: list[list[any]]
    # Python any type?
    # Can I show table directly from Matrix without Matrix.table ??

    def __init__(self, n: int =2, m: int =2, fill: any =' '):
        # Two types of parameters? n, m VS table?
        self.n = n
        self.m = m
        self.nm = (n, m)
        self.init_with(fill)

    def __str__(self):
        string = ""
        for row in self.table:
            string += str(row)
            string += '\n'
        return string

    def init_with(self, fill):
        row = []
        for r in range(self.n):
            row.append(fill)
        for c in range(self.m):
            self.table.append(row.copy())  # ?!

    def t(self):
        n_new = self.m
        m_new = self.n
        new_matrix = []
        for i in range(n_new):
            new_row = []
            for j in range(m_new):
                new_row.append(self.table[j][i])
            new_matrix.append(new_row)
        self.n = n_new
        self.m = m_new
        self.nm = (n_new, m_new)
        self.table = new_matrix

    def from_table(self, table: list[list[any]]):
        self.n = len(table)
        self.m = len(table[0])
        self.table = table.copy()
