import pytest


@pytest.mark.db
def test_active_qa_lead_exists_in_db(db_connection):
    """Validates user status and role using SQL queries."""
    cursor = db_connection.cursor()
    cursor.execute(
        "SELECT username, role FROM users WHERE is_active = 1 AND role = ?",
        ("QA_Lead",),
    )
    row = cursor.fetchone()

    assert row is not None, "Expected an active QA_Lead user in database"
    assert row[0] == "standard_user"
    assert row[1] == "QA_Lead"
