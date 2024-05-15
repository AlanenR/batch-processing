from src.batch_processor import batch_processor

def main():
    records = ['a' * 1024, 'b' * (512 * 1024), 'c' * (1 * 1024 * 1024), 'd' * (1 * 1024 * 1024 + 1)]

    batches = batch_processor(records)

    for i, batch in enumerate(batches):
        print(f"Batch {i + 1} with {len(batch)} records")

if __name__ == "__main__":
    main()