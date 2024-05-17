import pytest
from src.utils import get_size, validate_record, add_record_to_batch
from tests.test_data import test_data
from src.config import MAX_RECORD_SIZE, MAX_BATCH_SIZE, MAX_NUMBER_OF_RECORDS

def test_get_size():
    '''
    Checks that byte size is calculated correctly
    '''
    assert get_size("hello") == 5
    assert get_size("你好") == 6  # Assuming UTF-8, Chinese characters should take 3 bytes each

def test_validate_record():
    '''
    Checks that records are validated accordingly
    '''
    max_size = MAX_RECORD_SIZE
    assert validate_record(test_data['small_record'], max_size) == True
    assert validate_record(test_data['medium_record'], max_size) == True
    assert validate_record(test_data['large_record'], max_size) == True
    assert validate_record(test_data['oversized_record'], max_size) == False
    assert validate_record(test_data['exactly_one_mb_record'], max_size) == True
    assert validate_record(test_data['just_below_one_mb_record'], max_size) == True
    assert validate_record(test_data['just_above_one_mb_record'], max_size) == False
    assert validate_record(123, max_size) == False  # Non-string input

def test_add_record_to_batch():
    '''
    Checks that records are added to batch, 
    this function assumes valid records
    '''
    batch = []
    batches = []
    record = 'test'
    current_batch_size = 0
    max_record_size = 10
    max_batch_size = 20
    max_number_of_records = 3
    batch, batches, current_batch_size = add_record_to_batch(record=record, 
                        batch=batch, 
                        batches=batches, 
                        current_batch_size=current_batch_size, 
                        max_batch_size=max_batch_size, 
                        max_number_of_records=max_number_of_records)
    assert len(batch) == 1
    batch, batches, current_batch_size = add_record_to_batch(record=record, 
                        batch=batch, 
                        batches=batches, 
                        current_batch_size=current_batch_size, 
                        max_batch_size=max_batch_size, 
                        max_number_of_records=max_number_of_records)
    assert len(batch) == 2