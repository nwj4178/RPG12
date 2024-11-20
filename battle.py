class Battle:
    def fight(self, hero, monster):
        print(f"전투 시작 {hero.name} vs {monster.name}")
        turn = 1

        while hero.is_alive() and monster.is_alive():
            print(f"== 턴 {turn} ==")
            print(hero)
            print(monster)

            if hero.speed >= monster.speed:
                self.hero_turn(hero, monster)
                if not monster.is_alive():
                    break
                self.monster_turn(hero, monster)
            else:
                self.monster_turn(hero, monster)
                if not hero.is_alive():
                    break
                self.hero_turn(hero, monster)

            turn += 1

        if not monster.is_alive():
            print(f"{monster.name}가 쓰러졌습니다.")
            hero.gain_exp(monster.level * 5)
            dropped_item = monster.drop_item()
            if dropped_item:
                print(f"{monster.name}가 {dropped_item.name}을(를) 드롭했습니다.")
                hero.equip(dropped_item)
                print(f"{hero.name}가 {dropped_item.name}을(를) 착용했습니다.")
        elif not hero.is_alive():
            print(f"{hero.name}가 쓰러졌습니다.")

    def hero_turn(self, hero, monster):
        damage = monster.take_damage(hero.calculate_attack())
        print(f"{hero.name}가 {monster.name}에게 {damage}의 데미지를 입힘")

    def monster_turn(self, hero, monster):
        damage = hero.take_damage(monster.calculate_attack())
        print(f"{monster.name}가 {hero.name}에게 {damage}의 데미지를 입힘")
