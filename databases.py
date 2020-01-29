from model import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session
def con ():
	engine = create_engine('sqlite:///gamers.db')
	Base.metadata.create_all(engine)
	DBSession = scoped_session(sessionmaker(bind=engine,autoflush=False))
	session = DBSession()
	return session


def Signup(Gmail,name, password):
	session = con()
	gamers_info = Users(
		Gmail = Gmail,
		name = name,
		password = password)
	session.add(gamers_info)
	session.commit()


def db_login(N, psw):
	session = con()
	gamers_info = session.query(
		Users).filter_by(
		name=N).first()
	if gamers_info == None:
		return False
	else:
		if gamers_info.name == N:
			if gamers_info.password == psw:
				return True
			else: 
				return False
		else:
			return False










def Update_User(gamer_id,n, psw):
	session = con()
	gamers_info = session.query(
		Users).filter_by(
		gamer_id=gamer_id).first()
	gamers_info.name = n
	gamers_info.psw = psw
	session.commit()



def Delete_User(gamer_id, name):
	session = con()
	session.query(Users).filter_by(
		gamer_id=gamer_id).delete()
	session.commit()    

def query_users():
	session = con()
	return session.query(Users).all()

# print(query_users())