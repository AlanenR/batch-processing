from config import MAX_RECORD_SIZE, MAX_BATCH_SIZE, MAX_NUMBER_OF_RECORDS
from utils import validate_record, add_record_to_batch

def batch_processor(records, 
                  max_record_size=MAX_RECORD_SIZE, 
                  max_batch_size=MAX_BATCH_SIZE, 
                  max_number_of_records=MAX_NUMBER_OF_RECORDS):
    batch = [] 
    batches = []
    current_batch_size = 0
    for record in records: 
        if validate_record(record, max_record_size):
            batch, batches, current_batch_size = add_record_to_batch(
                record, batch, batches, current_batch_size, max_batch_size, max_number_of_records)
    if batch:
        batches.append(batch)
    return batches