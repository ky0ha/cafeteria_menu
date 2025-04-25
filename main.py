from sql_manager import SQLManager
from logger import logger, debugger
from time import strftime
import pandas as pd
import random

def extract_data(is_summer=False):
    logger.info(f"提取数据中... is_summer: {is_summer}")
    debugger.info(f"提取数据中... is_summer: {is_summer}")

    with SQLManager() as sql:
        if is_summer:
            data = sql.complex_query(
                """WITH a AS (
                SELECT F_NAME FROM menus
                GROUP BY F_NAME
                HAVING 
                SUM(CASE WHEN f_taste="麻辣" THEN 1 ELSE 0 END) >= 2 AND
                SUM(CASE WHEN f_taste="清淡" THEN 1 ELSE 0 END) >= 1 AND
                SUM(CASE WHEN f_meator="荤菜" THEN 1 ELSE 0 END) == 3 AND
                SUM(CASE WHEN f_type="凉菜" THEN 1 ELSE 0 END) >= 1
                )
                SELECT DISTINCT f_name FROM a ORDER BY RANDOM() LIMIT 6;"""
            )
        else:
            data = sql.complex_query(
                """WITH 
-- 先随机选择3个荤菜
荤菜 AS (
    SELECT f_name, f_taste, f_type, f_meator
    FROM menus
    WHERE f_meator = '荤菜'
    ORDER BY RANDOM()
    LIMIT 3
),
-- 再随机选择3个素菜
素菜 AS (
    SELECT f_name, f_taste, f_type, f_meator
    FROM menus
    WHERE f_meator = '素菜'
    ORDER BY RANDOM()
    LIMIT 3
),
-- 合并结果
合并结果 AS (
    SELECT * FROM 荤菜
    UNION ALL
    SELECT * FROM 素菜
)
-- 最终筛选满足条件的组合
SELECT * FROM 合并结果
WHERE (
    SELECT COUNT(*) FROM 合并结果 WHERE f_taste = '麻辣'
) >= 2
AND (
    SELECT COUNT(*) FROM 合并结果 WHERE f_taste = '清淡'
) >= 1
AND (
    SELECT COUNT(*) FROM 合并结果 WHERE f_type = '凉菜'
) >= 1;"""
            )
    
    return data

print(extract_data())
