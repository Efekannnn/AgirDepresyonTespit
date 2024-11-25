# AgirDepresyonTespit

# Proje Açıklaması
Bu proje, çevrimiçi platformlardan toplanan metin içerikleri kullanarak intihara meyilli bireylerin metinlerini analiz etmek ve sınıflandırmak amacıyla geliştirilmiştir. Reddit gibi platformlardan toplanan veriler, doğal dil işleme (NLP) yöntemleriyle temizlenmiş, işlenmiş ve etiketlenmiştir. Proje sonunda, intihara meyilli ve meyilli olmayan bireylerin metinlerini analiz edebilecek bir veri seti oluşturulmuştur.

# İçindekiler
Veri Toplama
Veri Temizleme ve Çeviri
Veri Etiketleme
Birleştirme ve Temizleme
Özellik Mühendisliği
Sonuçlar ve Gelecek Çalışmalar
# 1. Veri Toplama
Kaynaklar: Reddit API kullanılarak belirli subredditlerden metinler çekildi. Örneğin:
İntihara Meyilli İçerikler: r/SuicideWatch, r/depression, r/depression_help.
Günlük Konuşmalar: r/CasualConversation, r/AskReddit.
Toplam Veri: 10,364 gönderi (İntihara meyilli: 5,500, İntihara meyilli olmayan: 4,864).
Veri toplama işlemi httpx kütüphanesi ile gerçekleştirilmiştir.
# 2. Veri Temizleme ve Çeviri
Temizleme Adımları:
Küçük harfe çevirme.
Gereksiz karakterlerin silinmesi (semboller, sayılar vb.).
Boş ve tekrarlanan kayıtların kaldırılması.
Çeviri:
İngilizce gönderiler, deep_translator kütüphanesiyle Türkçeye çevrilmiştir.
Metinler, API limitine uygun şekilde parçalara ayrılarak çevrilmiştir.
# 3. Veri Etiketleme
İntihara meyilli gönderiler "1", meyilli olmayanlar "0" olarak etiketlendi.
Python'da etiketleme işlemi gerçekleştirilmiş ve veriye yeni bir sütun olarak eklenmiştir.
# 4. Birleştirme ve Temizleme
Farklı CSV dosyalarındaki veriler birleştirilmiştir.
Temizleme:
Tüm boş kayıtlar ve tekrarlanan veriler çıkarıldı.
# 5. Özellik Mühendisliği
Durdurma Kelimeleri (Stop Words):
Türkçe durdurma kelimeleri turkce-stop-words.txt dosyasından alındı.
Tokenizasyon ve Temizleme:
Kelime ayrıştırma ve gereksiz kelimelerin çıkarılması için nltk kullanıldı.
# 6. Sonuçlar ve Gelecek Çalışmalar
Sonuçlar:
Reddit gönderilerinden oluşan temiz ve etiketlenmiş bir veri seti oluşturuldu.
Veri seti, makine öğrenimi modelleri için uygun hale getirildi.
Gelecek Çalışmalar:
İntihara meyillilik analizi için bir sınıflandırma modeli geliştirilmesi.
Daha geniş ve çeşitli veri setlerinin toplanması.
Metin analiziyle erken müdahale mekanizmalarının geliştirilmesi.
Kullanılan Kütüphaneler
Python Kütüphaneleri: pandas, nltk, httpx, re, deep_translator.
Araçlar: Reddit API, JSON veri formatı.
