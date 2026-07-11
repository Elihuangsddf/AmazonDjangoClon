class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito = carrito

    def agregar(self, producto):
        app_label = producto._meta.app_label
        product_id = str(producto.id)
        key = f"{app_label}_{product_id}"

        if key not in self.carrito:
            self.carrito[key] = {
                "productoId": producto.id,
                "app_name": app_label,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "precioUnitario": str(producto.precio),
                "cantidad": 1,
                "imagen": producto.imagen.url if producto.imagen else ""
            }
        else:
            self.carrito[key]["cantidad"] += 1
            precioUnitario = float(self.carrito[key]["precioUnitario"])
            self.carrito[key]["precio"] = str(float(self.carrito[key]["precio"]) + precioUnitario)
            
        self.guardarCarrito()

    def guardarCarrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        app_label = producto._meta.app_label
        product_id = str(producto.id)
        key = f"{app_label}_{product_id}"
        
        if key in self.carrito:
            del self.carrito[key]
            self.guardarCarrito()
    
    def restarProducto(self, producto):
        app_label = producto._meta.app_label
        product_id = str(producto.id)
        key = f"{app_label}_{product_id}"

        if key in self.carrito:
            self.carrito[key]["cantidad"] -= 1
            precioUnitario = float(self.carrito[key]["precioUnitario"])
            self.carrito[key]["precio"] = str(float(self.carrito[key]["precio"]) - precioUnitario)

            if self.carrito[key]["cantidad"] < 1:
                self.eliminar(producto)
            else:
                self.guardarCarrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True