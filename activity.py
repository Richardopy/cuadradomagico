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
                        'Haz que todos los numeros alineados horizontalmente sumen 15!!!')
        hbox1 = Gtk.HButtonBox()
        hbox1.set_layout(Gtk.ButtonBoxStyle.CENTER)
        event_box = Gtk.EventBox()  
        self.button1 = Gtk.Button()
        self.button1.set_size_request(150, 150)
        self.button1.modify_bg(Gtk.StateType.NORMAL, 
                                style.Color("#1CCD16").get_gdk_color())
        self.button2 = Gtk.Button()
        self.button2.set_size_request(150, 150)
        self.button2.modify_bg(Gtk.StateType.NORMAL, 
                                style.Color("#1CCD16").get_gdk_color())
        self.button3 = Gtk.Button()
        self.button3.set_size_request(150, 150)
        self.button3.modify_bg(Gtk.StateType.NORMAL, 
                                style.Color("#1CCD16").get_gdk_color())
        hbox2 = Gtk.HButtonBox()
        hbox2.set_layout(Gtk.ButtonBoxStyle.CENTER)
        self.button4 = Gtk.Button()
        self.button4.set_size_request(150, 150)
        self.button4.modify_bg(Gtk.StateType.NORMAL, 
                                style.Color("#1CCD16").get_gdk_color())
        self.button5 = Gtk.Button()
        self.button5.set_size_request(150, 150)
        self.button5.modify_bg(Gtk.StateType.NORMAL, 
                                style.Color("#1CCD16").get_gdk_color())
        self.button6 = Gtk.Button()
        self.button6.set_size_request(150, 150)
        self.button6.modify_bg(Gtk.StateType.NORMAL, 
                                style.Color("#1CCD16").get_gdk_color())
        hbox3 = Gtk.HButtonBox()
        hbox3.set_layout(Gtk.ButtonBoxStyle.CENTER)
        self.button7 = Gtk.Button()
        self.button7.set_size_request(150, 150)
        self.button7.modify_bg(Gtk.StateType.NORMAL, 
                                style.Color("#1CCD16").get_gdk_color())
        self.button8 = Gtk.Button()
        self.button8.set_size_request(150, 150)
        self.button8.modify_bg(Gtk.StateType.NORMAL, 
                                style.Color("#1CCD16").get_gdk_color())
        self.button9 = Gtk.Button()
        self.button9.set_size_request(150, 150)
        self.button9.modify_bg(Gtk.StateType.NORMAL, 
                                style.Color("#1CCD16").get_gdk_color())
        hbox4 = Gtk.HButtonBox()
        hbox4.set_layout(Gtk.ButtonBoxStyle.CENTER)
        felicitaciones=Gtk.Label('Excelente lograste el nivel 1 prueba resolviendo el nivel 2!!!')

        self.sumat=0
        self.sumaf1=0
        self.sumaf2=0
        self.sumaf3=0
        self.sumac1=0
        self.sumac2=0
        self.sumac3=0
        self.sumad1=0
        self.sumad2=0
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

        self.button1.connect("clicked",self.cambiar, nivel, felicitaciones, 'self.button1')
        self.button2.connect("clicked",self.cambiar, nivel, felicitaciones, 'self.button2')
        self.button3.connect("clicked",self.cambiar, nivel, felicitaciones, 'self.button3')
        self.button4.connect("clicked",self.cambiar, nivel, felicitaciones, 'self.button4')
        self.button5.connect("clicked",self.cambiar, nivel, felicitaciones, 'self.button5')
        self.button6.connect("clicked",self.cambiar, nivel, felicitaciones, 'self.button6')
        self.button7.connect("clicked",self.cambiar, nivel, felicitaciones, 'self.button7')
        self.button8.connect("clicked",self.cambiar, nivel, felicitaciones, 'self.button8')
        self.button9.connect("clicked",self.cambiar, nivel, felicitaciones, 'self.button9')

        self.set_canvas(event_box)
        event_box.add(juego)
        juego.add(label)
        juego.add(nivel)
        juego.add(hbox1)
        hbox1.add(self.button1)
        hbox1.add(self.button2)
        hbox1.add(self.button3)
        juego.add(hbox2)
        hbox2.add(self.button4)
        hbox2.add(self.button5)
        hbox2.add(self.button6)
        juego.add(hbox3)
        hbox3.add(self.button7)
        hbox3.add(self.button8)
        hbox3.add(self.button9)
        juego.add(hbox4)
        juego.add(felicitaciones)

        #Visibilidad de ventanas
        event_box.show_all()

    def cargar_botones(self):
        self.x= random.randint(1,9)
        if self.x==1:
            self.a=self.x+5
            self.b=self.x+3 
            self.c=self.x+4
            self.d=self.x
            self.e=self.x+7
            self.f=self.x+8
            self.g=self.x+1
            self.h=self.x+2
            self.i=self.x+6
            self.button1.set_label(str(self.a))
            self.button2.set_label(str(self.b))
            self.button3.set_label(str(self.c))
            self.button4.set_label(str(self.d))
            self.button5.set_label(str(self.e))
            self.button6.set_label(str(self.f))
            self.button7.set_label(str(self.g))
            self.button8.set_label(str(self.h))
            self.button9.set_label(str(self.i))
        elif self.x==2:      
            self.a=self.x-1
            self.b=self.x+3
            self.c=self.x+5
            self.d=self.x+4
            self.e=self.x+6
            self.f=self.x+7
            self.g=self.x
            self.h=self.x+2
            self.i=self.x+1
            self.button1.set_label(str(self.a))
            self.button2.set_label(str(self.b))
            self.button3.set_label(str(self.c))
            self.button4.set_label(str(self.d))
            self.button5.set_label(str(self.e))
            self.button6.set_label(str(self.f))
            self.button7.set_label(str(self.g))
            self.button8.set_label(str(self.h))
            self.button9.set_label(str(self.i))
        elif self.x==3:
            self.a=self.x-1
            self.b=self.x+3
            self.c=self.x+5 
            self.d=self.x+4
            self.e=self.x+6
            self.f=self.x-2
            self.g=self.x
            self.h=self.x+2
            self.i=self.x+1
            self.button1.set_label(str(self.a))
            self.button2.set_label(str(self.b))
            self.button3.set_label(str(self.c))
            self.button4.set_label(str(self.d))
            self.button5.set_label(str(self.e))
            self.button6.set_label(str(self.f))
            self.button7.set_label(str(self.g))
            self.button8.set_label(str(self.h))
            self.button9.set_label(str(self.i))
        elif self.x==4:
            self.a=self.x-1
            self.b=self.x+3
            self.c=self.x+5
            self.d=self.x+4
            self.e=self.x-2
            self.f=self.x-3
            self.g=self.x
            self.h=self.x+2
            self.i=self.x+1
            self.button1.set_label(str(self.a))
            self.button2.set_label(str(self.b))
            self.button3.set_label(str(self.c))
            self.button4.set_label(str(self.d))
            self.button5.set_label(str(self.e))
            self.button6.set_label(str(self.f))
            self.button7.set_label(str(self.g))
            self.button8.set_label(str(self.h))
            self.button9.set_label(str(self.i))
        elif self.x==5:
            self.a=self.x-1
            self.b=self.x+3
            self.c=self.x+2
            self.d=self.x+4
            self.e=self.x-4
            self.f=self.x-3
            self.g=self.x
            self.h=self.x-2
            self.i=self.x+1
            self.button1.set_label(str(self.a))
            self.button2.set_label(str(self.b))
            self.button3.set_label(str(self.c))
            self.button4.set_label(str(self.d))
            self.button5.set_label(str(self.e))
            self.button6.set_label(str(self.f))
            self.button7.set_label(str(self.g))
            self.button8.set_label(str(self.h))
            self.button9.set_label(str(self.i))
        elif self.x==6:
            self.a=self.x-1
            self.b=self.x+3
            self.c=self.x-2
            self.d=self.x-5
            self.e=self.x-3
            self.f=self.x-4
            self.g=self.x
            self.h=self.x+2
            self.i=self.x+1
            self.button1.set_label(str(self.a))
            self.button2.set_label(str(self.b))
            self.button3.set_label(str(self.c))
            self.button4.set_label(str(self.d))
            self.button5.set_label(str(self.e))
            self.button6.set_label(str(self.f))
            self.button7.set_label(str(self.g))
            self.button8.set_label(str(self.h))
            self.button9.set_label(str(self.i))                   
        elif self.x==7:
            self.a=self.x-1
            self.b=self.x+2
            self.c=self.x-5
            self.d=self.x-6
            self.e=self.x-3
            self.f=self.x-4
            self.g=self.x
            self.h=self.x-2
            self.i=self.x+1
            self.button1.set_label(str(self.a))
            self.button2.set_label(str(self.b))
            self.button3.set_label(str(self.c))
            self.button4.set_label(str(self.d))
            self.button5.set_label(str(self.e))
            self.button6.set_label(str(self.f))
            self.button7.set_label(str(self.g))
            self.button8.set_label(str(self.h))
            self.button9.set_label(str(self.i))
        elif self.x==8:
            self.a=self.x-1
            self.b=self.x+1
            self.c=self.x-2
            self.d=self.x-5
            self.e=self.x-3
            self.f=self.x-4
            self.g=self.x
            self.h=self.x-7
            self.i=self.x-6
            self.button1.set_label(str(self.a))
            self.button2.set_label(str(self.b))
            self.button3.set_label(str(self.c))
            self.button4.set_label(str(self.d))
            self.button5.set_label(str(self.e))
            self.button6.set_label(str(self.f))
            self.button7.set_label(str(self.g))
            self.button8.set_label(str(self.h))
            self.button9.set_label(str(self.i))
        else:
            self.a=self.x
            self.b=self.x-7
            self.c=self.x-2
            self.d=self.x-4
            self.e=self.x-1
            self.f=self.x-5
            self.g=self.x-6
            self.h=self.x-3
            self.i=self.x-8
            self.button1.set_label(str(self.a))
            self.button2.set_label(str(self.b))
            self.button3.set_label(str(self.c))
            self.button4.set_label(str(self.d))
            self.button5.set_label(str(self.e))
            self.button6.set_label(str(self.f))
            self.button7.set_label(str(self.g))
            self.button8.set_label(str(self.h))
            self.button9.set_label(str(self.i))

    def cambiar(self, widget, nivel=None, felicitaciones=None ,Data=None):
        self.click+=1
        if self.click==1:
            self.x1=Data
            self.x2=widget.get_label()
            widget.modify_bg(Gtk.StateType.NORMAL, style.Color("#F20000").get_gdk_color())
        else:
            self.x3=widget.get_label()
            widget.set_label(self.x2)
            if self.x1=='self.button1':
                self.button1.set_label(str(self.x3))
                self.button1.modify_bg(Gtk.StateType.NORMAL, style.Color("#1CCD16").get_gdk_color())
            elif self.x1=='self.button2':
                self.button2.set_label(str(self.x3))
                self.button2.modify_bg(Gtk.StateType.NORMAL, style.Color("#1CCD16").get_gdk_color())
            elif self.x1=='self.button3':
                self.button3.set_label(str(self.x3))
                self.button3.modify_bg(Gtk.StateType.NORMAL, style.Color("#1CCD16").get_gdk_color())
            elif self.x1=='self.button4':
                self.button4.set_label(str(self.x3))
                self.button4.modify_bg(Gtk.StateType.NORMAL, style.Color("#1CCD16").get_gdk_color())
            elif self.x1=='self.button5':
                self.button5.set_label(str(self.x3))
                self.button5.modify_bg(Gtk.StateType.NORMAL, style.Color("#1CCD16").get_gdk_color())
            elif self.x1=='self.button6':
                self.button6.set_label(str(self.x3))
                self.button6.modify_bg(Gtk.StateType.NORMAL, style.Color("#1CCD16").get_gdk_color())
            elif self.x1=='self.button7':
                self.button7.set_label(str(self.x3))
                self.button7.modify_bg(Gtk.StateType.NORMAL, style.Color("#1CCD16").get_gdk_color())
            elif self.x1=='self.button8':
                self.button8.set_label(str(self.x3))
                self.button8.modify_bg(Gtk.StateType.NORMAL, style.Color("#1CCD16").get_gdk_color())
            else:
                self.button9.set_label(str(self.x3))
                self.button9.modify_bg(Gtk.StateType.NORMAL, style.Color("#1CCD16").get_gdk_color())
            self.click=0
            self.fila1=int(self.button1.get_label()) + int(self.button2.get_label()) + int(self.button3.get_label())
            self.fila2=int(self.button4.get_label()) + int(self.button5.get_label()) + int(self.button6.get_label())
            self.fila3=int(self.button7.get_label()) + int(self.button8.get_label()) + int(self.button9.get_label())
            self.columna1=int(self.button1.get_label()) + int(self.button4.get_label()) + int(self.button7.get_label())
            self.columna2=int(self.button2.get_label()) + int(self.button5.get_label()) + int(self.button8.get_label())
            self.columna3=int(self.button3.get_label()) + int(self.button6.get_label()) + int(self.button9.get_label())
            self.diagonal1=int(self.button1.get_label()) + int(self.button5.get_label()) + int(self.button9.get_label())
            self.diagonal2=int(self.button7.get_label()) + int(self.button5.get_label()) + int(self.button3.get_label())
    
        if self.nivel==1 and self.fila1==15 and self.fila2==15 and self.fila3==15:
            nivel.set_text('Nivel 2: \n'
                'Haz que todos los numeros alineados en forma vertical y horizontal sumen 15!!!')
            felicitaciones.set_visible(True)
            self.nivel+=1
            self.click=0
            self.cargar_botones()
        elif self.nivel==2 and self.fila1==15 and self.fila2==15 and self.fila3==15 and self.columna1==15 and self.columna2==15 and self.columna3==15:
            nivel.set_text('Nivel 3: \n'
                'Haz que todos los numeros alineados en forma vertical, horizontal y diagonal sumen 15!!!')
            felicitaciones.set_text('Excelente lograste el nivel 2 prueba resolviendo el nivel 3!!!')
            self.nivel+=1
            self.click=0
            self.cargar_botones()
        elif self.nivel==3 and self.fila1==15 and self.fila2==15 and self.fila3==15 and self.columna1==15 and self.columna2==15 and self.columna3==15 and self.diagonal1==15 and self.diagonal2==15:
            felicitaciones.set_text('Excelente lograste el nivel 3')