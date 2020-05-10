from collections.abc import MutableSequence

import wx
import wx.dataview
from wx.lib.scrolledpanel import ScrolledPanel

import discord


class ListModel(wx.dataview.DataViewVirtualListModel):
    __slots__ = ["_list"]

    def __init__(self, iterable=[]):
        super().__init__()
        self._list = list(iterable)
        self.Reset(len(self._list))

    def __len__(self):
        return len(self._list)

    def GetValueByRow(self, row, col):
        return self._list[row]

    def __getitem__(self, index):
        self._list[index]

    def __iter__(self):
        return iter(self._list)

    def __contains__(self, value):
        return value in self._list

    def __reversed__(self):
        return reversed(self._list)

    def index(self, *args, **kwargs):
        return self._list.index(*args, **kwargs)

    def count(self, value):
        return self._list.count(value)

    def __setitem__(self, index, value):
        self._list[index] = value
        self.RowChanged(index)

    def __delitem__(self, index):
        del self._list[index]
        self.RowDeleted(index)

    def insert(self, index, value):
        self._list.insert(index, value)
        self.RowInserted(index)

    def append(self, value):
        self._list.append(value)
        self.RowAppended()

    def clear(self):
        self._list.clear()
        self.Reset(len(self._list))

    def reverse(self):
        self._list.reverse()
        self.Reset(len(self._list))

    def extend(self, values):
        self._list.extend(values)
        self.Reset(len(self._list))

    def pop(self, index=-1):
        return self._list.pop(index)
        self.RowDeleted(index)

    def __iadd__(self, values):
        self.extend(values)
        return self


class PermsList(ScrolledPanel):
    def __init__(self, parent):
        super().__init__(parent)
        vbox = wx.BoxSizer(wx.VERTICAL)
        perms = [wx.CheckBox(self, label=p.desc) for p in discord.permissions]
        for p in perms:
            vbox.Add(p)
        self.SetSizer(vbox)
        self.SetupScrolling()


class RoleList(wx.ListCtrl):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs, style=wx.LC_REPORT | wx.LC_VIRTUAL | wx.LC_NO_HEADER | wx.LC_SINGLE_SEL)
        self.choices = ["Overseer", "Inquisitor", "Court Wizard", "Denizen"]
        self.AppendColumn("Name", width=wx.LIST_AUTOSIZE_USEHEADER)
        self.SetItemCount(len(self.choices))

    def OnGetItemText(self, item, column):
        return self.choices[item]


class MemberList(wx.ListBox):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs, choices=["Natalie", "Solace", "Kane", "Friend", "Stranger"])


class TabRoles(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        hbox = wx.BoxSizer(wx.HORIZONTAL)

        roles_list = RoleList(self, size=wx.Size(100, 0))
        hbox.Add(roles_list, 0, wx.EXPAND)

        self.perms = PermsList(self)
        hbox.Add(self.perms, 1, wx.EXPAND)

        self.SetSizer(hbox)


class TabMembers(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        hbox = wx.BoxSizer(wx.HORIZONTAL)

        left_vbox = wx.BoxSizer(wx.VERTICAL)
        members_list = MemberList(self, size=wx.Size(100, 0))
        left_vbox.Add(members_list, 1, wx.EXPAND)
        roles = ["Overseer", "Inquisitor", "Court Wizard", "Denizen"]
        roles_model = ListModel(roles)
        roles_list = wx.dataview.DataViewCtrl(self, style=wx.dataview.DV_NO_HEADER, size=wx.Size(100, 0))
        roles_list.AssociateModel(roles_model)
        roles_list.AppendTextColumn("Role", 0)
        left_vbox.Add(roles_list, 1, wx.EXPAND)
        hbox.Add(left_vbox, 0, wx.EXPAND)

        self.perms = PermsList(self)
        hbox.Add(self.perms, 1, wx.EXPAND)

        self.SetSizer(hbox)


class AppFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Permission Tester")

        # Create a panel and notebook (tabs holder)
        p = wx.Panel(self)
        nb = wx.Notebook(p)
        nb.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.on_notebook_page_changed)

        # Create the tab windows
        tabRoles = TabRoles(nb)
        tabMembers = TabMembers(nb)
        # ScrollSync(tabRoles.perms, tabMembers.perms)

        # Add the windows to tabs and name them
        nb.AddPage(tabRoles, "Roles")
        nb.AddPage(tabMembers, "Members")

        # Set notebook in a sizer to create the layout
        sizer = wx.BoxSizer()
        sizer.Add(nb, 1, wx.EXPAND)
        p.SetSizer(sizer)

    def on_notebook_page_changed(self, event):
        oldPerms = event.EventObject.GetPage(event.OldSelection).perms
        newPerms = event.EventObject.GetPage(event.Selection).perms

        newPerms.Scroll(wx.DefaultCoord, oldPerms.GetScrollPos(wx.VERTICAL))


if __name__ == "__main__":
    app = wx.App()
    AppFrame().Show()
    app.MainLoop()
