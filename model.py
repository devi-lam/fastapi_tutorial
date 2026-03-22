# model.py adalah file tempat kamu mendefinisikan struktur tabel database dalam bentuk kelas Python.
# Analoginya seperti ini:
# Database = gudang
# Tabel = rak di gudang
# models.py = blueprint/denah raknya — tinggi berapa, ada berapa kolom, tipe barangnya apa

from database import Base
from sqlalchemy import Column, Integer, VARCHAR

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(VARCHAR(255))
    author = Column(VARCHAR(255))
    publish_date = Column(VARCHAR(255))

