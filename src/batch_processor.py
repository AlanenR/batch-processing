from config import MAX_RECORD_SIZE, MAX_BATCH_SIZE, MAX_NUMBER_OF_RECORDS

def get_size(record):
    return len(record.encode('utf-8'))

def validate_record(record, max_record_size):
    if type(record) != str:
        return False
    if get_size(record) > max_record_size:
        return False
    return True


def add_record_to_batch(record, batch, batches, current_batch_size, max_batch_size, max_number_of_records):
    record_size = get_size(record)
    if (current_batch_size + record_size > max_batch_size) or (len(batch) >= max_number_of_records):
        batches.append(batch)
        batch = []
        current_batch_size = 0
    batch.append(record)
    current_batch_size += record_size
    return batch, batches, current_batch_size


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
