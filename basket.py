class Basket:
    def __init__(self):
        self.data = []

    def add(self, product, price):
        self.data.append({'product': product, 'price': price})
        print(f"{product} ({price}) savatga qo'shildi")

    def remove(self, product):
        for item in self.data:
            if item['product'] == product:
                self.data.remove(item)
                print(f"{product} savatdan olib tashlandi")
                return
        print(f"{product} savatda topilmadi")

    def show(self):
        if not self.data:
            print("Savat bo'sh")
        else:
            print("Savat tarkibi")
            for item in self.data:
                print(f"- {item['product']}: {item['price']}")

    def calculating(self):
        total = sum(item['price'] for item in self.data)
        print(f"Umumiy narx: {total}")
        
    def delete_basket(self):
        self.products.clear() 
        return "Savat butunlay bo'shatildi!"

    def cheapest_product(self):
        if not self.data:
            print("Savat bo'sh")
            return
        min_item = min(self.data, key=lambda x: x['price'])
        print(f"Eng arzon mahsulot: {min_item['product']} ({min_item['price']})")


basket = Basket()
basket.add("apple", 2)
basket.add("apple", 1)
basket.show()
basket.calculating()
basket.remove("apple")
basket.show()
