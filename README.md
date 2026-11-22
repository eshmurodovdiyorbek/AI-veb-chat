# 🤖 Diyorbek AI — Intelligent AI Assistant

**Diyorbek AI** — Python va LangChain texnologiyalari asosida ishlab chiqilayotgan shaxsiy AI Assistant. Ushbu loyiha foydalanuvchilarga savollarga javob topish, internetdan ma'lumot qidirish va oddiy hisob-kitoblarni bajarishda yordam berish uchun yaratilgan.

Loyihaning asosiy maqsadi — foydalanuvchi bilan tabiiy tilda muloqot qila oladigan, kerakli vositalardan foydalana oladigan va kelajakda doimiy xotiraga ega bo‘ladigan AI yordamchi yaratish.

## ✨ Asosiy imkoniyatlar

- 💬 **AI Chat:** foydalanuvchi bilan tabiiy tilda suhbatlashish.
- 🧠 **AI Agent:** foydalanuvchi topshirig‘iga qarab kerakli vositalarni tanlash.
- 🔎 **Smart Search:** DuckDuckGo orqali internetdan ma'lumot qidirish.
- 🧮 **Multiply Tool:** ikkita sonni ko‘paytirish.
- 💾 **Chat Memory:** suhbat tarixini boshqarish imkoniyati.
- 🌐 **Web Interface:** Chainlit yordamida yaratilgan chat interfeysi.

## 🏗️ Architecture — Loyiha arxitekturasi

Loyiha modulli arxitektura asosida tashkil etilgan. Har bir Python fayli alohida vazifani bajaradi.
Diyorbek_AI/
│
├── app_chainlit.py       # Asosiy chat dasturi
├── ai_memory.py          # AI xotirasini boshqarish
├── database.py           # PostgreSQL bilan ulanish
├── tools.py              # AI agent vositalari
├── .env                  # Maxfiy sozlamalar
└── requirements.txt      # Kutubxonalar

### 📂 Fayllarning vazifalari

| Fayl | Vazifasi |
|---|---|
| `app_chainlit.py` | Chainlit interfeysi va AI agentni ishga tushirish |
| `ai_memory.py` | Suhbat tarixini saqlash va qayta olish |
| `database.py` | PostgreSQL ma'lumotlar bazasiga ulanish |
| `tools.py` | AI agent foydalanadigan qo‘shimcha vositalar |
| `.env` | API kalitlari va ma'lumotlar bazasi sozlamalari |
| `requirements.txt` | Loyihada ishlatiladigan Python kutubxonalari |

## 🛠️ Texnologiyalar

| Texnologiya | Vazifasi |
|---|---|
| Python 3.12 | Asosiy dasturlash tili |
| Chainlit | AI chat interfeysi |
| LangChain | AI agent va LLM bilan ishlash |
| LangChain Classic | AgentExecutor va agent yaratish |
| ChatGroq | AI model bilan aloqa |
| GPT-OSS-120B | Foydalanilayotgan AI model |
| DuckDuckGo Search | Internetdan ma'lumot qidirish |
| Python-dotenv | Maxfiy sozlamalarni `.env` orqali yuklash |
| PostgreSQL | Suhbat ma'lumotlarini saqlash |
| LangChain Postgres | PostgreSQL bilan chat history integratsiyasi |

## ⚙️ AI Agent qanday ishlaydi?

Diyorbek AI quyidagi tartibda ishlaydi:

1. Foydalanuvchi chat oynasiga savol yuboradi.
2. Chainlit xabarni Python dasturiga uzatadi.
3. LangChain agent foydalanuvchi so‘rovini qayta ishlaydi.
4. Zarur bo‘lsa, agent mavjud vositalardan foydalanadi.
5. ChatGroq orqali AI javobi olinadi.
6. Javob foydalanuvchiga chat interfeysida ko‘rsatiladi.

### Mavjud Tools

**1. DuckDuckGo Search**

Internetdan kerakli ma'lumotlarni qidirish uchun ishlatiladi.

**2. Multiply Tool**

Ikkita sonni ko‘paytirish uchun ishlatiladi.

## 🧠 AI Memory — Xotira tizimi

Loyihada LangChain `RunnableWithMessageHistory` orqali suhbat tarixini kontekst sifatida ishlatish mexanizmi mavjud.

PostgreSQL asosidagi doimiy xotira tizimi ham ishlab chiqilmoqda.

Uning asosiy maqsadlari:

- Suhbatlarni ma'lumotlar bazasida saqlash.
- Oldingi suhbatlarni qayta ochish.
- Har bir suhbatni alohida boshqarish.
- AI uchun suhbat kontekstini taqdim etish.

**Eslatma:** PostgreSQL xotirasining to‘liq integratsiyasi loyiha rivojlanish bosqichida.

## 📦 O‘rnatish

### 1. Repository'ni yuklab olish

```bash
git clone <YOUR_REPOSITORY_URL>
```

### 2. Loyiha papkasiga kirish

```bash
cd Diyorbek_AI
```

### 3. Virtual muhit yaratish

```bash
python -m venv .venv
```

### 4. Virtual muhitni faollashtirish (Windows)

```bash
.venv\Scripts\activate
```

### 5. Kutubxonalarni o‘rnatish

```bash
pip install -r requirements.txt
```

## 🔐 Environment Variables

Loyiha papkasida `.env` faylini yarating:

```env
GROQ_API_KEY=your_groq_api_key

DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database
DB_USER=your_username
DB_PASSWORD=your_password
```

Haqiqiy API kalitlari va parollarni GitHub'ga yuklamang.

## 🚀 Ishga tushirish

`app_chainlit.py` joylashgan papkada terminalni oching:

```bash
chainlit run app_chainlit.py
```

Brauzerda quyidagi manzilni oching:

```text
http://localhost:8000
```

## 👥 Kimlar uchun foydali?

- **Talabalar:** savollarga javob topish va ma'lumot izlash.
- **Dasturchilar:** dasturlash bo‘yicha savollarni muhokama qilish.
- **O‘quvchilar:** turli mavzularni o‘rganish.
- **Oddiy foydalanuvchilar:** kundalik savollar va hisob-kitoblar.
- **Tadqiqotchilar:** internetdan dastlabki ma'lumotlarni qidirish.

## 📊 Loyiha samaradorligi

Hozircha Diyorbek AI bo‘yicha real foydalanuvchilar ishtirokidagi statistik sinov o‘tkazilmagan. Shu sababli foydalanuvchilarga yordam berish foizi aniq belgilanmagan.

Kelajakda samaradorlik quyidagi ko‘rsatkichlar orqali o‘lchanadi:

- Foydalanuvchi savollariga to‘g‘ri javob berish foizi.
- Muvaffaqiyatli bajarilgan topshiriqlar soni.
- Foydalanuvchilarning qoniqish darajasi.
- Javob berish tezligi.
- Takroriy foydalanish ko‘rsatkichi.

## 👨‍💻 Muallif

**Diyorbek Eshmurodov**

Python, Artificial Intelligence, LangChain va AI Agent texnologiyalari asosida ishlab chiqilayotgan shaxsiy loyiha.

---

*Building an intelligent assistant, one step at a time.* 🚀
