from models import *
print("Inventario de prodcutos")

p1 = ProductoBase(1, "Café Americano", 45.0)
p2 = ProductoBase(2, "Cappuccino Clásico", 65.0)
p3 = ProductoBase(3, "Latte Macchiato", 70.0)
p4 = ProductoBase(4, "Espresso Doble", 55.0)
p5 = ProductoBase(5, "Té Matcha", 80.0)
p6 = ProductoBase(6, "Frappé de Caramelo", 95.0)
p7 = ProductoBase(7, "Croissant de Mantequilla", 40.0)
p8 = ProductoBase(8, "Pastel de Zanahoria", 75.0)
p9 = ProductoBase(9, "Galleta Chispas", 30.0)
p10 = ProductoBase(10, "Bagel de Salmón", 120.0)

print(p1.mostrar_detalle())
print(p2.mostrar_detalle())
print(p3.mostrar_detalle())
print(p4.mostrar_detalle())
print(p5.mostrar_detalle())
print(p6.mostrar_detalle())
print(p7.mostrar_detalle())
print(p8.mostrar_detalle())
print(p9.mostrar_detalle())
print(p10.mostrar_detalle())

print("Registro de Clientes")
c1 = Cliente("c1", "Jorge Santos", "jorge@correo.com", 200)
c2 = Cliente("c2", "Lalolopes21", "lalo@correo.com", 150)
c3 = Cliente("c3", "Ana Ruiz", "ana@correo.com", 50)
c4 = Cliente("c4", "Luis Miguel", "luis@correo.com", 300)
c5 = Cliente("c5", "Marta C", "marta@correo.com", 10)
c6 = Cliente("c6", "David F", "david@correo.com", 80)
c7 = Cliente("c7", "Sofia W", "sofia@correo.com", 120)
c8 = Cliente("c8", "Elena R", "elena@correo.com", 400)
c9 = Cliente("c9", "Carlos M", "carlos@correo.com", 250)
c10 = Cliente("c10", "Valeria G", "valeria@correo.com", 90)

for cliente in [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]:
    print(f"Cliente: {cliente.nombre} - Correo: {cliente.email} - Puntos: {cliente.puntosFidelidad}")



inventario_cafe = Inventario ({
    "Café Americano": 10,
    "Cappuccino Clásico": 0, 
    "Croissant de Mantequilla": 15,
    "Pastel de Zanahoria": 5
})

print("Comenzando el de pedido")
print(f"Cliente: {c1.nombre} (Puntos: {c1.puntosFidelidad})")

productos_intento_1 = [p1, p2, p7]
print(f"Seleccione sus productos (separados por coma): {productos_intento_1[0].nombre}, {productos_intento_1[1].nombre}, {productos_intento_1[2].nombre}")
print("Verificando la disponibilidad  de los productos el inventario...")

pedido_1 = Pedido("101", c1, productos_intento_1, inventario_cafe)
resultado_1 = pedido_1.validarStock()
print(resultado_1)

if "Error" in resultado_1:
    print("Por favor, seleccione productos sí disponibles.")
    
    productos_intento_2 = [p1, p8, p7]
    print(f"Seleccione sus productos: {productos_intento_2[0].nombre}, {productos_intento_2[1].nombre}, {productos_intento_2[2].nombre}")
    
    pedido_final = Pedido("101", c1, productos_intento_2, inventario_cafe)
    print(pedido_final.validarStock())
    
    pedido_final.calcularTotal()
    print(f"Monto base: ${pedido_final.total:.2f}")
    
    print() 
    print(pedido_final.generar_ticket())

empleado_test = Empleado("emp1", "Roberto", "roberto@correo.com", "E01", "BARISTA")

postre_test = Postre(11, "Brownie", 50.0, True, False)

bebida_test = Bebida(12, "Té Chai", 60.0, "Mediano", "CALIENTE", ["Leche de almendra"])


print(f"Empleado instanciado: {empleado_test.nombre} (Rol: {empleado_test.rol})")
print(f"Postre instanciado: {postre_test.nombre} (Vegano: {postre_test.esVegano})")
print(f"Bebida instanciada: {bebida_test.nombre}")
print(bebida_test.agregarExtra("Vainilla"))
print(f"Precio con extras calculados: ${bebida_test.calcularPrecioFinal():.2f}")