# asywee

Asywee is asynchronous ORM framework based on [peewee](https://github.com/coleifer/peewee). For now it supports only PostgreSQL using [aiopg](https://github.com/aio-libs/aiopg).


Some examples
-------------
You can test asywee using following little example:

```python
import asywee

db = asywee.PostgresqlDatabase(database='ormageddon', user='postgres', host='127.0.0.1')

class User(asywee.Model):

    id = asywee.PrimaryKeyField()

    class Meta:
        database = db

async def get_user(user_id):
    return await User.get(User.id == user_id)

async def print_users(start=None, stop=None):
    async for user in User.select()[start:stop]:
        print(user)

async def create_user():
    user = User()
    await user.save()
```

Transactions
------------

```python
async def manual_transaction():
    await db.begin()
    try:
        # do whatever you need
    except:
        await db.rollback()
        raise
    else:
        await db.commit()

async def transaction_context():
    async with db.transaction() as transaction:
        # do whatever you need
```
