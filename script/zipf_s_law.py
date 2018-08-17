# coding: utf-8

import jieba
from collections import Counter
import matplotlib.pyplot as plt
import math


def zipf_s_law(path):
    words = []
    with open(path, 'r', encoding='utf-8') as fd:
        [words.extend(jieba.cut(line.strip())) for line in fd if len(line.strip()) > 0]
    counts = words_count(words)
    x = [math.log(i) for i in range(1, len(counts) + 1)]
    y = [math.log(l[1]) for l in counts]
    print(words)
    plt.plot(x, y)
    plt.show()


def words_count(words, topn=0):
    topn = len(words) if topn == 0 else topn
    order_counts = Counter(words).most_common(topn)
    return order_counts


if __name__ == '__main__':
    zipf_s_law("D:\\workspace\\projects\\study\\zipf_test.txt")
