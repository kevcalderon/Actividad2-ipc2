from xml.dom import minidom

#Accedemos al archivo por medio del nombre
doc = minidom.parse("pruebas.xml")

# Por medio del nombre de las etiquetas se busca en el xml.
name = doc.getElementsByTagName("name")[0]
print(name.firstChild.data)

staffs = doc.getElementsByTagName("staff")
#todas las etiquetas llamadas staff las ponemos en un arreglo para luego guardarlas
# y luego imprimirlas.
for staff in staffs:
        sid = staff.getAttribute("id")
        nickname = staff.getElementsByTagName("nickname")[0]
        salary = staff.getElementsByTagName("salary")[0]
        print("id:%s, nickname:%s, salary:%s" %
              (sid, nickname.firstChild.data, salary.firstChild.data))

