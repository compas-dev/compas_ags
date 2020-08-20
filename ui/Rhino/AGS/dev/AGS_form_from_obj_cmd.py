from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import scriptcontext as sc
import compas_rhino

from compas_ags.diagrams import FormGraph
from compas_ags.diagrams import FormDiagram


__commandname__ = "AGS_form_from_obj"


def RunCommand(is_interactive):

    if 'AGS' not in sc.sticky:
        compas_rhino.display_message('AGS has not been initialised yet.')
        return

    system = sc.sticky['AGS']['system']
    scene = sc.sticky['AGS']['scene']

    filepath = compas_rhino.browse_for_file('Select an input file.', folder=system['session.dirname'], filter='obj')
    if not filepath:
        return

    graph = FormGraph.from_obj(filepath)

    # check planarity
    if not graph.is_planar_embedding():
        compas_rhino.display_message('The graph is not planar. Check your graph!')
        return

    form = FormDiagram.from_graph(graph)

    scene.add(form, name='Form', layer='AGS::FormDiagram')

    scene.clear()
    scene.update()


# ==============================================================================
# Main
# ==============================================================================
if __name__ == '__main__':

    RunCommand(True)