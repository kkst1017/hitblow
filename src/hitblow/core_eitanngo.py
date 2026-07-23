"""英単語版 Hit & Blow の中心ロジック"""

import random

# 出題する単語（すべて3文字）
WORDS = [
    "cat",
    "dog",
    "sun",
    "map",
    "pen",
    "hat",
    "box",
    "cup",
    "car",
    "bus",
]


def judge_eitanngo(secret, guess):
    """secret と guess を比べて (hit, blow) を返す。"""
    hits = sum(s == g for s, g in zip(secret, guess))
    common = sum(min(secret.count(c), guess.count(c)) for c in set(guess))
    return hits, common - hits


def make_secret_eitanngo():
    """ランダムに英単語を1つ選ぶ。"""
    return random.choice(WORDS)

def make_hint(secret):
    """ランダムな1文字について周辺の文字をヒントとして返す。"""

    mode = random.choice(["around", "before", "after"])
    index = random.randint(0, 2)
    ch = secret[index]
    code = ord(ch)

    if mode == "around":
        # 前後1文字
        before = "z" if code == ord('a') else chr(code - 1)
        after = "a" if code == ord('z') else chr(code + 1)
        return f"ヒント: {index+1}文字目は「{before}」から「{after}」です"

    elif mode == "before":
        # 前2文字
        before2 = chr(code - 2) if code - 2 >= ord('a') else chr(ord('z') - (ord('a') - (code - 2) - 1))
        before1 = "z" if code == ord('a') else chr(code - 1)
        return f"ヒント: {index+1}文字目は「{before2}」から「{ch}」です"

    else:
        # 後2文字
        after1 = "a" if code == ord('z') else chr(code + 1)
        after2 = chr(code + 2) if code + 2 <= ord('z') else chr(ord('a') + (code + 2 - ord('z') - 1))
        return f"ヒント: {index+1}文字目は「{ch}」から「{after2}」です"