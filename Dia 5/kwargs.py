def suma(num1, num2, *args, **kwargs):
   print(f"El primer valor es {num1}")
   print(f"El primer valor es {num2}")

   for num in args:
       print(f"args = {num}")


   for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")



args = [100,200,35,725,]
kwargs = {'x': 'uno', 'y': 'dos', 'z' : 'tres'}
suma(15, 27, *args, **kwargs )