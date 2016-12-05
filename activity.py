# Copyright 2009 Simon Schampijer
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

from gi.repository import Gtk
import logging

from gettext import gettext as _

from sugar3.activity import activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import ActivityButton
from sugar3.activity.widgets import TitleEntry
from sugar3.activity.widgets import StopButton
from sugar3.activity.widgets import ShareButton
from sugar3.activity.widgets import DescriptionItem
from sugar3.graphics import style
import random

class CadradoMagicoActivity(activity.Activity):

    def __init__(self, handle):
        activity.Activity.__init__(self, handle)

        # we do not have collaboration features
        # make the share option insensitive
        self.max_participants = 1

        # toolbar with the new toolbar redesign
        toolbar_box = ToolbarBox()

        activity_button = ActivityButton(self)
        toolbar_box.toolbar.insert(activity_button, 0)
        activity_button.show()

        title_entry = TitleEntry(self)
        toolbar_box.toolbar.insert(title_entry, -1)
        title_entry.show()

        description_item = DescriptionItem(self)
        toolbar_box.toolbar.insert(description_item, -1)
        description_item.show()

        share_button = ShareButton(self)
        toolbar_box.toolbar.insert(share_button, -1)
        share_button.show()
        
        separator = Gtk.SeparatorToolItem()
        separator.props.draw = False
        separator.set_expand(True)
        toolbar_box.toolbar.insert(separator, -1)
        separator.show()

        stop_button = StopButton(self)
        toolbar_box.toolbar.insert(stop_button, -1)
        stop_button.show()

        self.set_toolbar_box(toolbar_box)
        toolbar_box.show()

        # label with the text, make the string translatable
        event_box = Gtk.EventBox()
        event_box.modify_bg(Gtk.StateType.NORMAL, 
                            style.Color('#FFFFFF').get_gdk_color())
        juego = Gtk.VBox()
        label = Gtk.Label('Cuadro Magico')
        nivel = Gtk.Label('Nivel 1: \n'
                        'Haz que la primera columna sume 15!!!')

        hbox1 = Gtk.HButtonBox()
        hbox1.set_layout(Gtk.ButtonBoxStyle.CENTER)
        hbox2 = Gtk.HButtonBox()
        hbox2.set_layout(Gtk.ButtonBoxStyle.CENTER)
        hbox3 = Gtk.HButtonBox()
        hbox3.set_layout(Gtk.ButtonBoxStyle.CENTER)
        hbox4 = Gtk.HButtonBox()
        hbox4.set_layout(Gtk.ButtonBoxStyle.CENTER)

        event_box = Gtk.EventBox()

        self.botones = []
        while len(self.botones) < 9:
            boton = Gtk.Button()
            boton.set_size_request(150, 150)
            boton.modify_bg(Gtk.StateType.NORMAL, style.Color("#1CCD16").get_gdk_color())
            self.botones.append(boton)

        felicitaciones = Gtk.Label('Excelente lograste el nivel 1 prueba resolviendo el nivel 2!!!')

        boton_id = 0
        for boton in self.botones:
            boton.connect("clicked", self.cambiar, nivel, felicitaciones)
            boton_id += 1

        self.click=0
        self.x3=0
        self.nivel=1
        self.fila1=0
        self.fila2=0
        self.fila3=0
        self.columna1=0
        self.columna2=0
        self.columna3=0
        self.diagonal1=0
        self.diagonal2=0
            
        self.cargar_botones()

        self.set_canvas(event_box)
        event_box.add(juego)

        hbox1.add(self.botones[0])
        hbox1.add(self.botones[1])
        hbox1.add(self.botones[2])

        hbox2.add(self.botones[3])
        hbox2.add(self.botones[4])
        hbox2.add(self.botones[5])

        hbox3.add(self.botones[6])
        hbox3.add(self.botones[7])
        hbox3.add(self.botones[8])

        juego.add(label)
        juego.add(nivel)
        juego.add(hbox1)
        juego.add(hbox2)
        juego.add(hbox3)
        juego.add(hbox4)
        juego.add(felicitaciones)

        #Visibilidad de ventanas
        event_box.show_all()

    def cargar_botones(self):
        numeros = []
        boton_id = 0
        while len(numeros) < 9:
            x = random.randint(1,9)
            if x in numeros:
                continue
            numeros.append(x)
            self.botones[boton_id].set_label(str(x))
            boton_id += 1

    def cambiar(self, widget, nivel=None, felicitaciones=None):
        self.click+=1
        if self.click==1:
	    self.first_press = widget
            widget.modify_bg(Gtk.StateType.NORMAL, style.Color("#F20000").get_gdk_color())
        else:
            temp_val=widget.get_label()
            widget.set_label(self.first_press.get_label())
            self.first_press.set_label(str(temp_val))
            self.first_press.modify_bg(Gtk.StateType.NORMAL, style.Color("#1CCD16").get_gdk_color())

            self.click=0
            self.fila1=int(self.botones[0].get_label()) + int(self.botones[1].get_label()) + int(self.botones[2].get_label())
            self.fila2=int(self.botones[3].get_label()) + int(self.botones[4].get_label()) + int(self.botones[5].get_label())
            self.fila3=int(self.botones[6].get_label()) + int(self.botones[7].get_label()) + int(self.botones[8].get_label())
            self.columna1=int(self.botones[0].get_label()) + int(self.botones[3].get_label()) + int(self.botones[6].get_label())
            self.columna2=int(self.botones[1].get_label()) + int(self.botones[4].get_label()) + int(self.botones[7].get_label())
            self.columna3=int(self.botones[2].get_label()) + int(self.botones[5].get_label()) + int(self.botones[8].get_label())
            self.diagonal1=int(self.botones[0].get_label()) + int(self.botones[4].get_label()) + int(self.botones[8].get_label())
            self.diagonal2=int(self.botones[6].get_label()) + int(self.botones[4].get_label()) + int(self.botones[2].get_label())
    
        if self.nivel==1 and self.columna1==15:
            nivel.set_text('Nivel 2: \n'
                'Haz que las dos primeras columnas sumen 15 cada una!!!')
            felicitaciones.set_visible(True)
            self.nivel+=1
            self.click=0
            self.cargar_botones()
        elif self.nivel==2 and self.columna1==15 and self.columna2==15:
            nivel.set_text('Nivel 3: \n'
                'Haz que las tres columnas sumen 15 cada una!!!')
            felicitaciones.set_text('Excelente lograste el nivel 2 prueba resolviendo el nivel 3!!!')
            self.nivel+=1
            self.click=0
            self.cargar_botones()
        elif self.nivel==3 and self.columna1==15 and self.columna2==15 and self.columna3==15:
            nivel.set_text('Nivel 4: \n'
                'Haz que las dos primeras columnas y la primera fila sumen 15 cada una!!!')
            felicitaciones.set_text('Excelente lograste el nivel 3 prueba resolviendo el nivel 4!!!')
            self.nivel+=1
            self.click=0
            self.cargar_botones()
        elif self.nivel==4 and self.columna1==15 and self.columna2 == 15 and self.fila1 == 15: 
            nivel.set_text('Nivel 5: \n'
                'Haz que las tres columnas y las tres filas sumen 15 cada una!!!')
            felicitaciones.set_text('Excelente lograste el nivel 4 prueba resolviendo el nivel 5!!!')
            self.nivel+=1
            self.click=0
            self.cargar_botones()
        elif self.nivel==5 and self.columna1==15 and self.columna2 == 15 and self.columna3 == 15 and self.fila1 == 15 and self.fila2 == 15 and self.fila3 == 15:
            nivel.set_text('Nivel ultimo: \n'
                'Haz que las tres columnas, las tres filas y las ambas diagonales sumen 15 cada una!!!')
            felicitaciones.set_text('Excelente lograste el nivel 4 prueba resolviendo el nivel 5!!!')
            self.nivel+=1
            self.click=0
            self.cargar_botones()
        elif self.nivel==6 and self.columna1 == 15 and self.columna2==15 and self.columna3==15 and self.fila1 == 15 and self.fila2 == 15 and self.fila3 == 15 and self.diagonal1 == 15 and diagonal2 == 15:
            felicitaciones.set_markup('<span style="color: red"><b>Excelente lograste el nivel ultimo!</b></span>')
