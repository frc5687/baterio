from sqlalchemy import Column, Integer, String, Boolean, create_engine, Text, DATETIME, JSON
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
import os

Bazo = declarative_base()


class UzantoV2(Bazo):
	__tablename__ = 'UzantoV2'
	uzanto_id = Column(String(36), primary_key=True)
	estas_administranto = Column(Boolean)
	retpoŝto = Column(Text(collation='utf8_general_ci'))
	unua_nomo = Column(Text(collation='utf8_general_ci'))
	familia_nomo = Column(Text(collation='utf8_general_ci'))
	pasvorto = Column(Text(collation='utf8_general_ci'))
	# Info de Google OAuth
	google_id = Column(Text())
	google_ekstra = Column(JSON)


class UzantoV1(Bazo):
	__tablename__ = 'UzantoV1'
	uzanto_id = Column(String(36), primary_key=True)
	estas_administranto = Column(Boolean)
	# Info de Google OAuth v2
	retpoŝto = Column(Text(collation='utf8_general_ci'))
	google_id = Column(Text())
	unua_nomo = Column(Text(collation='utf8_general_ci'))
	familia_nomo = Column(Text(collation='utf8_general_ci'))
	plena_nomo = Column(Text(collation='utf8_general_ci'))
	bildo = Column(Text())
	hd = Column(Text(collation='utf8_general_ci'))


class KunsidoV1(Bazo):
	__tablename__ = 'KunsidoV1'
	kunsidon_id = Column(String(36), primary_key=True)
	uzanto_id = Column(String(36))
	valida_ĝis = Column(DATETIME)


class BaterioV1(Bazo):
	__tablename__ = 'BaterioV1'
	baterio_id = Column(String(36), primary_key=True)
	baterio_nomo = Column(Text(collation='utf8_general_ci'))
	modelo = Column(Text(collation='utf8_general_ci'))

	okazaĵoj = relationship('BaterioOkazaĵoV1', back_populates='baterio')


class BaterioOkazaĵoV1(Bazo):
	__tablename__ = 'BaterioOkazaĵoV1'
	okazaĵo_id = Column(String(36), primary_key=True)
	baterio_id = Column(String(36))
	data = Column(JSON)

	baterio = relationship('BaterioV1', back_populates='okazaĵoj')


motoro = create_engine(os.environ['datumbazoAdreso'])
Bazo.metadata.create_all(motoro)
Bazo.metadata.bind = motoro
DBKunsido = sessionmaker(bind=motoro)
