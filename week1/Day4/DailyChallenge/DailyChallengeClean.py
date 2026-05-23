



import math
class Pagination:

    def __init__(self, items=None, page_size=10):

        if items is None:
            self.items = []
        else:
            self.items = items

        self.page_size = page_size
        self.current_idx = 0

        self.number_of_pages = math.ceil(len(self.items) / self.page_size) if self.page_size > 0 else 0
#
    def get_visible_items(self):

        start = self.current_idx * self.page_size
        stop = start + self.page_size

        return self.items[start:stop]

    def go_to_page(self, page_num):
        
        if page_num < 1 or page_num > self.number_of_pages:
            raise ValueError("page number out of range")
        self.current_idx = page_num - 1
       

    def first_page(self):

        self.current_idx = 0
        return self

    def last_page(self):
        self.current_idx = self.number_of_pages - 1
        return self 


    def next_page(self):
        if self.current_idx < self.number_of_pages - 1:
            self.current_idx += 1

        return self

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1

        return self
    def __str__(self):
        datas_to_show=self.get_visible_items()
        return "\n".join(datas_to_show)



alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())
p.next_page()
print(p.get_visible_items())

p.last_page()
print(p.get_visible_items())

p.go_to_page(10)
print(p.current_idx + 1)


p.go_to_page(0)
