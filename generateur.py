import argparse
from pyexcel_ods3 import get_data
import random
import time


# Note: rouler avec l'option -u (unbuffered) pour être certain que
# les outpus sont flushés immédiatement:
#
# $ python -u generateur.py

if __name__ == '__main__':

    parser = argparse.ArgumentParser('Generateur de cosmogonie')
    parser.add_argument(
        '-n', default=-1, type=int,
        help='nombre de paragraphes (-1 pour infini)'
    )
    parser.add_argument(
        '-p', nargs=2, default=(2, 5), type=int,
        help='longueur des paragraphes'
    )
    parser.add_argument(
        '-d', nargs=2, default=(1, 3), type=int,
        help='delai entre les paragraphes'
    )
    args = parser.parse_args()

    data = get_data("GR_AN_V1.ods")['Feuille1']

    n = 0
    while True:
        n_para_cells = random.randint(args.p[0], args.p[1])
        para = []
        while len(para) < n_para_cells:
            row = random.randint(1, len(data) - 1)
            col = random.randint(0, len(data[row]) - 1)
            cell = data[row][col].strip()
            if not cell:
                continue
            para.append(cell)
        print(', '.join('"%s"' % cell for cell in para))
        n += 1
        if args.n > 0 and n >= args.n:
            break
        time.sleep(random.randint(args.d[0], args.d[1]))
