from flask import Flask, render_template, request, flash, url_for, redirect
application = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from DB_setup import Base, Cause, Region, Charity, User



engine = create_engine('sqlite:///charity.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

session = DBSession()


@application.route('/')
@application.route('/home')
def home():
	cause = session.query(Cause).all()
	region = session.query(Region).all()
	k=0
	return render_template('index.html', cause = cause, region = region, k = k)


@application.route('/friends')
def friends():
	return render_template('friends.html')

@application.route('/activity')
def activity():
	return render_template('activity.html')

@application.route('/about')
def about():
	return render_template('about.html')


@application.route('/bycause', methods =['GET','POST'])
def bycause():
	searchword = request.args.get('cause', '')
	causes = session.query(Charity).filter_by(id = searchword)

	return render_template('bycause.html', causes = causes) 

@application.route('/donate', methods =['GET','POST'])
def donate():
	if request.method == 'POST':
		flash("Donated Succesfully .. Share with your friends on Facebook")
		return redirect(url_for('home'))
	id = request.args.get('charity','')
	charity = session.query((Charity)).filter_by(id = id)
	return render_template('donate.html', charity = charity)
@application.route('/charity')
def charity():
	cha = session.query(Charity).all()
	return render_template('donate.html', charity = cha)
if __name__ == '__main__':
	application.debug = True
	application.secret_key = '12345'
	application.run('0.0.0.0')
