# Different size records
small_record = 'a' * 1024  # 1 KB
medium_record = 'b' * (512 * 1024)  # 512 KB
large_record = 'c' * (1 * 1024 * 1024)  # 1 MB
oversized_record = 'd' * (1 * 1024 * 1024 + 1)  # Just above 1 MB

# Define batches
valid_batch = [small_record for _ in range(500)]
oversized_batch = [oversized_record for _ in range(10)]
mixed_batch = [small_record, medium_record, large_record, oversized_record]

# Boundary conditions
exactly_one_mb_record = 'e' * (1 * 1024 * 1024)
just_below_one_mb_record = 'f' * (1 * 1024 * 1024 - 1)
just_above_one_mb_record = 'g' * (1 * 1024 * 1024 + 1)

# Stress test records
stress_test_records = ['i' * 100] * 5000  # 5000 really small records

# Export all as a dictionary or pick a variable
test_data = {
    'small_record': small_record,
    'medium_record': medium_record,
    'large_record': large_record,
    'oversized_record': oversized_record,
    'valid_batch': valid_batch,
    'oversized_batch': oversized_batch,
    'mixed_batch': mixed_batch,
    'exactly_one_mb_record': exactly_one_mb_record,
    'just_below_one_mb_record': just_below_one_mb_record,
    'just_above_one_mb_record': just_above_one_mb_record,
    'stress_test_records': stress_test_records
}
