    the bot created as terminal with commands
    like windows
    you can speak with the bot with terminal help
    i do commands to show all commands(with description)
if you want do all commands to json file you can do like that **{
    "command_name": "command description",
}**
```if you want at DB you can created table with commands index command name and command description```
```py
    #this example only for postgres
    from sqlalchemy import create_engine, Column, Integer, String, DateTime, BigInteger
    from sqlalchemy.ext.declarative import declarative_base
    DATABASE_URL = "conn://postgres:to@your:d/b"


    engine = create_engine(DATABASE_URL)

    
    Base = declarative_base()

    
    class User(Base):
        __tablename__ = 'first_archive'
        index = Column(Integer, primary_key=True, autoincrement=True)
        command_name = Column(String, index=True)
        command_description = Column(String, index=True)
```


***if i have a lot of stars at this repository i add command at this command you can apload your files with your values and command to reconect bot***


