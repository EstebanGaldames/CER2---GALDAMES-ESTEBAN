class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito
    
    def agregar(self, Product):
        id = str(Product.id)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                
                "producto_id" : Product.id,
                "nombre"      : Product.nombre,
                "acumulado"   : Product.precio,
                "cantidad"    : 1
            }
        else:
            self.carrito[id]["cantidad"]  += 1
            self.carrito[id]["acumulado"] += Product.precio 
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified   = True

    def eliminar(self, Product):
        id = str(Product.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, Product):
        id = str(Product.id) 
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"]  -= 1
            self.carrito[id]["acumulado"] -= Product.precio
            if self.carrito[id]["cantidad"] <= 0: self.eliminar(Product)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified   = True             
