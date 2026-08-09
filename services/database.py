import sqlite3
from pathlib import Path
from datetime import datetime


# ============================================================
# DATABASE CONFIGURATION
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_PATH = BASE_DIR / "prompt_optimizer.db"


# ============================================================
# DATABASE CONNECTION
# ============================================================

def get_connection():
    """
    Create a connection to the SQLite database.
    """

    connection = sqlite3.connect(
        DATABASE_PATH,
        check_same_thread=False,
    )

    connection.row_factory = sqlite3.Row

    return connection


# ============================================================
# INITIALIZE DATABASE
# ============================================================

def init_database():
    """
    Create the prompt_history table if it doesn't exist.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS prompt_history (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            original_prompt TEXT NOT NULL,

            final_score INTEGER,

            clarity INTEGER,

            context INTEGER,

            specificity INTEGER,

            optimized_prompt TEXT,

            created_at TEXT NOT NULL

        )
        """
    )

    connection.commit()

    connection.close()


# ============================================================
# SAVE PROMPT
# ============================================================

def save_prompt(
    original_prompt,
    final_score,
    clarity,
    context,
    specificity,
    optimized_prompt,
):
    """
    Save an optimized prompt to the database.
    """

    connection = get_connection()

    cursor = connection.cursor()

    created_at = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    cursor.execute(
        """
        INSERT INTO prompt_history (
            original_prompt,
            final_score,
            clarity,
            context,
            specificity,
            optimized_prompt,
            created_at
        )

        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            original_prompt,
            final_score,
            clarity,
            context,
            specificity,
            optimized_prompt,
            created_at,
        ),
    )

    connection.commit()

    connection.close()


# ============================================================
# GET HISTORY
# ============================================================

def get_prompt_history():
    """
    Return all saved prompts.

    Newest prompts are returned first.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            id,
            original_prompt,
            final_score,
            clarity,
            context,
            specificity,
            optimized_prompt,
            created_at

        FROM prompt_history

        ORDER BY id DESC
        """
    )

    rows = cursor.fetchall()

    connection.close()

    return rows


# ============================================================
# DELETE PROMPT
# ============================================================

def delete_prompt(prompt_id):
    """
    Delete one prompt from history.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM prompt_history
        WHERE id = ?
        """,
        (prompt_id,),
    )

    connection.commit()

    connection.close()