import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import subprocess
import threading

UI_FILE = "main.ui"

class run(Gtk.Window):
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(UI_FILE)
        self.builder.connect_signals(self)

        self.something = "1"

        self.window = self.builder.get_object("window")
        self.window.show_all()
        self.window.connect("destroy", Gtk.main_quit)

        self.sudobox = self.builder.get_object("sudobox")

        self.pkgbuffer = self.builder.get_object("entrybuffer1")

        self.sudo = self.builder.get_object("sudo")
        self.pm = self.builder.get_object("pm")
        self.option = self.builder.get_object("option")
        self.pkg = self.builder.get_object("pkg")
        self.txt = self.builder.get_object("txt")
        self.text2 = self.builder.get_object("textbuffer1")


        try:
            subprocess.run(["pacman", "--version"])
            self.pm.set_active_id("4")
        except:
            print("no pacman")

        try:
            subprocess.run(["apt", "--version"])
            self.pm.set_active_id("1")
        except:
            print("no apt")

        try:
            subprocess.run(["dnf", "--version"])
            self.pm.set_active_id("0")
        except:
            print("no dnf")

    

    def enter_clicked(self, button):
        print("something")
        self.runthread = threading.Thread(target=self.threadthing, daemon=True)

        self.runthread.start()
    
    def threadthing(self):
        self.issudo =  self.sudo.get_active_text()
            
            

        self.ispm = self.pm.get_active_text()
        self.isoption = self.option.get_active_text()

        self.ispkg = self.pkgbuffer.get_text()


        if self.issudo == "#":
            try:
                self.output = subprocess.check_output(["sudo", self.ispm, self.isoption, self.ispkg, "-y"])
            except:
                self.output = subprocess.check_output(["sudo", self.ispm, self.isoption, self.ispkg])

            self.output = str(self.output).replace('\\n', '\n').replace('\\t', '\t')

            print(self.output)


        else:
            try:
                self.output = subprocess.check_output([self.ispm, self.isoption, self.ispkg, "-y"])
            except:
                self.output = subprocess.check_output([self.ispm, self.isoption, self.ispkg])

            self.output = str(self.output).replace('\\n', '\n').replace('\\t', '\t')




        print(self.output)

        self.text2.set_text(str(self.output))







    
        




def main():
    app = run()
    Gtk.main()

if __name__ == "__main__":
    main()
