import pytest
from Dbase import Session, Student  # лок. импорт

@pytest.fixture(scope="function")
def session():
    session = Session()
    yield session
    session.rollback()
    session.close()

def test_add_student(session):
    student = Student(user_id=1, level="бакалавриат", education_form="очная", subject_id=101)
    session.add(student)
    session.commit()

    from_db = session.query(Student).filter_by(user_id=1).first()
    assert from_db is not None
    assert from_db.education_form == "очная"

def test_update_student_level(session):
    student = Student(user_id=2, level="бакалавриат", education_form="очная", subject_id=102)
    session.add(student)
    session.commit()

    student.level = "магистратура"
    session.commit()

    updated = session.query(Student).filter_by(user_id=2).first()
    assert updated.level == "магистратура"

def test_change_subject(session):
    student = Student(user_id=3, level="аспирантура", education_form="дистанционная", subject_id=201)
    session.add(student)
    session.commit()

    student.subject_id = 202
    session.commit()

    updated = session.query(Student).filter_by(user_id=3).first()
    assert updated.subject_id == 202
