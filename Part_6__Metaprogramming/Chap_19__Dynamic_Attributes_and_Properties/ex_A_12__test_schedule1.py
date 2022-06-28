#  Reference: https://github.com/fluentpython/example-code-2e/blob/master/22-dyn-attr-prop/oscon/test_schedule_v1.py

import pytest

import ex_19_9__schedule1 as schedule


@pytest.fixture
def records():
    yield schedule.load(schedule.JSON_PATH)


def test_load(records):
    assert len(records) == 895


def test_record_attr_access():
    rec = schedule.Record(spam=99, eggs=12)
    assert rec.spam == 99
    assert rec.eggs == 12


def test_venue_record(records):
    venue = records['venue.1469']
    assert venue.serial == 1469
    assert venue.name == 'Exhibit Hall C'
