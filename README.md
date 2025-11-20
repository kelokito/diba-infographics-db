# 📘 **README**

## 📁 Project Structure

```
src/
├── db/
│   ├── db_connection.py
│   └── queries/
│        ├── bibliographics_queries.sql
│        ├── users_queries.sql
│        └── general_queries.sql
│
├── bibliographics/
│   ├── bibliographics_data.py
│   └── bibliographics_repository.py
│
├── users/
│   ├── users_data.py
│   └── users_repository.py
│
├── general/
│   ├── general_data.py
│   └── general_repository.py
│
├── dashboard/
│   ├── dashboard_service.py
│   └── dashboard_view.py
│
└── models/
    ├── bibliographics_model.py
    ├── users_model.py
    └── general_model.py
```

---

# 🚀 **1. Requirements**

You need:

* Python 3.9+
* Docker & Docker Compose
* `pip`
* Optionally pgAdmin (already included in docker-compose.yml)

---

# 🐳 **2. Running PostgreSQL with Docker**

Start the database and pgAdmin:

```bash
docker-compose up -d
```

To stop:

```bash
docker-compose down
```

### Database connection info (default)

| Item     | Value        |
| -------- | ------------ |
| Host     | localhost    |
| Port     | 5432         |
| User     | postgres     |
| Password | password     |
| DB name  | dashboard_db |

pgAdmin:
📍 [http://localhost:8080](http://localhost:8080)
Login: [admin@admin.com](mailto:admin@admin.com) / admin

---

# 🛠 **3. Python Setup**

### Step 1 — Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows
```

### Step 2 — Install Requirements

```bash
pip install -r requirements.txt
```

---

# 🔧 **4. Configure Environment Variables**

Create a `.env` file:

```
DB_HOST=localhost
DB_NAME=dashboard_db
DB_USER=postgres
DB_PASSWORD=password
```

---

# 🗄 **5. Create Tables**

Run SQL schema files manually:

```bash
psql -h localhost -U postgres -d dashboard_db -f src/db/queries/bibliographics_queries.sql
psql -h localhost -U postgres -d dashboard_db -f src/db/queries/users_queries.sql
psql -h localhost -U postgres -d dashboard_db -f src/db/queries/general_queries.sql
```

---

# 📥 **6. Ingest All Data**

Place your manually downloaded data files in:

```
/data/bibliographics.csv
/data/users.csv
/data/general.csv
```

Run ingestion:

```bash
python ingest_all.py
```

This:

* Loads .env
* Parses CSVs
* Inserts into all 3 tables

---

# 📊 **7. Run the Dashboard**

Depends on your view implementation.
If using Streamlit:

```bash
streamlit run src/dashboard/dashboard_view.py
```

If using a CLI view:

```bash
python -m src.dashboard.dashboard_view
```

---

# 🧪 **8. Testing**

```bash
pytest
```

---

# 📦 **9. Quick Commands**

| Action            | Command                                         |
| ----------------- | ----------------------------------------------- |
| Start DB          | `docker-compose up -d`                          |
| Stop DB           | `docker-compose down`                           |
| Ingest everything | `python ingest_all.py`                          |
| Run dashboard     | `streamlit run src/dashboard/dashboard_view.py` |
