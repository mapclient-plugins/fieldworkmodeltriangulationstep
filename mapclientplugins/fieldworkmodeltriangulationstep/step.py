"""
MAP Client, a program to generate detailed musculoskeletal models for OpenSim.
    Copyright (C) 2012  University of Auckland
    
This file is part of MAP Client. (http://launchpad.net/mapclient)

    MAP Client is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    MAP Client is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with MAP Client.  If not, see <http://www.gnu.org/licenses/>..
"""
'''
MAP Client Plugin Step
'''
import json

from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint
from mapclientplugins.fieldworkmodeltriangulationstep.configuredialog import ConfigureDialog


class FieldworkModelTriangulationStep(WorkflowStepMountPoint):
    """
    Skeleton step which is intended to be a helpful starting point
    for new steps.
    """

    def __init__(self, location):
        super(FieldworkModelTriangulationStep, self).__init__('Fieldwork Model Triangulation', location)
        self._configured = True  # A step cannot be executed until it has been configured.
        self._category = 'Fieldwork'
        # Add any other initialisation code here:
        # self._icon =  QtGui.QImage(':/fieldworkexportstlsurfacestep/images/fieldworkexportstlsurface.png')
        # Ports:
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'ju#fieldworkmodel'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#pointcloud'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#faces'))
        self._config = {}
        self._config['discretisation'] = '10,10'
        self._model = None
        self._v = None
        self._f = None

        self._identifier = ''

    def execute(self):
        """
        Add your code here that will kick off the execution of the step.
        Make sure you call the _doneExecution() method when finished.  This method
        may be connected up to a button in a widget for example.
        """
        # Put your execute step code here before calling the '_doneExecution' method.
        if 'x' in self._config['discretisation']:
            d = [int(x) for x in self._config['discretisation'].split('x')]
        else:
            d = [int(x) for x in self._config['discretisation'].split(',')]
        if len(d) != 2:
            raise ValueError('Incorrected discretisation: ' + self._config['discretisation'])

        self._v, self._f = self._model.triangulate(d, merge=True)

        self._doneExecution()

    def setPortData(self, index, dataIn):
        """
        Add your code here that will set the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        uses port for this step then the index can be ignored.
        """
        self._model = dataIn  # ju#fieldworkmodel

    def getPortData(self, index):
        if index == 1:
            return self._v
        else:
            return self._f

    def configure(self):
        """
        This function will be called when the configure icon on the step is
        clicked.  It is appropriate to display a configuration dialog at this
        time.  If the conditions for the configuration of this step are complete
        then set:
            self._configured = True
        """
        dlg = ConfigureDialog(self._main_window)
        dlg.setConfig(self._config)
        dlg.validate()
        dlg.setModal(True)

        if dlg.exec_():
            self._config = dlg.getConfig()

        self._configured = dlg.validate()
        self._configuredObserver()

    def getIdentifier(self):
        """
        The identifier is a string that must be unique within a workflow.
        """
        return self._identifier

    def setIdentifier(self, identifier):
        """
        The framework will set the identifier for this step when it is loaded.
        """
        self._identifier = identifier

    def serialize(self):
        """
        Add code to serialize this step to disk. Returns a json string for
        mapclient to serialise.
        """
        return json.dumps(self._config, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def deserialize(self, string):
        """
        Add code to deserialize this step from disk. Parses a json string
        given by mapclient
        """
        self._config.update(json.loads(string))

        d = ConfigureDialog()
        d.setConfig(self._config)
        self._configured = d.validate()
