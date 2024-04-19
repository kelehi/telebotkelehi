import sqlalchemy as db


class Database:
    def __init__(self, file='data_base_user_stoke_market_bot.db'):
        self.file = file
        self.engine = db.create_engine(f'sqlite:///{self.file}')
        self.conn = self.engine.connect()
        self.users = self.__scripts_base()

    def __scripts_base(self):
        metadata = db.MetaData()
        users = db.Table('users', metadata, autoload_with=self.engine)
        return users

    def write_database(self, activ: str, initial_time: str, end_time: str):
        insertion_query = self.users.insert().values([
            {'activ': activ, 'initial_time': initial_time, 'end_time': end_time}])
        self.conn.execute(insertion_query)

    def read_database(self):
        select_all_query = db.select(self.users)
        select_all_results = self.conn.execute(select_all_query)
        return select_all_results.fetchall()

    def __del__(self):
        self.conn.close()