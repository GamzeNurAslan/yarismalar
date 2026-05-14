import random

class Enemy:
    def __init__(self, name, hp, damage, xp_reward, level=1):
        self.name = name
        self.level = level
        self.max_hp = hp
        self.current_hp = hp
        self.damage = damage
        self.xp_reward = xp_reward
        self.stunned = False

    def attack(self):
        if self.stunned:
            print(f"  {self.name} felç! Bu tur saldıramadı.")
            self.stunned = False
            return 0

        damage = self.damage + random.randint(0, 3)

        if self.current_hp <= self.max_hp * 0.20:
            damage += 5
            print(f"  {self.name} vahşileşti! +5 hasar!")

        return damage

    def take_damage(self, damage):
        self.current_hp -= damage
        self.current_hp = max(0, self.current_hp)
        return damage

    def is_alive(self):
        return self.current_hp > 0

    def get_xp_reward(self):
        return self.xp_reward

    def show_stats(self):
        print(f"  [{self.name}] HP: {self.current_hp}/{self.max_hp} | Level: {self.level}")