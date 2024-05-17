def get_size(record):
    '''
    Returns the size of the record in bytes.
    '''
    return len(record.encode('utf-8'))

def validate_record(record, max_record_size):
    '''
    Checks if the record is a string,
    and its size does not exceed the maximum allowed size.
    '''
    if type(record) != str:
        return False
    if get_size(record) > max_record_size:
        return False
    return True


def add_record_to_batch(record, 
                        batch, 
                        batches, 
                        current_batch_size, 
                        max_batch_size, 
                        max_number_of_records):
    '''
    Adds a record to the current batch if it doesn't exceed size or count limits, 
    else creates a new batch.
    '''
    record_size = get_size(record)
    if (current_batch_size + record_size > max_batch_size) or (len(batch) >= max_number_of_records):
        batches.append(batch)
        batch = []
        current_batch_size = 0
    batch.append(record)
    current_batch_size += record_size
    return batch, batches, current_batch_size
