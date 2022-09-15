from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta




#CONSULTA1 TABLE
consulta1 = Table("consulta1", meta,
 Column("driverRef", String(255)),
 Column("cuenta", Integer),
 Column("position", Integer)
)

#CONSULTA2 TABLE
consulta2 = Table("consulta2", meta,
 Column("nombre", String(255)),
 Column("cuenta", Integer),
 Column("nationality", String(255))
)

#CONSULTA3 TABLE
consulta3 = Table("consulta3", meta,
 Column("year", Integer),
 Column("maximo", Integer)
)



#CONSULTA4 TABLE
consulta4 = Table("consulta4", meta,
 Column("name", String(255)),
 Column("cuenta", Integer)
)
