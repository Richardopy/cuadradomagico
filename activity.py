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
        win = Gtk.VBox()
        menu = Gtk.VButtonBox()
        menu.set_layout(Gtk.ButtonBoxStyle.CENTER)
        jugar = Gtk.Button('Jugar')
        jugar.modify_bg(Gtk.StateType.NORMAL,
                            style.Color("#FF2525").get_gdk_color())
        jugar.set_size_request(250, 150)
        ayuda = Gtk.Button('Ayuda')
        ayuda.set_size_request(250, 150)
        jugar.modify_bg(Gtk.StateType.PRELIGHT, 
                        style.Color("#FF5A5A").get_gdk_color())
        ayuda.modify_bg(Gtk.StateType.NORMAL, 
                        style.Color("#12DE03").get_gdk_color())
        ayuda.modify_bg(Gtk.StateType.PRELIGHT, 
                        style.Color("#54DA4A").get_gdk_color())
        acerca = Gtk.Button('Creditos')
        acerca.set_size_request(250, 150)
        acerca.modify_bg(Gtk.StateType.NORMAL, 
                           style.Color("#FFEF06").get_gdk_color())
        acerca.modify_bg(Gtk.StateType.PRELIGHT, 
                            style.Color("#FFF666").get_gdk_color())
        menu.add(jugar)
        menu.add(ayuda)
        menu.add(acerca)
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
        volver = Gtk.Button('Volver')
        volver.modify_bg(Gtk.StateType.NORMAL, 
                                style.Color("#FF2525").get_gdk_color())
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

        jugar.connect("clicked",self.jugar, menu, juego, felicitaciones)
        volver.connect("clicked",self.menu, menu, juego)

        self.set_canvas(event_box)
        event_box.add(win)
        #Primera ventana
        win.add(menu)
        menu.add(jugar)
        menu.add(ayuda)
        menu.add(acerca)

        #Segunda ventana
        win.add(juego)
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
        hbox4.add(volver)
        juego.add(felicitaciones)

        #Visibilidad de ventanas
        event_box.show_all()
        juego.set_visible(False)

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

    def jugar(self, widget, menu=None, juego=None, felicitaciones=None):
        menu.set_visible(False)
        juego.set_visible(True)
        felicitaciones.set_visible(False)

    def menu(self, widget, menu=None, juego=None):
        menu.set_visible(True)
        juego.set_visible(False)
