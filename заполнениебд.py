session = db_session.create_session()

category1 = Category(
    front_name='Большая пицца',
    back_name='big-pizza',
    describtion='aasd'
)
category2 = Category(
    front_name='Маленькая пицца',
    back_name='small-pizza',
    describtion='qqwe'
)
product1 = Product(
    back_name='zakIardbo_Q.jpg',
    front_name='Первая большая пицца',
    description='PPPPPPIIIIIIIZZZZZZZAAAAAA',
    cost=130,
    category=category1
)
product2 = Product(
    back_name='zakIardbo_Q.jpg',
    front_name='Вторая большая пицца',
    description='PPPPPPIIIIIIIZZZZZZZAAAAAA',
    cost=140,
    category=category1
)
product3 = Product(
    back_name='zakIardbo_Q.jpg',
    front_name='Третья большая пицца',
    description='PPPPPPIIIIIIIZZZZZZZAAAAAA',
    cost=100,
    category=category1
)
product4 = Product(
    back_name='zakIardbo_Q.jpg',
    front_name='Четвертая большая пицца',
    description='PPPPPPIIIIIIIZZZZZZZAAAAAA',
    cost=130,
    category=category1
)
product5 = Product(
    back_name='zakIardbo_Q.jpg',
    front_name='Первая маленькая пицца',
    description='PPPPPPIIIIIIIZZZZZZZAAAAAA',
    cost=130,
    category=category2
)
product6 = Product(
    back_name='zakIardbo_Q.jpg',
    front_name='Вторая маленькая пицца',
    description='PPPPPPIIIIIIIZZZZZZZAAAAAA',
    cost=130,
    category=category2
)
product7 = Product(
    back_name='zakIardbo_Q.jpg',
    front_name='Третья маленькая пицца',
    description='PPPPPPIIIIIIIZZZZZZZAAAAAA',
    cost=130,
    category=category2
)
product8 = Product(
    back_name='zakIardbo_Q.jpg',
    front_name='Четвертая маленькая пицца',
    description='PPPPPPIIIIIIIZZZZZZZAAAAAA',
    cost=130,
    category=category2
)
user = User(
    phone_number="9933",
    role="cook"
)
worker_data = WorkerData(
    worker=user
)
worker_data.set_password("123")

user2 = User(
    phone_number="9944",
    role="deliveryman"
)
worker_data2 = WorkerData(
    worker=user2
)

user3 = User(
    phone_number="9966",
    role="admin"
)
worker_data3 = WorkerData(
    worker=user3
)
worker_data.set_password("123")
worker_data2.set_password("123")
worker_data3.set_password("123")

session.add(category1)
session.add(category2)
session.add(product1)
session.add(product2)
session.add(product3)
session.add(product4)
session.add(product5)
session.add(product6)
session.add(product7)
session.add(product8)
session.add(user)
session.add(worker_data)
session.add(user2)
session.add(worker_data2)

session.add(user3)
session.add(worker_data3)

session.commit()
session.commit()
session.close()

session = db_session.create_session()
user3 = User(
    phone_number="9966",
    role="admin"
)
worker_data3 = WorkerData(
    worker=user3
)
worker_data3.set_password("123")
session.add(user3)
session.add(worker_data3)

session.commit()
session.close()