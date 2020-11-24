import plotly.graph_objects as go

class PlotTriangle (gdb.Command):
  def __init__ (self):
      super (PlotTriangle, self).__init__ ("PlotTriangle", gdb.COMMAND_USER)

  def invoke (self, arg, from_tty):
      fig = go.Figure()
      t = gdb.parse_and_eval(arg)
      p1 = t["p1"]
      p2 = t["p2"]
      p3 = t["p3"]
      triangle = dict(type="path",path="M {0} {1} L {2} {3} L {4} {5} Z".format(p1["x"],p1["y"],p2["x"],p2["y"],p3["x"],p3["y"]), line_color="Crimson")
      fig.update_layout(shapes=[triangle])
      fig.show()

PlotTriangle()
