import psycopg2, json, openpyxl

class MetaDatabase:

    @staticmethod
    def text_pg():
        conn = psycopg2.connect(dbname="metadb", user="postgres", password="pwd")
        cur = conn.cursor(cursor_factory=psycopg2.extensions.cursor)
        cur.execute("SELECT * FROM t_process")
        print(cur.fetchone()[2])
        print(1)

        '''
        conn
        try:
        ...     cur.execute("SELECT * FROM barf")
        ... except psycopg2.Error as e:
            ...     pass

                logger = logging.getLogger('sql_debug')
                logger.info(self.mogrify(sql, args))

                try:
                    psycopg2.extensions.cursor.execute(self, sql, args)
                except Exception, exc:
                    logger.error("%s: %s" % (exc.__class__.__name__, exc))
                    raise

        conn = psycopg2.connect(DSN)
        cur = conn.cursor(cursor_factory=LoggingCursor)
        cur.execute("INSERT INTO mytable VALUES (%s, %s, %s);"
        
        
        Import File config:
        
        
        '''

if __name__ == '__main__':
    pass