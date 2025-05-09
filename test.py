from sql_manager.sql_manager import SQLManager
from logger import logger, debugger
import pandas as pd

df = pd.read_excel("test.xlsx")
for row in df.iterrows():
    logger.debug(row[1].values)
    with SQLManager() as sql:
        sames = sql.select_from_table(
            "menus",
            ["f_name"],
            where = f"f_name = '{row[1].values[0]}'"
        )
        
        if sames:
            logger.info(f"菜品名 {row[1].values[0]} 已存在，跳过该菜品")
            continue
        
        sql.insert_into_table(
            "menus",
            row[1].values,
            key = ["f_name", "f_taste", "f_type", "f_meator"]
        )
    f_name, f_taste, f_type, f_meator = row[1].values
    logger.info(f"insert {f_name} {f_taste} {f_type} {f_meator}")
    

# sql = SQLManager()

# with sql:
#     # sql.insert_into_table(
#     #     "cookers",
#     #     ['jack'],
#     #     ['c_name']
#     # )
#     pass

# logger = setup_logger("main")
# logger.info("test1")
# logger.debug("test2")
# debugger.info("test3")