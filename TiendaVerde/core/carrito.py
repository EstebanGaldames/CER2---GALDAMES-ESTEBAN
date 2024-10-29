class Carrito:
    def __init__(self, request):
        #Guardo la solicitud y sesión del usuario.
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        #Si el carrito no existe, lo creo.
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito
    
    def agregar(self, Product):
        id = str(Product.id)
        #Lo agrego al carrito.
        if id not in self.carrito.keys():
            #Agrego los valores a los campos.
            self.carrito[id] = {
                
                "producto_id" : Product.id,
                "nombre"      : Product.nombre,
                "acumulado"   : Product.precio,
                "cantidad"    : 1
            }
        else:
            #Si el producto ya está en el carrito le sumo la cantidad y el precio.
            self.carrito[id]["cantidad"]  += 1
            self.carrito[id]["acumulado"] += Product.precio 
        #Guardo el carrito.    
        self.guardar_carrito()

    def guardar_carrito(self):
        #Guardo el carrito actual.
        self.session["carrito"] = self.carrito
        self.session.modified   = True

    def eliminar(self, Product):
        id = str(Product.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    #Funcion que le resta la cantidad de un producto en el carrito.
    def restar(self, Product):
        id = str(Product.id)
        #Busco el producto en el carrito. 
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"]  -= 1
            self.carrito[id]["acumulado"] -= Product.precio
            if self.carrito[id]["cantidad"] <= 0: self.eliminar(Product)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified   = True             
