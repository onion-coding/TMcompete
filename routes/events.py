from db import get_connection

def test_query():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT 1;")
    print(cur.fetchone())
    cur.close()
    conn.close()



# endpoints
# /browse           -> browse all competitions, will be the landing page
# /contact          -> contact details: email
# /login            -> Ubisoft Connect login (redirect to Ubisoft OAuth)
# /search           -> search competitions with filters
# /saved            -> user’s saved competitions
# /admin            -> moderation dashboard (approve ads, manage users)