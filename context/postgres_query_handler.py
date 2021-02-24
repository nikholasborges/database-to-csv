class QueryHandler:

    def __init__(self, logObj):
        self.log = logObj

    def execute_query(self, cursor, query):
        
        cursor.execute(query)

        result_set = {
            'header': '',
            'content': '',
        }

        self.log.write(f'number of lines fetched: {cursor.rowcount}')

        result_set['header'] = [desc[0] for desc in cursor.description]
        result_set['content'] = cursor.fetchall()

        return result_set