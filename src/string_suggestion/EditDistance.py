import numpy as np


class EditDistance:
    def __init__(self, insertion_cost: float = 1, deletion_cost: float = 1, substitution_cost: float = 2):
        self._i = insertion_cost
        self._d = deletion_cost
        self._s = substitution_cost
        self._array: np.array = np.array([])

    def _init_array(self, m: int, n: int) -> None:
        # init m + 1 by n + 1 array with a[i, 0] = i and a[0, j] = j
        M = m + 1
        N = n + 1
        self._array = np.zeros((M, N))
        self._array[0, :] = range(N)
        self._array[:, 0] = range(M)

    def compare(self, s: str, t: str) -> float:
        m, n = len(s), len(t)
        self._init_array(m, n)

        for _i in range(m):
            i = _i + 1
            for _j in range(n):
                j = _j + 1
                # compute distance table
                need_substitute = 1 if s[_i] != t[_j] else 0
                self._array[i, j] = min(
                    self._array[i - 1, j] + self._d,
                    self._array[i, j - 1] + self._i,
                    self._array[i - 1, j - 1] + need_substitute * self._s
                )

        return self._array[m, n]

    @property
    def edit_distance_table(self) -> np.array:
        return self._array.copy()
