# -*- coding: utf-8 -*-
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
MT["('s', '0,@')"] = tupla_transicion('t', '0,@', 'r,o')
MT["('t', '0,@')"] = tupla_transicion('y', '0,@', 'r,o')
MT["('y', '1,@')"] = tupla_transicion('u', '0,x', 'r,r')
MT["('u', '&,@')"] = tupla_transicion('j', '&,@', 'o,l')
MT["('u', '0,@')"] = tupla_transicion('h', '0,@', 'r,o')
MT["('h', '0,@')"] = tupla_transicion('g', '0,@', 'r,o')
MT["('d', '1,@')"] = tupla_transicion('u', '1,x', 'r,r')
MT["('j', '&,x')"] = tupla_transicion('j', '&,x', 'r,l')
MT["('u', '@,@')"] = tupla_transicion('h', '@,@', 's,s')


stri = '01110@'

tm = turing_machine(MT,stri)
result = tm.strart()
print(result)
print(tm.current_state, tm.current_position)