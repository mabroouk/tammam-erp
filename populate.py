from Receipt_Entry_Flask import db, User
db.create_all()
if not User.query.filter_by(username='ahmed').first():
    db.session.add(User(username='ahmed', password='judy'))
    db.session.commit()
    print('✅ User created: ahmed / judy')
else:
    print('User already exists.')
