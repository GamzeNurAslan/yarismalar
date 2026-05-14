# Debug Arena - The Glitched Hero

## Proje Hakkında

**Debug Arena - The Glitched Hero**, Türkiye Yapay Zeka Topluluğu tarafından düzenlenen bir **debugging simülasyonu** kapsamında geliştirilmiş Python tabanlı metin savaş oyunudur.

Bu simülasyonda amaç, projede bulunan hataları tespit etmek, nedenlerini anlamak ve kod üzerinde gerekli düzeltmeleri yaparak oyunu çalışır hale getirmektir. Ben de çözüm sürecinde önce oyunun çalışmasını engelleyen temel hataları analiz ettim, ardından karakter, düşman, savaş, envanter ve seviye sistemlerindeki eksiklikleri düzenledim.

Proje sürecinde yalnızca hataları düzeltmekle kalmadım; oyunun daha eğlenceli ve geliştirilebilir olması için kritik vuruş, combo, ateş topu, dodge, berserk enemy, lucky chest ve unit test gibi ek özellikler de ekledim.

---

## Çözülen Hatalar 🛠️

### 1. Oyun Başlatma Hatası
`main.py` dosyasında oyun başlatma sistemi eksikti. `Game` sınıfı import edilerek `game.start()` çağrısı eklendi.

### 2. Eksik Import Hataları
`game/game.py` dosyasında `Character` sınıfı ve `CHAPTERS` verisi import edilmediği için oyun hata veriyordu. Gerekli importlar eklendi.

### 3. Enemy Constructor Hatası
`game/enemy.py` dosyasında düşman oluşturmak için gerekli parametreler eksikti. Constructor yapısı `name`, `hp`, `damage`, `xp_reward` ve `level` bilgilerini alacak şekilde düzenlendi.

### 4. Hasar Sisteminin Çalışmaması
`game/character.py` dosyasında oyuncu saldırısı sürekli 0 hasar veriyordu. Hasar formülü yeniden yazıldı ve rastgele hasar sistemi eklendi.

### 5. Savunma Sisteminin Çalışmaması
Savunma seçildiğinde karakter savunma moduna geçmiyordu. `is_defending` kontrolü eklenerek savunma sistemi aktif edildi.

### 6. HP Değerlerinin Negatife Düşmesi
Karakter ve düşman HP değerleri 0’ın altına düşebiliyordu. HP değerleri `max(0, hp)` mantığıyla sınırlandırıldı.

### 7. Düşman Ölüm Kontrolü
HP değeri 0 olan düşman hâlâ canlı kabul ediliyordu. `is_alive()` kontrolü `current_hp > 0` olacak şekilde düzeltildi.

### 8. Envanter Kullanımında Tur Kaybı
Oyuncu envanteri açtığında tur direkt bitiyordu. Envanter sonrası oyuncunun tekrar seçim yapabilmesi sağlandı.

### 9. Item Kullanım Hakkı
Item kullanıldığında kullanım hakkı azalmıyordu. Her kullanım sonrası `uses` değeri azaltıldı.

### 10. Stun Sistemi
Felç etkisi düşmanın saldırmasını engellemiyordu. `stunned` kontrolü eklendi ve felçli düşmanın saldırısı atlandı.

### 11. Kaçılan Düşmanın HP Durumu
Oyuncu düşmandan kaçınca, düşman tekrar karşılaşıldığında tam canla geliyordu. Düşmanın mevcut HP değeri korunacak şekilde düzenleme yapıldı.

### 12. Level Up Sistemi
Seviye atlama sistemi eksik çalışıyordu. XP sıfırlama, maksimum HP artırma ve tam iyileşme sistemi eklendi.

### 13. Envanter Slot Sistemi
`expand_slot()` fonksiyonu boştu. `self.max_slots += 1` eklenerek envanter kapasitesi artırılabilir hale getirildi.

---

## Eklenen Bonus Özellikler ✨

Oyundaki hataları başarıyla ayıkladıktan sonra projeye bazı ek özellikler de ekledim. Bu özellikler oyunun daha eğlenceli, dinamik ve geliştirilebilir hale gelmesini amaçlamaktadır.


### Bonus Özellik 1: Kritik Vuruş Sistemi

**Nasıl Çalışıyor:**  
Karakter saldırı yaptığında belirli bir ihtimalle kritik vuruş gerçekleştirir. Kritik vuruş gerçekleşirse normal saldırı hasarı iki katına çıkar. Bu özellik savaşlara şans faktörü ekleyerek oyunu daha heyecanlı hale getirir.

**Dosya ve Konum Bilgisi:**  
Mevcut Dosya: `game/character.py`  
Geçtiği Yer: `attack()` metodu


### Bonus Özellik 2: Combo Sistemi

**Nasıl Çalışıyor:**  
Oyuncu arka arkaya saldırı yaptığında combo sayacı artar. Combo sayısına göre oyuncu ek hasar kazanır. Böylece sürekli saldırı yapmayı tercih eden oyuncular için ödüllendirici bir savaş mekaniği oluşur.

**Dosya ve Konum Bilgisi:**  
Mevcut Dosya: `game/character.py`  
Geçtiği Yerler: `attack()`, `defend()` ve `fireball()` metotları  

Mevcut Dosya: `game/battle.py`  
Geçtiği Yer: Savaş başlangıcında combo sayacının sıfırlanması


### Bonus Özellik 3: Ateş Topu Yeteneği

**Nasıl Çalışıyor:**  
Oyuncuya özel bir yetenek olarak Ateş Topu saldırısı eklendi. Ateş Topu normal saldırıdan daha yüksek hasar verir. Ancak bu yetenek kullanıldıktan sonra cooldown süresine girer ve birkaç tur boyunca tekrar kullanılamaz.

**Dosya ve Konum Bilgisi:**  
Mevcut Dosya: `game/character.py`  
Geçtiği Yer: `fireball()` metodu  

Mevcut Dosya: `game/battle.py`  
Geçtiği Yerler: Oyuncu savaş menüsü ve Ateş Topu seçeneğinin işlendiği bölüm


### Bonus Özellik 4: Dodge Sistemi

**Nasıl Çalışıyor:**  
Karakter düşman saldırısı aldığında belirli bir ihtimalle saldırıdan tamamen kaçınabilir. Dodge gerçekleştiğinde oyuncu hiç hasar almaz. Bu sistem savaşlara savunma dışında ekstra bir hayatta kalma şansı ekler.

**Dosya ve Konum Bilgisi:**  
Mevcut Dosya: `game/character.py`  
Geçtiği Yer: `take_damage()` metodu


### Bonus Özellik 5: Berserk Enemy Sistemi

**Nasıl Çalışıyor:**  
Düşmanların canı kritik seviyeye düştüğünde saldırı güçleri artar. Düşmanın HP değeri belirli bir oranın altına indiğinde düşman vahşileşir ve daha fazla hasar verir. Bu özellik savaşların son bölümünü daha zorlu hale getirir.

**Dosya ve Konum Bilgisi:**  
Mevcut Dosya: `game/enemy.py`  
Geçtiği Yer: `attack()` metodu


### Bonus Özellik 6: Lucky Chest Sistemi

**Nasıl Çalışıyor:**  
Bölüm geçişlerinde oyuncunun karşısına rastgele bir sandık çıkabilir. Bu sandıktan şifa, saldırı güçlendirmesi veya tuzak çıkabilir. Böylece bölüm geçişlerine rastgele olay mekaniği eklenmiştir.

**Dosya ve Konum Bilgisi:**  
Mevcut Dosya: `game/game.py`  
Geçtiği Yerler: `start()` ve `lucky_chest()` metotları


### Bonus Özellik 7: Unit Test Sistemi

**Nasıl Çalışıyor:**  
Oyundaki temel mekaniklerin doğru çalıştığını kontrol etmek için `pytest` kullanılarak unit testler yazıldı. Bu testlerle karakter hasarı, HP sınırlandırması, eşya kullanımı, düşman durumu, envanter ve seviye sistemi gibi yapıların doğrulanması amaçlandı.

**Dosya ve Konum Bilgisi:**  
Yeni Dosya ise: `tests/` klasörü altında test dosyaları  
Kullanıldığı Yerler: Temel oyun mekaniklerini test etmek için `pytest` ile çalıştırılır

---

## Kullanılan Teknolojiler 💻

- Python
- Pytest
- Git
- GitHub
- Nesne Yönelimli Programlama

---

## Oyunu Çalıştırma ▶️

```bash
python main.py
