#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
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

import random
import logging

from gettext import gettext as _

from gi.repository import Gtk
from gi.repository import Gio
from gi.repository import Pango

from sugar3.activity import activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import ActivityButton
from sugar3.activity.widgets import TitleEntry
from sugar3.activity.widgets import StopButton
from sugar3.activity.widgets import ShareButton
from sugar3.activity.widgets import DescriptionItem
from sugar3.activity.widgets import ActivityToolbarButton
from sugar3.graphics import style


COLOR_NORMAL = "#1CCD16"
COLOR_SELECCIONADO = "#F20000"

if "org.sugarlabs.user" in Gio.Settings.list_schemas():
    settings = Gio.Settings("org.sugarlabs.user")
    colores = settings.get_string("color")
    separados = colores.split(",")

    if len(separados) == 2:
        COLOR_NORMAL = separados[0]
        COLOR_SELECCIONADO = separados[1]


class CadradoMagicoActivity(activity.Activity):

    def __init__(self, handle):
        activity.Activity.__init__(self, handle)

        # we do not have collaboration features
        # make the share option insensitive
        self.max_participants = 1
        self.crear_toolbars()

        # label with the text, make the string translatable
        event_box = Gtk.EventBox()
        event_box.modify_bg(Gtk.StateType.NORMAL, 
                            style.Color('#FFFFFF').get_gdk_color())
        juego = Gtk.VBox()
        label = Gtk.Label('Cuadro Mágico')
        label.modify_font(Pango.FontDescription("22"))

        nivel = Gtk.Label('Nivel 1: \n'
                        'Haz que la primera columna sume 15!!!')
        nivel.modify_font(Pango.FontDescription("20"))

        event_box = Gtk.EventBox()

        felicitaciones = Gtk.Label('¡Excelente! Lograste el nivel 1, intenta resolver el nivel 2.')
        felicitaciones.modify_font(Pango.FontDescription("15"))

        self.botones = []

        for boton_id in range(0, 10):
            boton = Gtk.Button()
            boton.set_size_request(150, 150)
            boton.modify_bg(Gtk.StateType.NORMAL, style.Color(COLOR_SELECCIONADO).get_gdk_color())
            boton.modify_font(Pango.FontDescription("Bold 40"))
            boton.connect("clicked", self.cambiar, nivel, felicitaciones)
            self.botones.append(boton)

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

        grid = Gtk.Grid()
        grid.props.halign = Gtk.Align.CENTER
        grid.set_row_spacing(0)
        grid.set_column_spacing(0)

        for x in range(0, 3):
            grid.attach(self.botones[x], x, 0, 1, 1)
            grid.attach(self.botones[x + 3], x, 1, 1, 1)
            grid.attach(self.botones[x + 6], x, 2, 1, 1)

        juego.add(label)
        juego.add(nivel)
        juego.add(grid)
        juego.add(felicitaciones)

        #Visibilidad de ventanas
        event_box.show_all()

    def crear_toolbars(self):
        # toolbar with the new toolbar redesign
        toolbar_box = ToolbarBox()

        activity_button = ActivityToolbarButton(self)
        toolbar_box.toolbar.insert(activity_button, 0)

        separator = Gtk.SeparatorToolItem()
        separator.props.draw = False
        separator.set_expand(True)
        toolbar_box.toolbar.insert(separator, -1)

        stop_button = StopButton(self)
        toolbar_box.toolbar.insert(stop_button, -1)

        self.set_toolbar_box(toolbar_box)
        toolbar_box.show_all()

    def cargar_botones(self):
        numeros = range(1, 10)  # Números del 1 al 9
        random.shuffle(numeros)  # Ordenar los números aleatoriamente

        for boton_id in range(0, 9):
            self.botones[boton_id].set_label(str(numeros[boton_id]))

    def cambiar(self, widget, nivel=None, felicitaciones=None):
        self.click+=1
        if self.click==1:
	    self.first_press = widget
            widget.modify_bg(Gtk.StateType.NORMAL, style.Color(COLOR_NORMAL).get_gdk_color())
        else:
            temp_val=widget.get_label()
            widget.set_label(self.first_press.get_label())
            self.first_press.set_label(str(temp_val))
            self.first_press.modify_bg(Gtk.StateType.NORMAL, style.Color(COLOR_SELECCIONADO).get_gdk_color())

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
            felicitaciones.set_text('¡Excelente! Lograste el nivel 2, intenta resolver el nivel 3.')
            self.nivel+=1
            self.click=0
            self.cargar_botones()
        elif self.nivel==3 and self.columna1==15 and self.columna2==15 and self.columna3==15:
            nivel.set_text('Nivel 4: \n'
                'Haz que las dos primeras columnas y la primera fila sumen 15 cada una!!!')
            felicitaciones.set_text('¡Excelente! Lograste el nivel 3, intenta resolver el nivel 4')
            self.nivel+=1
            self.click=0
            self.cargar_botones()
        elif self.nivel==4 and self.columna1==15 and self.columna2 == 15 and self.fila1 == 15: 
            nivel.set_text('Nivel 5: \n'
                'Haz que las tres columnas y las tres filas sumen 15 cada una!!!')
            felicitaciones.set_text('¡Excelente! Lograste el nivel 4, intenta resolver el nivel 5')
            self.nivel+=1
            self.click=0
            self.cargar_botones()
        elif self.nivel==5 and self.columna1==15 and self.columna2 == 15 and self.columna3 == 15 and self.fila1 == 15 and self.fila2 == 15 and self.fila3 == 15:
            nivel.set_text('Nivel ultimo: \n'
                'Haz que las tres columnas, las tres filas y las ambas diagonales sumen 15 cada una!!!')
            felicitaciones.set_text('¡Excelente! Lograste el nivel 4, intenta resolver el nivel 5')
            self.nivel+=1
            self.click=0
            self.cargar_botones()
        elif self.nivel==6 and self.columna1 == 15 and self.columna2==15 and self.columna3==15 and self.fila1 == 15 and self.fila2 == 15 and self.fila3 == 15 and self.diagonal1 == 15 and diagonal2 == 15:
            felicitaciones.set_markup('<span style="color: red"><b>¡Excelente! ¡Lograste resolver el último nivel!</b></span>')
