class Persona:
    def __init__(self, idPersona, nombre, email):
        self.idPersona = idPersona
        self.nombre = nombre
        self.email = email

    def login(self):
        return f" el usuario {self.nombre} ha iniciado sesión."

    def actualizarPerfil(self):
        return ' el perfil se ha actualizado con éxito.'

class Cliente(Persona):
    def __init__(self, idPersona, nombre, email, puntosFidelidad):
        super().__init__(idPersona, nombre, email)
        self.puntosFidelidad = puntosFidelidad
        self.historialPedidos = []

    def realizarPedido(self, pedido):
        self.historialPedidos.append(pedido)
        return "Pedido registrado en el historial."

    def consultarHistorial(self):
        return self.historialPedidos

    def canjearPuntos(self):
        return "los  puntos fueron canjeados correctamente."

class Empleado(Persona):
    def __init__(self, idPersona, nombre, email, idEmpleado, rol):
        super().__init__(idPersona, nombre, email)
        self.idEmpleado = idEmpleado
        self.rol = rol

    def cambiarEstadoPedido(self):
        return "El estado del  pedido ha sido actualizado."

    def actualizarInventario(self):
        return "El inventario fue revisado y actualizado."

class ProductoBase:
    def __init__(self, idProducto, nombre, precioBase):
        self.idProducto = idProducto
        self.nombre = nombre
        self.precioBase = precioBase

    def mostrar_detalle(self):
        return f"ID del producto: {self.idProducto}  {self.nombre} (${self.precioBase})"

class Bebida(ProductoBase):
    def __init__(self, idProducto, nombre, precioBase, tamaño, temperatura, modificadores):
        super().__init__(idProducto, nombre, precioBase)
        self.tamaño = tamaño
        self.temperatura = temperatura
        self.modificadores = modificadores

    def agregarExtra(self, extra):
        self.modificadores.append(extra)
        return f"Extra de {extra} agregado a la bebida."

    def calcularPrecioFinal(self):
        costo_extras = len(self.modificadores) * 5.0
        return self.precioBase + costo_extras

class Postre(ProductoBase):
    def __init__(self, idProducto, nombre, precioBase, esVegano, sinGluten):
        super().__init__(idProducto, nombre, precioBase)
        self.esVegano = esVegano
        self.sinGluten = sinGluten

class Inventario:
    def __init__(self, ingredientes):
        self.ingredientes = ingredientes

    def reducirStock(self, item, cantidad):
        if self.ingredientes.get(item, 0) >= cantidad:
            self.ingredientes[item] -= cantidad
            return True
        return False
    
    def notificarFaltante(self):
        return "Alerta: Stock insuficiente para algunos ingredientes."

class Pedido:
    def __init__(self, idPedido, cliente, productos, inventario):
        self.idPedido = idPedido
        self.cliente = cliente
        self.productos = productos
        self.inventario = inventario
        self.estado="pendiente"
        self.total = 0.0

    def calcularTotal(self):
        total_temp = 0.0
        for i in range(len(self.productos)):
            if isinstance(self.productos[i], Bebida):
                total_temp += self.productos[i].calcularPrecioFinal()
            else:
                total_temp += self.productos[i].precioBase
        self.total = total_temp
        return self.total

    def validarStock(self):
        agotados = []
        for i in range(len(self.productos)):
            if not self.inventario.reducirStock(self.productos[i].nombre, 1):
                agotados.append(self.productos[i].nombre)
        
        if len(agotados) > 0:
            return f"Error: El producto {agotados[0]} ya está agotadop"
        
        self.estado = "en proceso"
        
        prods_str = ""
        for i in range(len(self.productos)):
            prods_str += self.productos[i].nombre
            if i < len(self.productos) - 1:
                prods_str += ", "
                
        return f"Productos {prods_str} confirmados con éxito."

    def generar_ticket(self):
        self.calcularTotal()
        
        prods_str = ""
        for i in range(len(self.productos)):
            prods_str += self.productos[i].nombre
            if i < len(self.productos) - 1:
                prods_str += ", "

        return f"Resumen del pedido #{self.idPedido} hecho por el Cliente: {self.cliente.nombre} que contiene los productos: [{prods_str}] y da un total: ${self.total:.2f}  con estado: {self.estado}. Ticket generado."