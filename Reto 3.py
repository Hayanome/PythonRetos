ventas=([
 (2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
 (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
 (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'), 
 (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
 (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')])

def AutoPartes (ventas:list)->dict:
    listadic={}
    for venta in ventas:
        if venta[0] not in listadic.keys():
            listadic[venta[0]]=list()
        listadic[venta[0]].append([venta[1],venta[2],venta[3],venta[4],venta[5],venta[6],venta[7]])    
    return listadic

def consultaRegistro (ventas,idproducto):
    if idproducto not in ventas:
        mensaje="No hay registro de venta de ese producto"
        print(mensaje)
    else:
        for venta in ventas[idproducto]:
            idproducto1=idproducto
            dProducto=venta[0]
            pnProducto=venta[1]
            cvProducto=venta[2]
            sProducto=venta[3]
            nComprador=venta[4]
            cComprador=venta[5]
            fVenta=venta[6]
            print('Producto consultado :', idproducto1, ' Descripción '\
                    , dProducto, ' #Parte ', pnProducto, ' Cantidad vendida '\
                    , cvProducto, ' Stock ', sProducto, ' Comprador', nComprador,\
                    ' Documento ', cComprador, ' Fecha Venta ', fVenta)
    


consultaRegistro(AutoPartes([
    (2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
    (2010,'bujía', '     MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
    (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),    
    (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
    (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')]), 2010)