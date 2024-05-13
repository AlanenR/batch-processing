from config import MAX_RECORD_SIZE, MAX_BATCH_SIZE, MAX_NUMBER_OF_RECORDS

def get_size(record):
    return len(record.encode('utf-8'))


def process_batch(records, 
                  max_record_size=MAX_RECORD_SIZE, 
                  max_batch_size=MAX_BATCH_SIZE, 
                  max_number_of_records=MAX_NUMBER_OF_RECORDS
                  ):
    batches = []
    batch = []
    current_batch_size = 0

    for record in records:
        if type(record) != str:
            continue

        record_size = get_size(record)

        if record_size > max_record_size:
            continue

        if (current_batch_size + record_size > max_batch_size 
            or len(batch) == max_number_of_records):
            batches.append(batch)
            batch = []
            current_batch_size = 0

        current_batch_size += record_size
        batch.append(record)

    if batch:
        batches.append(batch)
    
    return batches
