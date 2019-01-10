#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import gui3d
import gui
from core import G

from .randomizeaction import RandomizeAction
from .humanstate import HumanState

mhapi = gui3d.app.mhapi

import mh, time, os, re

from PyQt5.QtWidgets import *

import pprint
pp = pprint.PrettyPrinter(indent=4)

DEFAULT_TABLE_HEIGHT=250
DEFAULT_LABEL_COLUMN_WIDTH=300

class MassProduceTaskView(gui3d.TaskView):

    def __init__(self, category):
        gui3d.TaskView.__init__(self, category, 'Mass produce')

        self.human = G.app.selectedHuman

        self.log = mhapi.utility.getLogChannel("massproduce")

        self._setupLeftPanel()
        self._setupMainPanel()
        self._setupRightPanel()

    def _setupLeftPanel(self):
        self.addLeftWidget( self._createMacroSettings() )
        self.addLeftWidget(mhapi.ui.createLabel())
        self.addLeftWidget( self._createModelingSettings() )

    def _setupAllowedSkinsTables(self, layout):


        sysSkins = mhapi.assets.getAvailableSystemSkins()
        userSkins = mhapi.assets.getAvailableUserSkins()

        allowedFemaleSkins = dict()
        allowedMaleSkins = dict()

        pp.pprint(sysSkins)
        pp.pprint(userSkins)

        skinBaseNames = []
        for s in sysSkins:
            bn = os.path.basename(s).lower()
            bn = re.sub(r'.mhmat','',bn)
            bn = re.sub(r'_', ' ', bn)
            skinBaseNames.append(bn)

            allowedFemaleSkins[bn] = dict()
            allowedFemaleSkins[bn]["fullPath"] = os.path.abspath(s)
            allowedMaleSkins[bn] = dict()
            allowedMaleSkins[bn]["fullPath"] = os.path.abspath(s)

        for s in userSkins:
            bn = os.path.basename(s).lower()
            bn = re.sub(r'.mhmat', '', bn)
            bn = re.sub(r'_', ' ', bn)
            skinBaseNames.append(bn)

            allowedFemaleSkins[bn] = dict()
            allowedFemaleSkins[bn]["fullPath"] = os.path.abspath(s)
            allowedMaleSkins[bn] = dict()
            allowedMaleSkins[bn]["fullPath"] = os.path.abspath(s)

        skinBaseNames.sort()

        self.allowedFemaleSkinsTable = QTableWidget()
        self.allowedFemaleSkinsTable.setRowCount(len(skinBaseNames))
        self.allowedFemaleSkinsTable.setColumnCount(5)
        self.allowedFemaleSkinsTable.setHorizontalHeaderLabels(["Skin", "Mixed", "African", "Asian", "Caucasian"])

        self.allowedMaleSkinsTable = QTableWidget()
        self.allowedMaleSkinsTable.setRowCount(len(skinBaseNames))
        self.allowedMaleSkinsTable.setColumnCount(5)
        self.allowedMaleSkinsTable.setHorizontalHeaderLabels(["Skin", "Mixed", "African", "Asian", "Caucasian"])

        skins = dict()

        i = 0
        for n in skinBaseNames:

            female = allowedFemaleSkins[n]
            male = allowedMaleSkins[n]

            self.allowedFemaleSkinsTable.setItem(i, 0, QTableWidgetItem(n))
            self.allowedMaleSkinsTable.setItem(i, 0, QTableWidgetItem(n))

            male["mixed"] = mhapi.ui.createCheckBox("")
            male["african"] = mhapi.ui.createCheckBox("")
            male["asian"] = mhapi.ui.createCheckBox("")
            male["caucasian"] = mhapi.ui.createCheckBox("")

            self.allowedMaleSkinsTable.setCellWidget(i, 1, male["mixed"])
            self.allowedMaleSkinsTable.setCellWidget(i, 2, male["african"])
            self.allowedMaleSkinsTable.setCellWidget(i, 3, male["asian"])
            self.allowedMaleSkinsTable.setCellWidget(i, 4, male["caucasian"])

            female["mixed"] = mhapi.ui.createCheckBox("")
            female["african"] = mhapi.ui.createCheckBox("")
            female["asian"] = mhapi.ui.createCheckBox("")
            female["caucasian"] = mhapi.ui.createCheckBox("")

            self.allowedFemaleSkinsTable.setCellWidget(i, 1, female["mixed"])
            self.allowedFemaleSkinsTable.setCellWidget(i, 2, female["african"])
            self.allowedFemaleSkinsTable.setCellWidget(i, 3, female["asian"])
            self.allowedFemaleSkinsTable.setCellWidget(i, 4, female["caucasian"])

            if self._matchesEthnicGender(n,"female"):

                female["mixed"].setChecked(True)

                if self._matchesEthnicGender(n,ethnicity="african"):
                    female["african"].setChecked(True)
                if self._matchesEthnicGender(n,ethnicity="asian") and not self._matchesEthnicGender(n,ethnicity="caucasian"):
                    female["asian"].setChecked(True)
                if self._matchesEthnicGender(n,ethnicity="caucasian"):
                    female["caucasian"].setChecked(True)

            if self._matchesEthnicGender(n,"male") and not self._matchesEthnicGender(n,"female"):

                male["mixed"].setChecked(True)

                if self._matchesEthnicGender(n,ethnicity="african"):
                    male["african"].setChecked(True)
                if self._matchesEthnicGender(n,ethnicity="asian") and not self._matchesEthnicGender(n,ethnicity="caucasian"):
                    male["asian"].setChecked(True)
                if self._matchesEthnicGender(n,ethnicity="caucasian"):
                    male["caucasian"].setChecked(True)

            i = i + 1

        self.allowedFemaleSkinsTable.setColumnWidth(0, DEFAULT_LABEL_COLUMN_WIDTH)
        self.allowedMaleSkinsTable.setColumnWidth(0, DEFAULT_LABEL_COLUMN_WIDTH)

        i = 1
        while i < 5:
            self.allowedFemaleSkinsTable.setColumnWidth(i, 80)
            self.allowedMaleSkinsTable.setColumnWidth(i, 80)
            i = i + 1

        self.allowedFemaleSkinsTable.setMaximumHeight(DEFAULT_TABLE_HEIGHT)
        self.allowedMaleSkinsTable.setMaximumHeight(DEFAULT_TABLE_HEIGHT)

        layout.addWidget(mhapi.ui.createLabel("Allowed female skins:"))
        layout.addWidget(self.allowedFemaleSkinsTable)

        layout.addWidget(mhapi.ui.createLabel(""))

        layout.addWidget(mhapi.ui.createLabel("Allowed male skins:"))
        layout.addWidget(self.allowedMaleSkinsTable)

        self.allowedFemaleSkins = allowedFemaleSkins
        self.allowedMaleSkins = allowedMaleSkins


    def _matchesEthnicGender(self, teststring, gender = None, ethnicity = None):

        if not gender is None:
            if not gender in teststring:
                return False
        if not ethnicity is None:
            if not ethnicity in teststring:
                return False

        return True

    def _setupMainPanel(self):

        self.tableData = dict()

        self.mainSettingsPanel = QWidget()
        self.mainSettingsLayout = QVBoxLayout()

        self.testWidget = QTableWidget()
        self.testWidget.setRowCount(5)
        self.testWidget.setColumnCount(3)

        self._setupAllowedSkinsTables(self.mainSettingsLayout)

        self.mainSettingsLayout.addStretch()
        self.mainSettingsPanel.setLayout(self.mainSettingsLayout)
        self.addTopWidget(self.mainSettingsPanel)

    def _setupRightPanel(self):
        self.addRightWidget(self._createExportSettings())
        self.addRightWidget(mhapi.ui.createLabel())
        self.addRightWidget(self._createProducePanel())

    def _createExportSettings(self):
        self.exportPanel = mhapi.ui.createGroupBox("Export settings")
        self.exportPanel.addWidget(mhapi.ui.createLabel("File name base"))
        self.fnbase = self.exportPanel.addWidget(mhapi.ui.createTextEdit("mass"))
        self.exportPanel.addWidget(mhapi.ui.createLabel(""))

        data = ["MHM","OBJ","MHX","FBX","DAE"]

        self.exportPanel.addWidget(mhapi.ui.createLabel("File format"))
        self.fileformat = self.exportPanel.addWidget(mhapi.ui.createComboBox(data=data))

        info = "\nFiles end up in the\n"
        info +="usual directory, named\n"
        info +="with the file name base\n"
        info +="plus four digits plus\n"
        info +="file extension."

        self.exportPanel.addWidget(mhapi.ui.createLabel(info))

        return self.exportPanel

    def _createProducePanel(self):
        self.producePanel = mhapi.ui.createGroupBox("Produce")

        self.producePanel.addWidget(mhapi.ui.createLabel("Number of characters"))
        self.numfiles = self.producePanel.addWidget(mhapi.ui.createTextEdit("2"))
        self.producePanel.addWidget(mhapi.ui.createLabel(""))
        self.produceButton = self.producePanel.addWidget(mhapi.ui.createButton("Produce"))

        @self.produceButton.mhEvent
        def onClicked(event):
            self._onProduceClick()

        return self.producePanel

    def _createModelingSettings(self):
        self.modelingPanel = mhapi.ui.createGroupBox("Modeling settings")

        self.head = self.modelingPanel.addWidget(mhapi.ui.createCheckBox(label="Randomize head", selected=True))
        self.face = self.modelingPanel.addWidget(mhapi.ui.createCheckBox(label="Randomize face", selected=True))
        self.torso = self.modelingPanel.addWidget(mhapi.ui.createCheckBox(label="Randomize torso", selected=True))
        self.stomach = self.modelingPanel.addWidget(mhapi.ui.createCheckBox(label="Randomize stomach", selected=True))
        self.buttocks = self.modelingPanel.addWidget(mhapi.ui.createCheckBox(label="Randomize buttocks", selected=True))
        self.pelvis = self.modelingPanel.addWidget(mhapi.ui.createCheckBox(label="Randomize pelvis", selected=True))
        self.arms = self.modelingPanel.addWidget(mhapi.ui.createCheckBox(label="Randomize arms", selected=False))
        self.hands = self.modelingPanel.addWidget(mhapi.ui.createCheckBox(label="Randomize hands", selected=False))
        self.legs = self.modelingPanel.addWidget(mhapi.ui.createCheckBox(label="Randomize legs", selected=False))
        self.feet = self.modelingPanel.addWidget(mhapi.ui.createCheckBox(label="Randomize feet", selected=False))

        self.modelingPanel.addWidget(mhapi.ui.createLabel())
        self.maxdev = self.modelingPanel.addWidget(mhapi.ui.createSlider(value=0.3, min=0.0, max=1.0, label="Max deviation from default"))

        self.modelingPanel.addWidget(mhapi.ui.createLabel())
        self.symmetry = self.modelingPanel.addWidget(mhapi.ui.createSlider(value=0.7, min=0.0, max=1.0, label="Symmetry"))

        return self.modelingPanel

    def _createMacroSettings(self):
        self.macroPanel = mhapi.ui.createGroupBox("Macro settings")

        self.randomizeAge = self.macroPanel.addWidget(mhapi.ui.createCheckBox(label="Randomize age", selected=True))
        self.ageMinimum = self.macroPanel.addWidget(mhapi.ui.createSlider(label="Minimum age", value=0.45))
        self.ageMaximum = self.macroPanel.addWidget(mhapi.ui.createSlider(label="Maximum age", value=0.95))

        self.macroPanel.addWidget(mhapi.ui.createLabel())

        self.randomizeWeight = self.macroPanel.addWidget(mhapi.ui.createCheckBox(label="Randomize weight", selected=True))
        self.weightMinimum = self.macroPanel.addWidget(mhapi.ui.createSlider(label="Minimum weight", value=0.1))
        self.weightMaximum = self.macroPanel.addWidget(mhapi.ui.createSlider(label="Maximum weight", value=0.9))

        self.macroPanel.addWidget(mhapi.ui.createLabel())

        self.randomizeHeight = self.macroPanel.addWidget(mhapi.ui.createCheckBox(label="Randomize height", selected=True))
        self.heightMinimum = self.macroPanel.addWidget(mhapi.ui.createSlider(label="Minimum height", value=0.2))
        self.heightMaximum = self.macroPanel.addWidget(mhapi.ui.createSlider(label="Maximum height", value=0.9))

        self.macroPanel.addWidget(mhapi.ui.createLabel())

        self.randomizeMuscle = self.macroPanel.addWidget(mhapi.ui.createCheckBox(label="Randomize muscle", selected=True))
        self.muscleMinimum = self.macroPanel.addWidget(mhapi.ui.createSlider(label="Minimum muscle", value=0.3))
        self.muscleMaximum = self.macroPanel.addWidget(mhapi.ui.createSlider(label="Maximum muscle", value=0.8))

        self.macroPanel.addWidget(mhapi.ui.createLabel())

        self.gender = self.macroPanel.addWidget(mhapi.ui.createCheckBox(label="Randomize gender", selected=True))
        self.genderabsolute = self.macroPanel.addWidget(mhapi.ui.createCheckBox(label="Absolute gender", selected=True))

        self.macroPanel.addWidget(mhapi.ui.createLabel())

        self.ethnicity = self.macroPanel.addWidget(mhapi.ui.createCheckBox(label="Randomize ethnicity", selected=True))
        self.ethnicityabsolute = self.macroPanel.addWidget(mhapi.ui.createCheckBox(label="Absolute ethnicity", selected=True))

        return self.macroPanel

    def _generateSettingsHash(self):
        settings = dict()

        # Macro
        macro = dict()

        macro["randomizeAge"] = self.randomizeAge.selected
        macro["ageMinimum"] = self.ageMinimum.getValue()
        macro["ageMaximum"] = self.ageMaximum.getValue()

        macro["randomizeWeight"] = self.randomizeWeight.selected
        macro["weightMinimum"] = self.weightMinimum.getValue()
        macro["weightMaximum"] = self.weightMaximum.getValue()

        macro["randomizeHeight"] = self.randomizeHeight.selected
        macro["heightMinimum"] = self.heightMinimum.getValue()
        macro["heightMaximum"] = self.heightMaximum.getValue()

        macro["randomizeMuscle"] = self.randomizeMuscle.selected
        macro["muscleMinimum"] = self.muscleMinimum.getValue()
        macro["muscleMaximum"] = self.muscleMaximum.getValue()

        macro["gender"] = self.gender.selected
        macro["genderabsolute"] = self.genderabsolute.selected
        macro["ethnicity"] = self.ethnicity.selected
        macro["ethnicityabsolute"] = self.ethnicityabsolute.selected

        settings["macro"] = macro

        # Modeling

        modeling = dict()

        modeling["head"] = self.head.selected
        modeling["face"] = self.face.selected
        modeling["torso"] = self.torso.selected
        modeling["stomach"] = self.stomach.selected
        modeling["buttocks"] = self.buttocks.selected
        modeling["pelvis"] = self.pelvis.selected
        modeling["arms"] = self.arms.selected
        modeling["hands"] = self.hands.selected
        modeling["legs"] = self.legs.selected
        modeling["feet"] = self.feet.selected

        modeling["maxdev"] = self.maxdev.getValue()
        modeling["symmetry"] = self.symmetry.getValue()

        settings["modeling"] = modeling

        # Output

        output = dict()

        num = 1
        try:
            num = int(self.numfiles.text)
        except:
            pass

        output["numfiles"] = num
        output["fnbase"] = self.fnbase.text
        output["format"] = str(self.fileformat.getCurrentItem())

        settings["output"] = output

        # Skins

        femaleSkins = dict()

        for name in self.allowedFemaleSkins.keys():
            skinUI = self.allowedFemaleSkins[name]
            skinSettings = dict()
            skinSettings["fullPath"] = skinUI["fullPath"]
            skinSettings["mixed"] = skinUI["mixed"].selected
            skinSettings["african"] = skinUI["african"].selected
            skinSettings["asian"] = skinUI["asian"].selected
            skinSettings["caucasian"] = skinUI["caucasian"].selected
            femaleSkins[name] = skinSettings

        maleSkins = dict()

        for name in self.allowedMaleSkins.keys():
            skinUI = self.allowedMaleSkins[name]
            skinSettings = dict()
            skinSettings["fullPath"] = skinUI["fullPath"]
            skinSettings["mixed"] = skinUI["mixed"].selected
            skinSettings["african"] = skinUI["african"].selected
            skinSettings["asian"] = skinUI["asian"].selected
            skinSettings["caucasian"] = skinUI["caucasian"].selected
            maleSkins[name] = skinSettings

        settings["materials"] = dict()
        settings["materials"]["femaleSkins"] = femaleSkins
        settings["materials"]["maleSkins"] = maleSkins

        return settings

    def _onProduceClick(self):
        print("Produce")

        settings = self._generateSettingsHash()

        pp.pprint(settings)

        self.initialState = HumanState()

        i = settings["output"]["numfiles"]
        base = settings["output"]["fnbase"]

        while i > 0:
            self.nextState = HumanState(settings)
            self.nextState.applyState(False)
            format = settings["output"]["format"]
            name = base + str(i).rjust(4,"0")

            if format == "MHM":
                path = mhapi.locations.getUserHomePath("models")
                name = name + ".mhm"
                self.human.save(os.path.join(path,name))
            else:
                path = mhapi.locations.getUserHomePath("exports")

            i = i - 1
            self.initialState.applyState(True)
            self.human.applyAllTargets()
