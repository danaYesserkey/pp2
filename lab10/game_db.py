import json
from db import get_connection

def get_or_create_user(username):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id FROM game_user WHERE username = %s", (username,))
    row = cur.fetchone()

    if row:
        user_id = row[0]
    else:
        cur.execute(
            "INSERT INTO game_user (username) VALUES (%s) RETURNING id",
            (username,)
        )
        user_id = cur.fetchone()[0]
        conn.commit()

    cur.close()
    conn.close()
    return user_id


def get_last_user_state(user_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT level, score, game_state
        FROM user_score
        WHERE user_id = %s
        ORDER BY saved_at DESC
        LIMIT 1
    """, (user_id,))

    row = cur.fetchone()

    cur.close()
    conn.close()
    return row


def save_user_state(user_id, level, score, snake_body, food_pos):
    state = json.dumps({
        "snake": snake_body,
        "food": food_pos
    })

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO user_score (user_id, level, score, game_state)
        VALUES (%s, %s, %s, %s)
        """,
        (user_id, level, score, state)
    )

    conn.commit()
    cur.close()
    conn.close()

    print("Saved")