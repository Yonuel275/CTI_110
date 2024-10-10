# In-class example on dictionaries

# Create a dictionary
rose_bush = {"rose_color":"purple", "price":32.98, "max_height":60, "is_it_perennial":True}

# Get value, given the key
print(f"The rose bush perennail price is: ${rose_bush['price']:.2f}")
print(f"The rose bush perennail price is: ${rose_bush['rose_color']}")
print(f"The rose bush perennail price is: ${rose_bush['max_height']:.2f}")
print(f"Is the rose bush perennail? {rose_bush['is_it_perennial']}")
