import os
import dotenv
import sqlalchemy as alch


dotenv.load_dotenv()

passw = os.getenv("pass_sql")
dbName="rick_morty"
connectionData=f"mysql+pymysql://root:{passw}@localhost/{dbName}"
engine = alch.create_engine(connectionData)
