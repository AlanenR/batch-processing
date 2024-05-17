import pytest
from src.batch_processor import batch_processor
from tests.test_data import test_data
from src.config import MAX_RECORD_SIZE, MAX_BATCH_SIZE, MAX_NUMBER_OF_RECORDS
from src.utils import get_size

def test_valid_batch_creation():
    '''
    Checks that batch is created when all records are valid
    '''
    records = test_data['valid_batch']
    batches = batch_processor(records)
    assert len(batches) == 1
    assert len(batches[0]) == 500

def test_discard_oversized_records():
    '''
    Checks that oversized records get discarded
    '''
    records = [test_data['oversized_record']]
    batches = batch_processor(records)
    assert len(batches) == 0

def test_max_number_of_records_per_batch():
    '''
    Checks that no batch contains more records than MAX_NUMBER_OF_RECORDS
    '''
    records = [test_data['small_record']] * (MAX_NUMBER_OF_RECORDS + 100)
    batches = batch_processor(records)
    for batch in batches:
        assert len(batch) <= MAX_NUMBER_OF_RECORDS


def test_boundary_conditions():
    '''
    Checks that:
    - record exactly at the size limit is included
    - record just below at the size limit is included
    - record just above at the size limit is excluded
    '''
    records = [
        test_data['exactly_one_mb_record'],
        test_data['just_below_one_mb_record'],
        test_data['just_above_one_mb_record']
    ]
    batches = batch_processor(records)
    expected_count = 2
    total_records_processed = 0
    for batch in batches:
        number_of_records_in_batch = len(batch)
        total_records_processed += number_of_records_in_batch
    assert total_records_processed == expected_count

def test_batch_size_limitation():
    records = test_data['mixed_batch'] # Contains 3 valid and one oversized records
    batches = batch_processor(records)
    total_records_processed = 0
    for batch in batches:
        total_records_processed += len(batch)
    assert total_records_processed == len(records)-1 # subtract oversized record
    for batch in batches:
        assert len(batch) <= 500, f"A batch contains {len(batch)} records, exceeding the 500 record limit"
 
def test_batch_count_limitation():
    '''
    checks that records in batch don't exceed the MAX_NUMBER_OF_RECORDS limit.
    '''
    records = [test_data['small_record']] * 501
    batches = batch_processor(records)
    assert len(batches) > 1
    all_batches_within_limit = True
    for batch in batches:
        if len(batch) > MAX_NUMBER_OF_RECORDS:
            all_batches_within_limit = False
            break
    assert all_batches_within_limit

def test_stress_with_many_small_records():
    '''
    Stress testing to ensure the function can handle a large number of small records.
    '''
    records = test_data['stress_test_records']
    batches = batch_processor(records)
    total_records_processed = 0
    for batch in batches:
        total_records_processed += len(batch)
    assert total_records_processed == len(records), f"Expected {len(records)} records processed, got {total_records_processed}"
    for batch in batches:
        assert len(batch) <= MAX_NUMBER_OF_RECORDS, f"A batch contains {len(batch)} records, exceeding the {MAX_NUMBER_OF_RECORDS} record limit"
    for batch in batches:
        batch_size = 0
        for record in batch:
            batch_size += get_size(record)
        assert batch_size <= MAX_BATCH_SIZE, f"A batch size is {batch_size} bytes, exceeding the {MAX_BATCH_SIZE} bytes limit"



