from fastapi import Depends, FastAPI, HTTPException
import schema, model, utils
from sqlalchemy.orm import Session
from database import SessionLocal, engine, get_database_session
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


model.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "welcome to FastAPI!"}

@app.get("/item/", response_model=schema.Info)
def read_items(db: Session = Depends(get_database_session)):
    try:
        users = utils.get_items(db)
        return JSONResponse(jsonable_encoder(users))
    except Exception as e:
        return {'error': 'Something went wrong', 'exception': str(e)}

@app.get("/item/{pincode}", response_model=list[schema.Info])
def read_item(pincode: int, db: Session = Depends(get_database_session)):
    try:
        item = utils.get_items_by_pincode(db, pincode=pincode)
        if item is None:
            raise HTTPException(status_code=404, detail="item not found")
        return JSONResponse(content=jsonable_encoder(item))
    except Exception as e:
        return {'error': 'Something went wrong', 'exception': str(e)}