#a^5n| n>0



class tupla_transicion:
    def __init__(self, _estado, _caracter , _direccion):
        self.estado = _estado
        self.caracter = _caracter
        self.direccion = _direccion

class turing_machine:
    def __init__(self, transicion, string_cinta):
        if isinstance(transicion, dict):
            self.tabla_transicion = transicion
        self.cinta = list(string_cinta)
        self.current_state = 's'
        self.current_position = 0
    def strart(self):
        result = False
        if self.current_state == 's':
            while (self.current_state!= 'Alto' and self.current_state!= 'Si' and self.current_state!= 'No' and self.current_state !='Error'):
                car = self.cinta[self.current_position]
                tupla = "('" + self.current_state + "', '" + car + "')"
                if  tupla in self.tabla_transicion:
                    accion = self.tabla_transicion[tupla]
                    if isinstance(accion, tupla_transicion):
                        self.current_state = accion.estado
                        print(self.cinta[self.current_position], accion.caracter, accion.direccion, accion.estado)
                        self.cinta[self.current_position] = accion.caracter
                        if accion.direccion == 'l':
                            self.current_position = self.current_position - 1
                        else:
                            if accion.direccion == 'r':
                                self.current_position = self.current_position + 1
                            else:
                                if accion.direccion != 'o':
                                    #salida si hay error
                                    self.current_state = 'Error'

        if self.current_state!= 'Alto' or self.current_state!= 'Si' or  self.current_state!= 'No':
            result = True
        return result



MT = dict()
MT["('s', '0,@')"] = tupla_transicion('t', '0,0', 'r,r')
MT["('t', '0,@')"] = tupla_transicion('y', '0,0', 'r,r')
MT["('y', '0,@')"] = tupla_transicion('i', '0,0', 'r,r')
MT["('p', '0,@')"] = tupla_transicion('L', '0,0', 'r,r')
MT["('L', '0,@')"] = tupla_transicion('k', '0,0', 'r,r')
MT["('k', '@,@')"] = tupla_transicion('f', '@,@', 'o,o')
MT["('k', '0,@')"] = tupla_transicion('j', '0,@', 'o,l')
MT["('j', '0,0')"] = tupla_transicion('j', '0,0', 'r,l')
MT["('j', '@,@')"] = tupla_transicion('f', '@,@', 'o,o')
MT["('j', '0,@')"] = tupla_transicion('d', '0,@', 'o,r')
MT["('d', '0,0')"] = tupla_transicion('d', '0,0', 'r,r')
MT["('d', '@,@')"] = tupla_transicion('f', '@,@', 'o,o')
MT["('d', '0,@')"] = tupla_transicion('j', '0,@', 'o,l')
stri = '0000000000@'

tm = turing_machine(MT,stri)
result = tm.strart()
print(result)
print(tm.current_state, tm.current_position)
