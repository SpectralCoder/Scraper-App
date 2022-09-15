from sqlalchemy.orm import Session
import model, schema

def get_items(db: Session):
    return db.query(model.info).all()

def get_items_by_pincode(db: Session, pincode: int):
    return db.query(model.info).filter(model.info.pincode == pincode).all()