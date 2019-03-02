# two_files.py
d_path = 'dog_breeds.txt'
d_r_path = 'dog_breeds_reversed.txt'

with open(d_path, 'r') as reader, open(d_r_path, 'w') as writer:
    dog_breeds = reader.readlines()
    writer.writelines(reversed(dog_breeds))
