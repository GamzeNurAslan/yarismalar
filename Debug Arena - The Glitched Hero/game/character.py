import random

from .item import Item
from .inventory import Inventory
from .data import LEVEL_REWARDS

class Character:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.max_hp = 100
        self.current_hp = 100
        self.xp = 0
        self.xp_needed = 100
        self.damage = 10
        self.is_defending = False
        self.temp_damage_boost = 0
        self.temp_shield = 0
        self.inventory = Inventory(max_slots=3)
        self.inventory.add_item(Item("İksir", "heal", 30, uses=2))
        self.combo_count = 0
        self.fireball_cooldown = 0

    def attack(self):
        self.combo_count += 1

        combo_bonus = 0
        if self.combo_count == 2:
            combo_bonus = 2
            print("  COMBO x2! +2 hasar!")
        elif self.combo_count >= 3:
            combo_bonus = 4
            print("  COMBO x3! +4 hasar!")

        damage = self.damage + random.randint(0, 5) + self.temp_damage_boost + combo_bonus
        critical = random.random() < 0.10

        if critical:
            print("  KRİTİK VURUŞ!")
            damage *= 2

        self.temp_damage_boost = 0
        return damage

    def defend(self):
        self.combo_count = 0
        self.is_defending = True
        print(f"  {self.name} savunma pozisyonu aldı! Bu tur %50 az hasar alacak.")

    def take_damage(self, damage):
        if random.random() < 0.15:
            print(f"  {self.name} saldırıdan kaçındı!")
            return 0

        if self.temp_shield > 0:
            blocked = min(self.temp_shield, damage)
            damage -= blocked
            self.temp_shield = 0
            print(f"  Kalkan {blocked} hasarı bloke etti!")

        if self.is_defending:
            damage = damage // 2
            self.is_defending = False

        self.current_hp -= damage
        self.current_hp = max(0, self.current_hp)
        return damage

    def gain_xp(self, amount):
        self.xp += amount
        print(f"  {self.name} {amount} XP kazandı!")
        if self.level < 5 and self.xp >= self.xp_needed:
            self.level_up()

    def level_up(self):
        XP_THRESHOLDS = {2: 150, 3: 225, 4: 340, 5: 500}
        self.level += 1

        self.xp = 0
        self.max_hp += 20

        self.xp_needed = XP_THRESHOLDS.get(self.level, 500)
        self.current_hp = self.max_hp
        self.damage += 2

        print(f"\n  *** SEVİYE ATLADI! {self.name} artık Level {self.level}! ***")
        print(f"  Max HP: {self.max_hp} | Hasar: {self.damage}")

        self.inventory.expand_slot()
        reward = LEVEL_REWARDS.get(self.level)
        if reward:
            item = Item(reward["name"], reward["type"], reward["value"], uses=reward["uses"])
            added = self.inventory.add_item(item)
            if added:
                print(f"  Yeni item kazandın: {item.name}!")
            else:
                print(f"  Envanter doldu, {item.name} alınamadı.")

    def is_alive(self):
        return self.current_hp > 0

    def show_stats(self):
        print(f"  [{self.name}] HP: {self.current_hp}/{self.max_hp} | ")
        print(f"Level: {self.level} | XP: {self.xp}/{self.xp_needed}")

    def fireball(self):
        self.combo_count = 0
        if self.fireball_cooldown > 0:
            print(f"  Ateş Topu hazır değil! {self.fireball_cooldown} tur kaldı.")
            return 0

        self.fireball_cooldown = 3

        damage = 25 + random.randint(0, 10)

        print(f"  {self.name} ATEŞ TOPU kullandı!")
        return damage