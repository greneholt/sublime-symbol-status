import sublime, sublime_plugin

class SymbolStatusHander(sublime_plugin.EventListener):
  def on_selection_modified_async(self, view):
    for region in view.sel():
      region_row, region_col = view.rowcol(region.begin())
      for (r, name) in reversed(view.symbols()):
        row, col = view.rowcol(r.begin())
        if row <= region_row:
          view.set_status('last_symbol', name.strip())
          print(name)
          return

    view.erase_status('last_symbol')
