def CDT (usuario, capital, tiempo):
        valoraperder = capital * 0.02
        valortotalperder = capital - valoraperder
        intereses = (capital * 0.03 * tiempo)/12
        valortotalganar =intereses + capital
        if tiempo <= 2:
                capitalfinal = valortotalperder
        else:
                capitalfinal = valortotalganar 
        mensaje = "Para el usuario " + usuario + " La cantidad de dinero a recibir, según el monto inicial " + str(capital) + " para un tiempo de " + str(tiempo) + " meses es: "+ str(capitalfinal)
        return mensaje

mensaje_resultado=CDT ("ER3366",  650000, 2)
print (mensaje_resultado)
