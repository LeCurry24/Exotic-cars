import uvicorn
from fastapi import FastAPI, Depends
from sqlmodel import Session, select, func
from db import get_session
from models.cars import Cars
from models.people import People
from models.tokens import Token
from models.users import User

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello World'}

@app.get("/cars")
def get_cars(session: Session = Depends(get_session)):
    statement = select(Cars)
    results = session.exec(statement).all()
    return results

@app.post('/cars/add')
async def add_Cars(car: Cars, session: Session = Depends(get_session)):
    new_car = Cars(name=car.name, year=car.year, price=car.price)
    session.add(new_car)
    session.commit()
    return {"Cars Added": car.name}
    

@app.get("/people")
def get_people(session: Session = Depends(get_session)):
    statement = select(
        People.id,
        People.name,
        func.array_agg(Cars.name).label('cars')
    ).join(
        Cars, Cars.id == People.car_id
    ).group_by(
        People
    )
    print(statement)
    results = session.exec(statement).mappings().all()
    return results

@app.post('/people/add')
async def add_people(people: People, session: Session = Depends(get_session)):
    people = People(name=people.name)
    session.add(people)
    session.commit()
    return {"People Added": people.name}

@app.get("/tokens")
def get_tokens(session: Session = Depends(get_session)):
    statement = select(Token)
    results = session.exec(statement).all()
    return results

@app.get("/users")
def get_users(session: Session = Depends(get_session)):
    statement = select(User)
    results = session.exec(statement).all()
    return results

if __name__ == '__main__':
    uvicorn.run('main:app', host='localhost', port=8000, reload=True)