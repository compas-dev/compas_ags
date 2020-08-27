from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import scriptcontext as sc

import compas_rhino


__commandname__ = "AGS_form_displaysettings"


def RunCommand(is_interactive):

    if 'AGS' not in sc.sticky:
        compas_rhino.display_message('AGS has not been initialised yet.')
        return

    scene = sc.sticky['AGS']['scene']

    objects = scene.find_by_name('Form')
    if not objects:
        compas_rhino.display_message("There is no FormDiagram in the scene.")
        return
    form = objects[0]

    options = ["Vertexlabels", "Edgelabels", "Forcelabels", "CompressionTension", "PipeScale"]

    while True:
        option = compas_rhino.rs.GetString("FormDiagram Display", strings=options)

        if not option or option not in options:
            return

        if option == "Vertexlabels":
            current = str(form.artist.settings['show.vertexlabels'])
            show = compas_rhino.rs.GetString("Vertex labels", current, ["True", "False"])

            if show == "True":
                form.artist.settings['show.vertexlabels'] = True
            elif show == "False":
                form.artist.settings['show.vertexlabels'] = False

        elif option == "Edgelabels":
            current = str(form.artist.settings['show.edgelabels'])
            show = compas_rhino.rs.GetString("Edge labels", current, ["True", "False"])

            if show == "True":
                form.artist.settings['show.edgelabels'] = True
                form.artist.settings['show.forcelabels'] = False
            elif show == "False":
                form.artist.settings['show.edgelabels'] = False

        elif option == "Forcelabels":
            current = str(form.artist.settings['show.forcelabels'])
            show = compas_rhino.rs.GetString("Force labels", current, ["True", "False"])

            if show == "True":
                form.artist.settings['show.forcelabels'] = True
                form.artist.settings['show.edgelabels'] = False
            elif show == "False":
                form.artist.settings['show.forcelabels'] = False

        elif option == "CompressionTension":
            current = str(form.artist.settings['show.forces'])
            show = compas_rhino.rs.GetString("Compression / Tension", current, ["True", "False"])

            if show == "True":
                form.artist.settings['show.forces'] = True
            elif show == "False":
                form.artist.settings['show.forces'] = False

        elif option == "PipeScale":
            scale = compas_rhino.rs.GetReal("Scale Forces", form.artist.settings['scale.forces'])
            scale = float(scale)
            form.artist.settings['scale.forces'] = scale

        else:
            raise NotImplementedError

        scene.update()


# ==============================================================================
# Main
# ==============================================================================

if __name__ == '__main__':

    RunCommand(True)
