"""コマンドの入口。ここでモードを選んでから、対応するゲームを呼ぶ。"""

from .game import play
from .game_eitanngo import play_eitanngo
from .game_battle import play_battle
from .game_eitanngobattle import play_eitanngo_battle


def main():
    print("=== Hit & Blow ===")
    print("1: 1人プレイ")
    print("2: 対戦モード")

    while True:
        play_mode = input("プレイ人数を選んでください（1 or 2） > ").strip()
        if play_mode == "1":
            choose_solo_mode()
            break
        elif play_mode == "2":
            choose_dual_mode()
            break
        else:
            print("1か2を入力してね")


def choose_solo_mode():
    print("1: 数字当てモード")
    print("2: 英単語当てモード")

    while True:
        mode = input("モードを選んでください（1 or 2） > ").strip()
        if mode == "1":
            play()
            break
        elif mode == "2":
            play_eitanngo()
            break
        else:
            print("1か2を入力してね")


def choose_dual_mode():
    print("1: 数字当てモード")
    print("2: 英単語当てモード")

    while True:
        mode = input("モードを選んでください（1 or 2） > ").strip()
        if mode == "1":
            play_battle()
            break
        elif mode == "2":
            play_eitanngo_battle()
            break
        else:
            print("1か2を入力してね")
