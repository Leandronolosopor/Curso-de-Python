from collections import Counter
#counter cuenta

def count_sales(products: list[str]) -> Counter:
    # Usa Counter para contar cuántos productos de cada tipo se han vendido
    return Counter(products)#le damos como informacion los productos y los cuenta.


sales = ["laptop", "smartphone", "smartphone", "laptop", "tablet"]
result = count_sales(sales)
print(result)  # Output: Counter({'laptop': 2, 'smartphone': 2, 'tablet': 1})
#y da contado la cantidad de laptops porque counter hacer eso