# ÇÖZÜLEN HATALAR FORMU

## 1- Ana Oyun Başlatma Sistemi Eksikliği

Dosya Adı ve Satır Aralığı: main.py

Hatanın Sebebi: Oyun motorunu başlatan giriş noktası eksikti. Game sınıfı import edilmediği için oyun çalıştırılamıyordu.

Nasıl Çözdünüz: `from game.game import Game` importu eklendi ve Game nesnesi oluşturularak `game.start()` çağrıldı.

---

## 2- Character Sınıfının Import Edilmemesi

Dosya Adı ve Satır Aralığı: game/game.py

Hatanın Sebebi: Character sınıfı import edilmediği için `NameError: Character is not defined` hatası oluşuyordu.

Nasıl Çözdünüz: `from game.character import Character` importu eklendi.

---

## 3- CHAPTERS Verisinin Eksik Importu

Dosya Adı ve Satır Aralığı: game/game.py

Hatanın Sebebi: Bölüm verileri kullanılmasına rağmen `CHAPTERS` import edilmediği için sistem çalışmıyordu.

Nasıl Çözdünüz: `from game.data import CHAPTERS` importu eklendi.

---

## 4- Enemy Constructor Parametre Eksikliği

Dosya Adı ve Satır Aralığı: game/enemy.py

Hatanın Sebebi: Enemy sınıfı yalnızca `level` parametresi alıyordu. Ancak oyun sistemi düşman oluştururken name, hp, damage ve xp_reward parametrelerini gönderiyordu.

Nasıl Çözdünüz: Constructor parametreleri yeniden düzenlenerek tüm gerekli değerler eklendi.

---

## 5- Oyuncunun Sürekli 0 Hasar Vurması

Dosya Adı ve Satır Aralığı: game/character.py, attack fonksiyonu

Hatanın Sebebi: attack() fonksiyonu her zaman `0` döndürüyordu. Bu nedenle düşmanlar hiç hasar almıyordu.

Nasıl Çözdünüz: Hasar formülü README’de belirtilen kurala göre yeniden yazıldı:
Temel Hasar + Rastgele Değer (0-5) + Geçici Buff.

---

## 6- Savunma Mekaniğinin Aktifleşmemesi

Dosya Adı ve Satır Aralığı: game/character.py, defend fonksiyonu

Hatanın Sebebi: Savunma seçildiğinde `is_defending` bayrağı aktif edilmiyordu.

Nasıl Çözdünüz: `self.is_defending = True` eklenerek savunma sistemi çalışır hale getirildi.

---

## 7- HP Değerlerinin Negatif Olabilmesi

Dosya Adı ve Satır Aralığı: game/character.py ve game/enemy.py

Hatanın Sebebi: Karakter ve düşman can değerleri negatif değerlere düşebiliyordu.

Nasıl Çözdünüz: HP değerleri `max(0, hp)` mantığıyla sınırlandırıldı.

---

## 8- Düşmanların Ölmemesi

Dosya Adı ve Satır Aralığı: game/enemy.py, is_alive fonksiyonu

Hatanın Sebebi: HP değeri 0 olduğunda düşman hâlâ canlı kabul ediliyordu.

Nasıl Çözdünüz: Kontrol sistemi `current_hp > 0` olacak şekilde düzeltildi.

---

## 9- Inventory Kullanımında Tur Kaybı

Dosya Adı ve Satır Aralığı: game/battle.py, player_turn fonksiyonu

Hatanın Sebebi: Oyuncu envanter açtığında tur direkt sona eriyor ve düşman bedava saldırı yapıyordu.

Nasıl Çözdünüz: Envanter sonrası oyuncunun tekrar hamle seçebilmesi sağlandı.

---

## 10- Item Kullanım Haklarının Azalmaması

Dosya Adı ve Satır Aralığı: game/item.py

Hatanın Sebebi: Eşya kullanıldığında kullanım sayısı düşmüyordu ve itemler sonsuz kullanılabiliyordu.

Nasıl Çözdünüz: Her kullanım sonrası `self.uses -= 1` eklenerek kullanım hakkı azaltıldı.

---

## 11- Stun Etkisinin Çalışmaması

Dosya Adı ve Satır Aralığı: game/item.py ve game/enemy.py

Hatanın Sebebi: Felç etkisi düşmanı gerçekten durdurmuyordu ve stunned durumu sıfırlanmıyordu.

Nasıl Çözdünüz: Düşmanın stunned durumu aktif hale getirildi ve saldırı atlandıktan sonra normale dönmesi sağlandı.

---

## 12- Kaçılan Düşmanın HP’sinin Yenilenmesi

Dosya Adı ve Satır Aralığı: game/game.py

Hatanın Sebebi: Kaçılan düşman tekrar karşılaşıldığında HP’si tamamen doluyordu.

Nasıl Çözdünüz: Düşmanın mevcut HP değeri korunarak tekrar savaşa dahil edilmesi sağlandı.

---

## 13- Level Up Sisteminin Eksik Çalışması

Dosya Adı ve Satır Aralığı: game/character.py, level_up fonksiyonu

Hatanın Sebebi:

* XP sıfırlanmıyordu
* Max HP artmıyordu
* Karakter tam iyileşmiyordu

Nasıl Çözdünüz:

* XP sıfırlandı
* Max HP +20 artırıldı
* Current HP yeni maksimum değere eşitlendi

---

## 14- Boş Envanter Kontrolünün Hatalı Çalışması

Dosya Adı ve Satır Aralığı: game/inventory.py

Hatanın Sebebi: Kullanılabilir item kalmadığında sistem hâlâ envanter menüsünü açıyordu.

Nasıl Çözdünüz: `has_items()` kontrolü yeniden düzenlenerek yalnızca kullanılabilir item varsa menünün açılması sağlandı.

---

# EKLENEN BONUS ÖZELLİKLER

## Bonus Özellik 1: Combo Sistemi

Nasıl Çalışıyor:
Oyuncu arka arkaya saldırdığında combo sayacı artar.

* 2. saldırıda +2 hasar
* 3 ve üzeri saldırılarda +4 hasar bonusu uygulanır.

Savunma yapıldığında combo sıfırlanır.

Dosya ve Konum Bilgisi:
game/character.py → attack ve defend fonksiyonları

---

## Bonus Özellik 2: Dodge Sistemi

Nasıl Çalışıyor:
Oyuncu gelen saldırılardan belirli ihtimalle tamamen kaçınabilir ve 0 hasar alır.

Dosya ve Konum Bilgisi:
game/character.py → take_damage fonksiyonu

---

## Bonus Özellik 3: Berserk Enemy Sistemi

Nasıl Çalışıyor:
Düşmanın canı %30’un altına düştüğünde vahşileşir ve saldırıları +5 hasar kazanır.

Dosya ve Konum Bilgisi:
game/enemy.py → attack fonksiyonu

---

## Bonus Özellik 4: Lucky Chest Sistemi

Nasıl Çalışıyor:
Bölüm geçişlerinde rastgele sandık etkinliği oluşur.
Sandıktan:

* Şifa
* Güçlendirme
* Tuzak

çıkabilir.

Dosya ve Konum Bilgisi:
game/game.py → lucky_chest fonksiyonu

