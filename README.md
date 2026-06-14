# AgirDepresyonTespit

Çevrimiçi platformlardan toplanan metinleri kullanarak intihara meyilli
bireylerin paylaşımlarını analiz eden ve sınıflandıran bir doğal dil işleme
(NLP) projesi. Reddit'ten toplanan veriler temizlenir, Türkçeye çevrilir,
etiketlenir ve XLM-RoBERTa tabanlı bir model için hazır hale getirilir.

## Proje Yapısı

```
.
├── src/                      # Veri işleme pipeline'ı
│   ├── scrape_reddit.py      # 1. Reddit'ten veri toplama
│   ├── translate.py          # 2. İngilizce -> Türkçe çeviri + temizleme
│   ├── label.py              # 3. Etiketleme (0/1)
│   ├── preprocess.py         # 4. Tokenizasyon + stop word temizliği
│   └── merge.py              # 5. Tüm veriyi birleştirme
├── notebooks/                # Model eğitimi ve değerlendirme
│   ├── xlm_roberta_training.ipynb
│   ├── xlm_roberta_training_draft.ipynb
│   └── model_evaluation.ipynb
├── resources/
│   └── turkish_stopwords.txt # Türkçe durdurma kelimeleri
├── docs/
│   └── project_report.pdf    # Proje dokümanı
├── data/                     # Veri (sürüm kontrolüne dahil DEĞİL)
│   ├── raw/                  # Ham (İngilizce) gönderiler
│   ├── translated/           # Çevrilmiş gönderiler
│   ├── cleaned/              # Temizlenmiş metinler
│   ├── labeled/              # Etiketlenmiş veriler
│   └── combined/             # Birleştirilmiş nihai veri seti
├── requirements.txt
├── LICENSE
└── README.md
```

> **Not:** `data/` klasörü ve tüm `.csv` dosyaları `.gitignore` ile sürüm
> kontrolünün dışında tutulur. Veri kümeleri repoya commit'lenmez.

## Kurulum

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux / macOS
source .venv/bin/activate

pip install -r requirements.txt
```

## Pipeline'ı Çalıştırma

Scriptler proje kökünden, sırayla çalıştırılır:

```bash
python src/scrape_reddit.py   # 1. Veri toplama        -> data/raw/
python src/translate.py       # 2. Çeviri + temizleme  -> data/translated/
python src/preprocess.py      # 3. Tokenize + stopword -> data/cleaned/
python src/label.py           # 4. Etiketleme          -> data/labeled/
python src/merge.py           # 5. Birleştirme         -> data/combined/
```

Ardından `notebooks/xlm_roberta_training.ipynb` ile model eğitilir ve
`notebooks/model_evaluation.ipynb` ile değerlendirilir.

## Yöntem

1. **Veri Toplama** — Reddit'in herkese açık JSON uç noktası üzerinden ilgili
   subreddit'lerden (`r/SuicideWatch`, `r/depression`, `r/depression_help`,
   günlük konuşmalar vb.) gönderiler `httpx` ile çekilir.
2. **Temizleme ve Çeviri** — Küçük harfe çevirme, sembol/sayı temizliği, boş ve
   tekrar eden kayıtların kaldırılması; İngilizce metinler `deep-translator` ile
   API limitine uygun parçalara bölünerek Türkçeye çevrilir.
3. **Etiketleme** — İntihara meyilli gönderiler `1`, meyilli olmayanlar `0`.
4. **Özellik Mühendisliği** — `nltk` ile tokenizasyon ve Türkçe stop word
   temizliği (`resources/turkish_stopwords.txt`).
5. **Birleştirme** — Etiketlenmiş tüm CSV'ler tek bir temiz veri setinde
   birleştirilir.

## Sonuçlar

Reddit gönderilerinden oluşan temiz ve etiketlenmiş bir veri seti üretilmiş,
XLM-RoBERTa tabanlı sınıflandırma modeli için hazır hale getirilmiştir.

![output (1)](https://github.com/user-attachments/assets/6ad1e957-a0ce-44c7-9e0d-dac2893f3586)
![output](https://github.com/user-attachments/assets/528c711f-9631-47dd-910e-7624fe65318d)

## Gelecek Çalışmalar

- İntihara meyillilik analizi için sınıflandırma modelinin geliştirilmesi.
- Daha geniş ve çeşitli veri setlerinin toplanması.
- Metin analiziyle erken müdahale mekanizmalarının geliştirilmesi.

## Kullanılan Kütüphaneler

`pandas`, `numpy`, `scikit-learn`, `nltk`, `httpx`, `deep-translator`,
`transformers`, `torch`, `matplotlib`.
