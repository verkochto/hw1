from smartphone import Smartphone

#список каталог
catalog = []

# добавляем 5 объектов класса Smartphone
catalog.append(Smartphone("Apple", "iPhone 14", "+79161234567"))
catalog.append(Smartphone("Samsung", "Galaxy S22", "+79876543210"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 11", "+79001234567"))
catalog.append(Smartphone("Google", "Pixel 7", "+79215678901"))
catalog.append(Smartphone("OnePlus", "9 Pro", "+79998887766"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")
