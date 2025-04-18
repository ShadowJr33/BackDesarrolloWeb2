from connection import SessionLocal

class BaseDAO:

    @staticmethod
    def execute_query(query_fn):
        try:
            with SessionLocal() as session:
                return query_fn(session)
        except Exception as e:
            print(f'Error ejecutando query con SQLAlchemy: {e}')
            return None
