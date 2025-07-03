is_member = True
age = 11

if is_member:#Como member es true entra, si fuera false no entra
    if age >= 15:
        print('Tienes acceso ya que eres miembor y tienes 15 o mas años')
    else:
        print('Eres miembro por no tienes acceso porque no llegas a 15 años')
else:
    print('No eres miembro y NO TIENES ACCESO')