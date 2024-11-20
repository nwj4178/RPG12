from character import Hero, Monster
from battle import Battle
from equipment import Equipment

def main():
    print("게임 시작")
    name = input("이름 입력: ")
    role = input("직업 입력(전사/마법사/궁수): ")
    hero = Hero(name, 100, 20, 5, 15, role)
    print(hero)

    # 몬스터 생성
    monster = Monster("고블린", 30, 10, 2, 10, 1)
    print(monster)

    # 전투
    battle = Battle()
    battle.fight(hero, monster)

    print(hero)

if __name__ == '__main__':
    main()
