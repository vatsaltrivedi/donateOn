from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from DB_setup import Base, Cause, Region, Charity, User

engine = create_engine('sqlite:///charity.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

session = DBSession()

#check = session.query(Region).all()
# for c in check:
# 	if c.id>6:
# 		session.delete(c)
# 		session.commit()
# region1 = Region(name = 'Asia')
# session.add(region1)
# session.commit()

# region1 = Region(name = 'South America')
# session.add(region1)
# session.commit()

# region1 = Region(name = 'North America')
# session.add(region1)
# session.commit()

# region1 = Region(name = 'Europe')
# session.add(region1)
# session.commit()

# region1 = Region(name = 'Africa')
# session.add(region1)
# session.commit()

# region1 = Region(name = 'Australia')
# session.add(region1)
# session.commit()


# cause1 = Cause(name = 'Aged')
# session.add(cause1)
# session.commit()

# cause1 = Cause(name = 'Family')
# session.add(cause1)
# session.commit()

# cause1 = Cause(name = 'Disabled')
# session.add(cause1)
# session.commit()

# cause1 = Cause(name = 'Housing')
# session.add(cause1)
# session.commit()

# cause1 = Cause(name = 'Medical Welfare')
# session.add(cause1)
# session.commit()

# cause1 = Cause(name = 'Religious')
# session.add(cause1)
# session.commit()

# cause1 = Cause(name = 'Animals')
# session.add(cause1)
# session.commit()

# cause1 = Cause(name = 'Education')
# session.add(cause1)
# session.commit()

# cause1 = Cause(name = 'Health')
# session.add(cause1)
# session.commit()


# charity1 = Charity(name = 'WHO Asia', description = 'working for health in asia. ', contact ='ABC xx ', cause_id = 9, region_id =1)
# session.add(cause1)
# session.commit()

# charity1 = Charity(name = '22q11 Ireland', description = 'The 22q11 Ireland Support Group was set up to provide help, support and accurate information to Irish families. ', contact ='Organisation ID: CHY17647', cause_id = 2, region_id =4)
# session.add(cause1)
# session.commit()


# charity1 = Charity(name = 'ADAPT', description = 'ADAPT Services is a voluntary organisation set up in 1974 which provides a wide range of services for women survivors of domestic abuse', contact ='Organisation ID: CHY7405', cause_id = 2, region_id =4)
# session.add(charity1)
# session.commit()
# charity1 = Charity(name = 'Age Action', description = 'Age Action is the national charity on ageing and older people. ', contact ='Organisation ID: CHY17647', cause_id = 1, region_id =4)
# session.add(charity1)
# session.commit()
# charity1 = Charity(name = 'ASH Animal Rescue', description = 'ASH Animal Rescue, is a No Kill animal rescue shelter located in Co.Wicklow.', contact ='Organisation ID: CHY17647', cause_id = 6, region_id =4)
# session.add(charity1)
# session.commit()
# charity1 = Charity(name = 'Cerebral Palsy Support Ireland', description = 'Cerebral Palsy Sport Ireland (CPSI) was founded in 1978 to provide sport and recreational opportunities to individuals with Cerebral Palsy/ Other Physical Disabilities', contact ='Organisation ID: CHY17647', cause_id = 9, region_id =4)
# session.add(charity1)
# session.commit()
charity1 = Charity(name = 'COPE Galway', description = 'COPE Galway is a Galway based charity working in Galway to fight isolation. ', contact ='Organisation ID: CHY17647', cause_id = 9, region_id =4)
session.add(charity1)
session.commit()
charity1 = Charity(name = 'DEBRA Ireland', description = 'DEBRA Ireland is the national charity established in 1988 to provide patient support services and to drive research into treatments and cures for those living with the genetic skin condition ', contact ='Organisation ID: CHY17647', cause_id = 9, region_id =4)
session.add(charity1)
session.commit()
