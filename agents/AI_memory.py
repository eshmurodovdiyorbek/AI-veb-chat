import uuid

from database import get_connection
from langchain_postgres import PostgresChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

# PostgreSQL jadvallari nomi
CONVERSATIONS_TABLE = "conversations"
HISTORY_TABLE = "chat_history"


def create_conversation(user_id, title="Yangi suhbat"):
    """Yangi suhbat yaratadi."""

    conversation_id = str(uuid.uuid4())

    with get_connection() as conn:
        conn.execute(
            """
            INSERT INTO conversations (id, user_id, title)
            VALUES (%s, %s, %s)
            """,
            (conversation_id, user_id, title)
        )
    print("CREATED USER:", user_id)
    print("CREATED ID:", conversation_id)
    return conversation_id


def get_user_conversations(user_id):
    """Foydalanuvchining barcha suhbatlarini chiqaradi."""

    with get_connection() as conn:
        result = conn.execute(
            """
            SELECT id, title, created_at, updated_at
            FROM conversations
            WHERE user_id = %s
            ORDER BY updated_at DESC
            """,
            (user_id,)
        )

        return result.fetchall()


def save_message(user_id, conversation_id, message):
    """Foydalanuvchi yoki AI xabarini saqlaydi."""

    with get_connection() as conn:
        # Suhbat shu foydalanuvchiga tegishlimi?
        result = conn.execute(
            """
            SELECT id FROM conversations
            WHERE id = %s AND user_id = %s
            """,
            (conversation_id, user_id)
        )

        if result.fetchone() is None:
            raise ValueError("Suhbat topilmadi!")

        history = PostgresChatMessageHistory(
            HISTORY_TABLE,
            str(conversation_id),
            sync_connection=conn
        )

        history.add_messages([message])

        conn.execute(
            """
            UPDATE conversations
            SET updated_at = NOW()
            WHERE id = %s
            """,
            (conversation_id,)
        )


def get_chat_history(user_id, conversation_id):
    """Tanlangan suhbat tarixini qaytaradi."""

    with get_connection() as conn:
        result = conn.execute(
            """
            SELECT id FROM conversations
            WHERE id = %s AND user_id = %s
            """,
            (conversation_id, user_id)
        )

        row =result.fetchone()

        print("Database result: ",row)
        if row is None:
            raise ValueError("Suhbat topilmadi!")

        history = PostgresChatMessageHistory(
            HISTORY_TABLE,
            str(conversation_id),
            sync_connection=conn
        )

        return history.messages


# Sinov
if __name__ == "__main__":

    USER_ID = "Diyorbek"

    llm = ChatGroq(
        model_name="openai/gpt-oss-120b",
        temperature=0
    )
    # 1. Yangi suhbat yaratamiz
    conversation_id = create_conversation(
        USER_ID,
        "Python darslari"
    )

    print("Yangi suhbat ID:", conversation_id)
    while True:
        user_input = input("\nSiz: ")

        if user_input.lower() == "stop":
            print("Suhbat yakunlandi.")
            break
    messages = get_chat_history(
        USER_ID,
        conversation_id
    )

    human_message = HumanMessage(content=user_input)
    messages.append(human_message)

    response = llm.invoke(messages)

    ai_response = response.content

    print("Diyorbek AI:",ai_response)
    save_message(
        USER_ID,
        conversation_id,
        human_message
    )

    save_message(
        USER_ID,
        conversation_id,
        AIMessage(content=ai_response)
    )
