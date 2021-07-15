
from sqlalchemy.sql.sqltypes import Float
import db
from sqlalchemy import Column, Integer, String, Boolean

class Todo(db.Base):
    __tablename__ = 'todo'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title= Column(String(100))
    complete = Column(Boolean, unique=False, default=False)
    
    def __init__(self, title, complete):
        self.title = title
        self.complete = complete