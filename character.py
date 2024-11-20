from equipment import Equipment

class Character:
    def __init__(self, name, hp, base_attack, base_defense, speed):
        self.name = name
        self.hp = hp
        self.base_attack = base_attack
        self.base_defense = base_defense
        self.speed = speed
        self.weapon = None
        self.armor = None

    def take_damage(self, damage):
        actual_damage = max(0, damage - self.calculate_defense())
        self.hp = max(0, self.hp - actual_damage)
        return actual_damage

    def is_alive(self):
        return self.hp > 0

    def equip(self, equipment):
        if equipment.type == "무기":
            self.weapon = equipment
        elif equipment.type == "방어구":
            self.armor = equipment

    def calculate_attack(self):
        return self.base_attack + (self.weapon.power if self.weapon else 0)

    def calculate_defense(self):
        return self.base_defense + (self.armor.power if self.armor else 0)

    def __str__(self):
        return (f"{self.name} - HP: {self.hp}, 공격력: {self.base_attack}, "
                f"방어력: {self.base_defense}, 속도: {self.speed}, "
                f"무기: {self.weapon.name if self.weapon else '없음'}, "
                f"방어구: {self.armor.name if self.armor else '없음'}")


class Hero(Character):
    def __init__(self, name, hp, base_attack, base_defense, speed, role):
        super().__init__(name, hp, base_attack, base_defense, speed)
        self.role = role
        self.exp = 0
        self.level = 1

    def gain_exp(self, amount):
        self.exp += amount
        if self.exp >= self.level * 10:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.exp = 0
        self.hp += 20
        self.base_attack += 5
        self.base_defense += 3
        self.speed += 2
        print(f"{self.name}가 레벨업 했습니다! (Lv: {self.level})")

    def __str__(self):
        return (f"{self.name}[{self.role}] - HP: {self.hp}, 공격력: {self.calculate_attack()}, "
                f"방어력: {self.calculate_defense()}, 속도: {self.speed}, 레벨: {self.level}, "
                f"무기: {self.weapon.name if self.weapon else '없음'}, "
                f"방어구: {self.armor.name if self.armor else '없음'}, 경험치: {self.exp}")


class Monster(Character):
    def __init__(self, name, hp, base_attack, base_defense, speed, level):
        super().__init__(name, hp, base_attack, base_defense, speed)
        self.level = level

    def drop_item(self):
        import random
        if random.randint(1, 100) <= 50:  # 50% 확률로 아이템 드롭
            item_type = "무기" if random.randint(1, 2) == 1 else "방어구"
            rarity_roll = random.randint(1, 100)
            if rarity_roll <= 50:
                rarity = "일반"
            elif rarity_roll <= 80:
                rarity = "레어"
            else:
                rarity = "전설"
            power = random.randint(5, 10) + (5 if rarity == "레어" else 10 if rarity == "전설" else 0)
            return Equipment(f"{rarity} {item_type}", item_type, power)
        return None

    def __str__(self):
        return (f"{self.name}[Lv: {self.level}] - HP: {self.hp}, "
                f"공격력: {self.calculate_attack()}, 방어력: {self.calculate_defense()}, 속도: {self.speed}, "
                f"무기: {self.weapon.name if self.weapon else '없음'}, "
                f"방어구: {self.armor.name if self.armor else '없음'}")
