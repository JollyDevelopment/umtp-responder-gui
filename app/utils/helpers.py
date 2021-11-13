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
        self.del_button = Gtk.Button.new_from_icon_name("edit-delete-remove", Gtk.IconSize(4))
        self.choices_hbox = Gtk.Box.new(Gtk.Orientation(0), 3)  # 0 == horizontal
        self.whole_hbox = Gtk.Box.new(Gtk.Orientation(0), 3)  # 0 == horizontal
        self.overall_hbox = Gtk.Box.new(Gtk.Orientation(0), 3) # 0 == horizontal
        self.label = Gtk.Label.new(self.get_display_name())

    # create the list item
    # hbox (3 children)(horizontal)
    # \-label
    # \-hbox (3 children)(horizontal)
    #   \-radio button "RO"
    #   \-radio button "RW"
    #   \-radio button "D"
    # \-button (delete)

    def build_row(self):
        # show() all the bits
        self.d_radio_button.show()
        self.rw_radio_button.show()
        self.ro_radio_button.show()
        self.del_button.show()
        self.choices_hbox.show()
        self.label.show()
        self.whole_hbox.show()
        self.overall_hbox.show()
        # give the widgets names
        self.d_radio_button.set_name("disabled")
        self.rw_radio_button.set_name("rw")
        self.ro_radio_button.set_name("ro")
        self.choices_hbox.set_name("choices")
        self.del_button.set_name("delete")
        # add some space to the left of the del button
        self.del_button.set_margin_start(5)  # 5 pixels
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
        # add the whole box and the del button to the overall box
        self.overall_hbox.add(self.whole_hbox)
        self.overall_hbox.add(self.del_button)
        # return the whole box to be added as a listrow item
        return self.overall_hbox

    def set_access_level_toggle(self):
        # check the access_level, set the corresponding radio button as toggled
        if self.access_level == "ro":
            self.ro_radio_button.set_active(True)
        elif self.access_level == "rw":
            self.rw_radio_button.set_active(True)
        else:
            self.d_radio_button.set_active(True)

    def get_display_name(self):
        path_split = self.folder_path.split('/')
        return path_split.pop((len(path_split) - 1))
