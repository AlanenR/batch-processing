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
