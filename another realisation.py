def load_script(filename):
    pass


def load_log(filename):
    pass


class Request:
    pass


##main (7 - 58)


class MainUI():
    def __init__(self, store, shop):
        """Initialize the main UI"""
        self.store = store
        self.shop = shop

    def _printer(self):
        """All start prints"""
        print(load_script("greetings"))
        print(load_script("inst"))
        print(load_script("action1"))
        print(load_script("action1/req"))
        print(load_script("action2"))
        print(load_script("action2/req"))
        print(load_script("store/state"))
        print(self.store.get_items())
        print(load_script("shop/state"))
        print(self.shop.get_items())
        print(load_script("for/end"))
        print(load_script("start"))

    def main(self):
        """Main cycle where happen all actions"""
        while True:
            request = self._create_request()
            if not self._is_valid_request(request):
                continue
            if not self.__logic(request):
                continue
            self._end_printer()



    def _create_request(self):
        """Create a request"""
        req = input().lower()
        if req == "завершить":
            print(load_script("end"))
            exit(0)
        print(load_log("check/req"))
        return Request(req)

    def _is_valid_request(self, request):
        """validate request"""
        try:
            if not request.is_incorrect(self.shop, self.store):
                print(f'{load_log("info/req")}\n{request}')
        except ValueError:
            print(load_log('req/error'))
        return True

    def _to_shop(self, request):
        """exchange data from store to shop"""
        self.shop.add(request.product, request.amount)
        self.store.remove(request.product, request.amount)

    def _to_store(self, request):
        """exchange data from shop to store"""
        self.store.add(request.product, request.amount)
        self.shop.remove(request.product, request.amount)

    def _to_another(self):
        """if we don't have some kind of storage"""
        print(load_log('loc/error'))

    def __logic(self, request):
        """check which one function we should call
        :return False - if we don't have some kind of storage'"""
        if request.to == 'магазин':
            self._to_shop(request)
        elif request.to == 'склад':
            self._to_store(request)
        else:
            self._to_another()
            return False

    def _end_printer(self):
        """End printer which print updated data"""
        print(load_script("store/state"))
        print(self.store.get_items())
        print(load_script("shop/state"))
        print(self.shop.get_items())
