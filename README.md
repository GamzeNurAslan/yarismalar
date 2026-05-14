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

### Kritik Vuruş Sistemi
Oyuncu saldırılarında belirli bir ihtimalle kritik vuruş yapabilir ve normal hasarın iki katını verir.

### Combo Sistemi
Oyuncu arka arkaya saldırı yaptığında combo oluşur ve ek hasar kazanır.

### Ateş Topu Yeteneği
Oyuncuya cooldown süresi olan özel bir ateş topu saldırısı eklendi.

### Dodge Sistemi
Karakter belirli bir ihtimalle düşman saldırılarından tamamen kaçınabilir.

### Berserk Enemy Sistemi
Düşmanların canı kritik seviyeye düştüğünde saldırı güçleri artar.

### Lucky Chest Sistemi
Bölüm geçişlerinde rastgele sandık etkinlikleri eklendi. Sandıklardan şifa, güçlendirme veya tuzak çıkabilir.

### Unit Test Sistemi
`pytest` ile temel oyun mekaniklerini test eden unit testler yazıldı.

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
