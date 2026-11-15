from agent.connection import get_connection

c = get_connection()

try:
    with c.cursor() as cur:
        cur.execute("select CURRENT_USER(), CURRENT_ROLE(), CURRENT_WAREHOUSE(), (SELECT COUNT(*) FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.CUSTOMER)")
        print(cur.fetchone())
finally:
    c.close()
