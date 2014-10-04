#!/usr/bin/env python3

from gi.repository import Gtk as gtk
import steering


class stackSwitcher(gtk.Window):

    def __init__(self):
        gtk.Window.__init__(self, title="Task Monitor")
        self.set_border_width(10)      
        self.set_default_size(200,200)

        vbox = gtk.Box(orientation=gtk.Orientation.VERTICAL, spacing=10)# spacing b/w top and main body
        self.add(vbox)

        stack = gtk.Stack()
        stack.set_transition_type(gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(300)
        
        # 1st stack
        checkbutton = gtk.CheckButton("Touch")
        stack.add_titled(checkbutton, "check","Check Button")

        # 2nd stack
        info = steering .cpuinfo()
        label= gtk.Label()
        label.set_markup("<big>CPU INFO</big>")
        
        details = ""
        for x,y in info.items():
            details += str(str(x) + " : " + str(y) + "\n")
        label.set_text(details)

        stack.add_titled(label, "cpu", "CPU Info")
        
        # 3rd stack

        stack_switcher = gtk.StackSwitcher()
        stack_switcher.set_stack(stack)
        vbox.pack_start(stack_switcher, True, True, 0) # placing order matters
        vbox.pack_start(stack, True, True, 0)


app = stackSwitcher()
app.connect("delete-event", gtk.main_quit)
app.show_all()
gtk.main()
