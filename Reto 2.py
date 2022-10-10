def cliente (information):
    edad=information['edad']
    id=information['id_cliente']
    nombre=information['nombre']
    primer_ingreso=information['primer_ingreso']
    if edad>18:
        atraccion="X-Treme"
        precioatraccion=20000
        apto=True
    if edad>=15 and edad<=18:
        atraccion="Carroschocones"
        precioatraccion=5000
        apto=True
    if edad>=7 and edad<15:
        atraccion="Sillas voladoras"
        precioatraccion=10000
        apto=True
    if edad<7:
        atraccion="N/A"
        precioatraccion:"N/A"
        apto=False
    if atraccion=="X-Treme" and primer_ingreso==True:
        precioatraccion=20000*0.95
    if atraccion=="Carroschocones" and primer_ingreso==True:
        precioatraccion=5000*0.92
    if atraccion=="Sillas voladoras" and primer_ingreso==True:
        precioatraccion=10000*0.95
    if atraccion=="N/A" and primer_ingreso==True:
        precioatraccion="N/A"
    dic2={
        "nombre":nombre,
        "edad":edad,
        "atraccion":atraccion,
        "apto":apto,    
        "primer_ingreso" : primer_ingreso,
        "total_boleta":precioatraccion,        
    }
    return dic2