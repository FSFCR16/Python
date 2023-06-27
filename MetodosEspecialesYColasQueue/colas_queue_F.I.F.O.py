import queue

"""#primer tipo de cola F.I.F.O"""

miCola1=queue.Queue()

#metodo put

miCola1.put("Madrid")
miCola1.put("Bogota")
miCola1.put("Medellin")

#metodo get, tipo F.I.F.O sale primero madrid

print(miCola1.get())

#todos los elementos de la cola

print("A continuacion se imprimen todos los elementos restantes en la cola")

for elemnto in miCola1.queue:

    print(elemnto)



#Metodo full

print(miCola1.full())


#metodo empty

print(miCola1.empty())


print("----------------------------------------")

"""segundo tipo de cola L.I.F.O"""

miCola2=queue.LifoQueue()

#metodo put

miCola2.put("Madrid")
miCola2.put("Bogota")
miCola2.put("Medellin")

#metodo get, tipo F.I.F.O sale primero madrid

print(miCola2.get())

#todos los elementos de la cola

print("A continuacion se imprimen todos los elementos restantes en la cola")

for elemnto in miCola2.queue:

    print(elemnto)


#Metodo full

print(miCola2.full())

#metodo empty

print(miCola2.empty())


print("----------------------------------------")


"""segundo tipo de cola PRIORITY"""

miCola3=queue.PriorityQueue()

#metodo put

miCola3.put((3,"Madrid"))
miCola3.put((2,"Bogota"))
miCola3.put((1,"Medellin"))

#metodo get, tipo F.I.F.O sale primero madrid

print(miCola3.get())

#todos los elementos de la cola

print("A continuacion se imprimen todos los elementos restantes en la cola")

for elemnto in miCola3.queue:

    print(elemnto)

#Metodo full

print(miCola3.full())


#metodo empty

print(miCola3.empty())


print("------------------------------------")

for cur_queue in (miCola1,miCola2,miCola3):
    print("")
    print(cur_queue)
    while True:
        try:
            item = cur_queue.get_nowait()
        except queue.Empty:
            # Ya se han retornado todos los ítems
            break
        else:
            print(item)
