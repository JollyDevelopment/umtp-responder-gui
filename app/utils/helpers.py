#
# helper classes for umtp-responder-gui
#

# ----- imports -----
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio, Gdk


# ----- variables -----


# ----- functions ------


# ----- classes -----


# class: RowItem
# this is to load into the list of exports

class RowItem(object):
    def __init__(self, folder_path="/tmp", access_level="ro"):
        self.folder_path = folder_path
        self.access_level = access_level
        self.d_radio_button = Gtk.RadioButton.new_with_label(None, "D")
        self.rw_radio_button = Gtk.RadioButton.new_with_label(None, "RW")
        self.ro_radio_button = Gtk.RadioButton.new_with_label(None, "RO")
        self.choices_hbox = Gtk.Box.new(Gtk.Orientation(0), 3)  # 0 == horizontal
        self.whole_hbox = Gtk.Box.new(Gtk.Orientation(0), 3)  # 0 == horizontal
        self.label = Gtk.Label.new(self.folder_path)

    # create the list item
    # hbox (2 children)(horizontal
    # \-label
    # \-hbox (3 children)(horizontal)
    #   \-radio button "RO"
    #   \-radio button "RW"
    #   \-radio button "D"

    def build_row(self):
        # show() all the bits
        self.d_radio_button.show()
        self.rw_radio_button.show()
        self.ro_radio_button.show()
        self.choices_hbox.show()
        self.label.show()
        self.whole_hbox.show()
        # give the widgets names
        self.d_radio_button.set_name("disabled")
        self.rw_radio_button.set_name("rw")
        self.ro_radio_button.set_name("ro")
        self.choices_hbox.set_name("choices")
        # add the ro/rw buttons to the disabled buttons group
        self.ro_radio_button.join_group(self.d_radio_button)
        self.rw_radio_button.join_group(self.d_radio_button)
        # set the access toggle
        self.set_access_level_toggle()
        # add the radio buttons to the choices box
        self.choices_hbox.add(self.d_radio_button)
        self.choices_hbox.add(self.rw_radio_button)
        self.choices_hbox.add(self.ro_radio_button)
        # add the choices box and the label to the whole box
        self.whole_hbox.add(self.label)
        self.whole_hbox.add(self.choices_hbox)
        # set the whole_box to be homogenous (so both children take up the same space)
        self.whole_hbox.set_homogeneous(True)
        # return the whole box to be added as a listrow item
        return self.whole_hbox

    def set_access_level_toggle(self):
        # check the access_level, set the corresponding radio button as toggled
        if self.access_level == "ro":
            self.ro_radio_button.set_active(True)
        elif self.access_level == "rw":
            self.rw_radio_button.set_active(True)
        else:
            self.d_radio_button.set_active(True)

