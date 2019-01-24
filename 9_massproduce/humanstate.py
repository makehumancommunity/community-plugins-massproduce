#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import gui3d
import gui
from core import G

import material

from .randomizeaction import RandomizeAction
from .modifiergroups import MACROGROUPS

mhapi = gui3d.app.mhapi

from PyQt5.QtWidgets import *

import pprint
pp = pprint.PrettyPrinter(indent=4)

class HumanState():

    def __init__(self, settings = None):

        self.settings = settings
        self.human = G.app.selectedHuman
        self.macroModifierValues = dict()
        self.appliedTargets = dict(self.human.targetsDetailStack)

        print("\nSKIN\n")

        self.skin = material.Material().copyFrom(self.human.material)
        print(self.skin)

        self._fillMacroModifierValues()

        if not settings is None:
            self._randomizeMacros()
            if settings.getValue("materials", "randomizeSkinMaterials"):
                self._randomizeSkin()

        print("MACRO:\n")
        pp.pprint(self.macroModifierValues)

        print("\nTARGET:\n")
        pp.pprint(self.appliedTargets)

    def _fillMacroModifierValues(self):
        for group in MACROGROUPS.keys():
            for n in MACROGROUPS[group]:
                mod = self.human.getModifier(n)
                v = mod.getValue()
                self.macroModifierValues[n] = v

    def _randomizeOneSidedMaxMin(self, valuesHash, modifierList, maximumValue, minimumValue):

        max = maximumValue
        min = minimumValue

        if(min > max):
            min = maximumValue
            max = minimumValue

        avg = (max - min) / 2.0

        for name in modifierList:
            val = self.getRandomValue(min, max)
            valuesHash[name] = val

    def _pickOne(self, valuesHash, modifierList):
        for n in modifierList:
            valuesHash[n] = 0.0
        num = len(modifierList)
        pickedVal = random.randrange(num)
        pickedName = modifierList[pickedVal]
        valuesHash[pickedName] = 1.0

    def _dichotomous(self, valuesHash, modifierList):
        for n in modifierList:
            valuesHash[n] = float(random.randrange(2))

    def _randomizeMacros(self):

        if self.settings.getValue("macro","randomizeAge"):
            min = self.settings.getValue("macro", "ageMinimum")
            max = self.settings.getValue("macro", "ageMaximum")
            self._randomizeOneSidedMaxMin(self.macroModifierValues, MACROGROUPS["age"], min, max)

        if self.settings.getValue("macro", "randomizeWeight"):
            min = self.settings.getValue("macro", "weightMinimum")
            max = self.settings.getValue("macro", "weightMaximum")
            self._randomizeOneSidedMaxMin(self.macroModifierValues, MACROGROUPS["weight"], min, max)

        if self.settings.getValue("macro", "randomizeHeight"):
            min = self.settings.getValue("macro", "heightMinimum")
            max = self.settings.getValue("macro", "heightMaximum")
            self._randomizeOneSidedMaxMin(self.macroModifierValues, MACROGROUPS["height"], min, max)

        if self.settings.getValue("macro", "randomizeMuscle"):
            min = self.settings.getValue("macro", "muscleMinimum")
            max = self.settings.getValue("macro", "muscleMaximum")
            self._randomizeOneSidedMaxMin(self.macroModifierValues, MACROGROUPS["muscle"], min, max)

        if self.settings.getValue("macro", "ethnicity"):
            if self.settings.getValue("macro", "ethnicityabsolute"):
                self._pickOne(self.macroModifierValues, MACROGROUPS["ethnicity"])
            else:
                self._randomizeOneSidedMaxMin(self.macroModifierValues, MACROGROUPS["ethnicity"], 0.0, 1.0)

        if self.settings.getValue("macro", "gender"):
            if self.settings.getValue("macro", "genderabsolute"):
                self._dichotomous(self.macroModifierValues, MACROGROUPS["gender"])
            else:
                self._randomizeOneSidedMaxMin(self.macroModifierValues, MACROGROUPS["gender"], 0.0, 1.0)

    def _getCurrentEthnicity(self):
        for ethn in MACROGROUPS["ethnicity"]:
            value = self.macroModifierValues[ethn]
            name = ethn.split("/")[1].lower()
            if value > 0.9:
                return name
        return "mixed"

    def _getCurrentGender(self):
        key = MACROGROUPS["gender"][0]
        value = self.macroModifierValues[key]
        gender = "mixed"

        if value < 0.3:
            gender = "female"
        if value > 0.7:
            gender = "male"

        return gender

    def _findSkinForEthnicityAndGender(self,ethnicity,gender):

        skinHash = None
        if gender == "female":
            category = "allowedFemaleSkins"
        else:
            category = "allowedMaleSkins"

        print(ethnicity)

        matchingSkins = []
        for name in self.settings.getNames(category):
            skin = self.settings.getValueHash(category, name)
            print(skin)
            if skin[ethnicity]:
                matchingSkins.append(skin["fullPath"])
        print("\nGENDER IS: " + gender)
        pp.pprint(matchingSkins)

        pick = random.randrange(len(matchingSkins))
        self.skin = material.fromFile(matchingSkins[pick])

    def _randomizeSkin(self):

        gender = self._getCurrentGender()
        ethnicity = self._getCurrentEthnicity()

        self._findSkinForEthnicityAndGender(ethnicity,gender)

    def applyState(self, assumeBodyReset=False):

        self._applyMacroModifiers()
        if assumeBodyReset:
            self.human.targetsDetailStack = self.appliedTargets
        self.human.material = self.skin

        mhapi.modifiers._threadSafeApplyAllTargets()

    def _applyMacroModifiers(self):
        for group in MACROGROUPS.keys():
            for n in MACROGROUPS[group]:
                mod = self.human.getModifier(n)
                v = self.macroModifierValues[n]
                mod.setValue(v)

    def getRandomValue(self, minValue, maxValue):
        size = maxValue - minValue
        val = random.random() * size
        return minValue + val

    def getNormalRandomValue(self, minValue, maxValue, middleValue, sigmaFactor=0.2):
        rangeWidth = float(abs(maxValue - minValue))
        sigma = sigmaFactor * rangeWidth
        randomVal = random.gauss(middleValue, sigma)
        if randomVal < minValue:
            randomVal = minValue + abs(randomVal - minValue)
        elif randomVal > maxValue:
            randomVal = maxValue - abs(randomVal - maxValue)
        return max(minValue, min(randomVal, maxValue))


