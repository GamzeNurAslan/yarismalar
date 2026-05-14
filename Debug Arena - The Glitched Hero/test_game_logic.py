from game.character import Character
from game.enemy import Enemy
from game.item import Item


def test_character_attack_damage_positive():
    hero = Character("Test")
    damage = hero.attack()
    assert damage >= hero.damage


def test_character_hp_never_negative():
    hero = Character("Test")
    hero.take_damage(999)
    assert hero.current_hp == 0


def test_defend_reduces_damage():
    hero = Character("Test")
    hero.defend()
    taken = hero.take_damage(20)
    assert taken == 10


def test_heal_item_does_not_exceed_max_hp():
    hero = Character("Test")
    hero.current_hp = 80
    potion = Item("Test İksir", "heal", 50, uses=1)
    potion.use(hero)
    assert hero.current_hp == hero.max_hp


def test_item_use_decreases_uses():
    hero = Character("Test")
    potion = Item("Test İksir", "heal", 20, uses=1)
    potion.use(hero)
    assert potion.uses == 0


def test_enemy_hp_never_negative():
    enemy = Enemy("Test Goblin", 30, 5, 10, 1)
    enemy.take_damage(999)
    assert enemy.current_hp == 0


def test_enemy_dead_when_hp_zero():
    enemy = Enemy("Test Goblin", 30, 5, 10, 1)
    enemy.take_damage(30)
    assert enemy.is_alive() is False


def test_stun_item_stuns_enemy():
    hero = Character("Test")
    enemy = Enemy("Test Goblin", 30, 5, 10, 1)
    stun_item = Item("Test Stun", "stun", 0, uses=1)
    stun_item.use(hero, enemy)
    assert enemy.stunned is True