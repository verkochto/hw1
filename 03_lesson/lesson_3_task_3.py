from address import Address
from mailing import Mailing

# создаем два адреса
to_addr = Address("101000", "Москва", "Тверская", "1", "10")
from_addr = Address("190000", "Санкт-Петербург", "Невский проспект", "5", "25")

# отправление
mailing = Mailing(to_addr, from_addr, 250, "ABC123456RU")

print(f"Отправление {mailing.track} из "
      f"{mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, "
      f"{mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. "
      f"Стоимость {mailing.cost} рублей.")
