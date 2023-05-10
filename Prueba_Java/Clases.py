class Universidad:
    def __init__(self, pnombre, pciudad, prector, pnumero_facultades):
        self.nombre = pnombre
        self.ciudad = pciudad
        self.rector = prector
        self.numero_facultades = pnumero_facultades
    
    #setters
    def set_nombre (self, p):
        self.nombre = p
    def set_ciudad(self, p):
        self.ciudad = p
    def set_rector(self, p):
        self.rector = p
    def set_numero_facultades(self, p):
        self.numero_facultades = p
    #getters
    def get_nombre(self):
        return self.nombre
    def get_ciudad(self):
        return self.ciudad
    def get_rector(self):
        return self.rector
    def get_numero_facultades(self):
        return self.numero_facultades
    #tostring
    def __str__(self):
        return "Universidad:  %s\n, Ciudad: %s\n, Rector: %s\n, Numero de Facultades: %d\n" \
        % (self.nombre, self.ciudad, self.rector, self.numero_facultades)

class Carrera:
    def __init__(self, pnombre, pfacultad, ptitulo, psemestres):
        self.nombre = pnombre
        self.facultad = pfacultad
        self.titulo = ptitulo
        self.semestres = psemestres

    #setters
    def set_nombre (self, p):
        self.nombre = p
    def set_facultad(self, p):
        self.facultad = p
    def set_titulo(self, p):
        self.titulo = p
    def set_semestres(self, p):
        self.semestres = p
    #getters
    def get_nombre (self):
        return self.nombre
    def get_facultad(self):
        return self.facultad
    def get_titulo(self):
        return self.titulo
    def get_semestres(self):
        return self.semestres
    #tostring
    def __str__(self):
        return "Carrera: %s\n, Facultad: %s\n, Titulo que otorga: %s\n, Numero de semestres: %d\n" %(self.nombre, self.facultad, self.titulo, self.semestres)
    