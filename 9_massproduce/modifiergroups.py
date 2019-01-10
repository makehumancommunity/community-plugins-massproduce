#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

MACROGROUPS = dict()
MACROGROUPS["age"] = ["macrodetails/Age"]
MACROGROUPS["height"] = ["macrodetails-height/Height"]
MACROGROUPS["weight"] = ["macrodetails-universal/Weight"]
MACROGROUPS["muscle"] = ["macrodetails-universal/Muscle"]
MACROGROUPS["gender"] = ["macrodetails/Gender"]
MACROGROUPS["proportion"] = ["macrodetails-proportions/BodyProportions"]
MACROGROUPS["ethnicity"] = ["macrodetails/African", "macrodetails/Asian", "macrodetails/Caucasian"]

'''
    head
 -- UniversalModifier head/head-age-decr|incr
 -- UniversalModifier head/head-angle-in|out
 -- UniversalModifier head/head-fat-decr|incr
 -- UniversalModifier head/head-oval
 -- UniversalModifier head/head-round
 -- UniversalModifier head/head-rectangular
 -- UniversalModifier head/head-square
 -- UniversalModifier head/head-triangular
 -- UniversalModifier head/head-invertedtriangular
 -- UniversalModifier head/head-diamond
 -- UniversalModifier head/head-scale-depth-decr|incr
 -- UniversalModifier head/head-scale-horiz-decr|incr
 -- UniversalModifier head/head-scale-vert-decr|incr
 -- UniversalModifier head/head-trans-in|out
 -- UniversalModifier head/head-trans-down|up
 -- UniversalModifier head/head-trans-backward|forward
 -- UniversalModifier head/head-back-scale-depth-decr|incr
forehead
 -- UniversalModifier forehead/forehead-trans-backward|forward
 -- UniversalModifier forehead/forehead-scale-vert-decr|incr
 -- UniversalModifier forehead/forehead-nubian-decr|incr
 -- UniversalModifier forehead/forehead-temple-decr|incr
eyebrows
 -- UniversalModifier eyebrows/eyebrows-trans-backward|forward
 -- UniversalModifier eyebrows/eyebrows-angle-down|up
 -- UniversalModifier eyebrows/eyebrows-trans-down|up
neck
 -- UniversalModifier neck/neck-double-decr|incr
 -- UniversalModifier neck/neck-scale-depth-decr|incr
 -- UniversalModifier neck/neck-scale-horiz-decr|incr
 -- UniversalModifier neck/neck-scale-vert-decr|incr
 -- UniversalModifier neck/neck-trans-in|out
 -- UniversalModifier neck/neck-trans-down|up
 -- UniversalModifier neck/neck-trans-backward|forward
 -- UniversalModifier neck/neck-back-scale-depth-decr|incr
eyes
 -- UniversalModifier eyes/r-eye-bag-decr|incr
 -- UniversalModifier eyes/r-eye-bag-in|out
 -- UniversalModifier eyes/r-eye-bag-height-decr|incr
 -- UniversalModifier eyes/r-eye-eyefold-angle-down|up
 -- UniversalModifier eyes/r-eye-epicanthus-in|out
 -- UniversalModifier eyes/r-eye-eyefold-concave|convex
 -- UniversalModifier eyes/r-eye-eyefold-down|up
 -- UniversalModifier eyes/r-eye-height1-decr|incr
 -- UniversalModifier eyes/r-eye-height2-decr|incr
 -- UniversalModifier eyes/r-eye-height3-decr|incr
 -- UniversalModifier eyes/r-eye-push1-in|out
 -- UniversalModifier eyes/r-eye-push2-in|out
 -- UniversalModifier eyes/r-eye-trans-in|out
 -- UniversalModifier eyes/r-eye-trans-down|up
 -- UniversalModifier eyes/r-eye-scale-decr|incr
 -- UniversalModifier eyes/r-eye-corner1-down|up
 -- UniversalModifier eyes/r-eye-corner2-down|up
 -- UniversalModifier eyes/l-eye-bag-decr|incr
 -- UniversalModifier eyes/l-eye-bag-in|out
 -- UniversalModifier eyes/l-eye-bag-height-decr|incr
 -- UniversalModifier eyes/l-eye-eyefold-angle-down|up
 -- UniversalModifier eyes/l-eye-epicanthus-in|out
 -- UniversalModifier eyes/l-eye-eyefold-concave|convex
 -- UniversalModifier eyes/l-eye-eyefold-down|up
 -- UniversalModifier eyes/l-eye-height1-decr|incr
 -- UniversalModifier eyes/l-eye-height2-decr|incr
 -- UniversalModifier eyes/l-eye-height3-decr|incr
 -- UniversalModifier eyes/l-eye-push1-in|out
 -- UniversalModifier eyes/l-eye-push2-in|out
 -- UniversalModifier eyes/l-eye-trans-in|out
 -- UniversalModifier eyes/l-eye-trans-down|up
 -- UniversalModifier eyes/l-eye-scale-decr|incr
 -- UniversalModifier eyes/l-eye-corner1-down|up
 -- UniversalModifier eyes/l-eye-corner2-down|up
nose
 -- UniversalModifier nose/nose-trans-down|up
 -- UniversalModifier nose/nose-trans-backward|forward
 -- UniversalModifier nose/nose-trans-in|out
 -- UniversalModifier nose/nose-scale-vert-decr|incr
 -- UniversalModifier nose/nose-scale-horiz-decr|incr
 -- UniversalModifier nose/nose-scale-depth-decr|incr
 -- UniversalModifier nose/nose-nostrils-width-decr|incr
 -- UniversalModifier nose/nose-point-width-decr|incr
 -- UniversalModifier nose/nose-base-down|up
 -- UniversalModifier nose/nose-width1-decr|incr
 -- UniversalModifier nose/nose-width2-decr|incr
 -- UniversalModifier nose/nose-width3-decr|incr
 -- UniversalModifier nose/nose-compression-compress|uncompress
 -- UniversalModifier nose/nose-curve-concave|convex
 -- UniversalModifier nose/nose-greek-decr|incr
 -- UniversalModifier nose/nose-hump-decr|incr
 -- UniversalModifier nose/nose-volume-decr|incr
 -- UniversalModifier nose/nose-nostrils-angle-down|up
 -- UniversalModifier nose/nose-point-down|up
 -- UniversalModifier nose/nose-septumangle-decr|incr
 -- UniversalModifier nose/nose-flaring-decr|incr
mouth
 -- UniversalModifier mouth/mouth-scale-horiz-decr|incr
 -- UniversalModifier mouth/mouth-scale-vert-decr|incr
 -- UniversalModifier mouth/mouth-scale-depth-decr|incr
 -- UniversalModifier mouth/mouth-trans-in|out
 -- UniversalModifier mouth/mouth-trans-down|up
 -- UniversalModifier mouth/mouth-trans-backward|forward
 -- UniversalModifier mouth/mouth-lowerlip-height-decr|incr
 -- UniversalModifier mouth/mouth-lowerlip-width-decr|incr
 -- UniversalModifier mouth/mouth-upperlip-height-decr|incr
 -- UniversalModifier mouth/mouth-upperlip-width-decr|incr
 -- UniversalModifier mouth/mouth-cupidsbow-width-decr|incr
 -- UniversalModifier mouth/mouth-dimples-in|out
 -- UniversalModifier mouth/mouth-laugh-lines-in|out
 -- UniversalModifier mouth/mouth-lowerlip-ext-down|up
 -- UniversalModifier mouth/mouth-angles-down|up
 -- UniversalModifier mouth/mouth-lowerlip-middle-down|up
 -- UniversalModifier mouth/mouth-lowerlip-volume-decr|incr
 -- UniversalModifier mouth/mouth-philtrum-volume-decr|incr
 -- UniversalModifier mouth/mouth-upperlip-volume-decr|incr
 -- UniversalModifier mouth/mouth-upperlip-ext-down|up
 -- UniversalModifier mouth/mouth-upperlip-middle-down|up
 -- UniversalModifier mouth/mouth-cupidsbow-decr|incr
ears
 -- UniversalModifier ears/r-ear-trans-backward|forward
 -- UniversalModifier ears/r-ear-scale-decr|incr
 -- UniversalModifier ears/r-ear-trans-down|up
 -- UniversalModifier ears/r-ear-scale-vert-decr|incr
 -- UniversalModifier ears/r-ear-lobe-decr|incr
 -- UniversalModifier ears/r-ear-shape-pointed|triangle
 -- UniversalModifier ears/r-ear-rot-backward|forward
 -- UniversalModifier ears/r-ear-shape-square|round
 -- UniversalModifier ears/r-ear-scale-depth-decr|incr
 -- UniversalModifier ears/r-ear-wing-decr|incr
 -- UniversalModifier ears/r-ear-flap-decr|incr
 -- UniversalModifier ears/l-ear-trans-backward|forward
 -- UniversalModifier ears/l-ear-scale-decr|incr
 -- UniversalModifier ears/l-ear-trans-down|up
 -- UniversalModifier ears/l-ear-scale-vert-decr|incr
 -- UniversalModifier ears/l-ear-lobe-decr|incr
 -- UniversalModifier ears/l-ear-shape-pointed|triangle
 -- UniversalModifier ears/l-ear-rot-backward|forward
 -- UniversalModifier ears/l-ear-shape-square|round
 -- UniversalModifier ears/l-ear-scale-depth-decr|incr
 -- UniversalModifier ears/l-ear-wing-decr|incr
 -- UniversalModifier ears/l-ear-flap-decr|incr
chin
 -- UniversalModifier chin/chin-jaw-drop-decr|incr
 -- UniversalModifier chin/chin-cleft-decr|incr
 -- UniversalModifier chin/chin-prominent-decr|incr
 -- UniversalModifier chin/chin-width-decr|incr
 -- UniversalModifier chin/chin-height-decr|incr
 -- UniversalModifier chin/chin-bones-decr|incr
 -- UniversalModifier chin/chin-prognathism-decr|incr
cheek
 -- UniversalModifier cheek/l-cheek-volume-decr|incr
 -- UniversalModifier cheek/l-cheek-bones-decr|incr
 -- UniversalModifier cheek/l-cheek-inner-decr|incr
 -- UniversalModifier cheek/l-cheek-trans-down|up
 -- UniversalModifier cheek/r-cheek-volume-decr|incr
 -- UniversalModifier cheek/r-cheek-bones-decr|incr
 -- UniversalModifier cheek/r-cheek-inner-decr|incr
 -- UniversalModifier cheek/r-cheek-trans-down|up
torso
 -- UniversalModifier torso/torso-scale-depth-decr|incr
 -- UniversalModifier torso/torso-scale-horiz-decr|incr
 -- UniversalModifier torso/torso-scale-vert-decr|incr
 -- UniversalModifier torso/torso-trans-in|out
 -- UniversalModifier torso/torso-trans-down|up
 -- UniversalModifier torso/torso-trans-backward|forward
 -- UniversalModifier torso/torso-vshape-decr|incr
 -- UniversalModifier torso/torso-muscle-dorsi-decr|incr
 -- UniversalModifier torso/torso-muscle-pectoral-decr|incr
hip
 -- UniversalModifier hip/hip-scale-depth-decr|incr
 -- UniversalModifier hip/hip-scale-horiz-decr|incr
 -- UniversalModifier hip/hip-scale-vert-decr|incr
 -- UniversalModifier hip/hip-trans-in|out
 -- UniversalModifier hip/hip-trans-down|up
 -- UniversalModifier hip/hip-trans-backward|forward
 -- UniversalModifier hip/hip-waist-down|up
stomach
 -- UniversalModifier stomach/stomach-navel-in|out
 -- UniversalModifier stomach/stomach-tone-decr|incr
 -- UniversalModifier stomach/stomach-pregnant-decr|incr
 -- UniversalModifier stomach/stomach-navel-down|up
buttocks
 -- UniversalModifier buttocks/buttocks-volume-decr|incr
pelvis
 -- UniversalModifier pelvis/pelvis-tone-decr|incr
 -- UniversalModifier pelvis/bulge-decr|incr
armslegs
 -- UniversalModifier armslegs/r-hand-fingers-distance-decr|incr
 -- UniversalModifier armslegs/r-hand-fingers-diameter-decr|incr
 -- UniversalModifier armslegs/r-hand-fingers-length-decr|incr
 -- UniversalModifier armslegs/r-hand-scale-decr|incr
 -- UniversalModifier armslegs/r-hand-trans-in|out
 -- UniversalModifier armslegs/l-hand-fingers-distance-decr|incr
 -- UniversalModifier armslegs/l-hand-fingers-diameter-decr|incr
 -- UniversalModifier armslegs/l-hand-fingers-length-decr|incr
 -- UniversalModifier armslegs/l-hand-scale-decr|incr
 -- UniversalModifier armslegs/l-hand-trans-in|out
 -- UniversalModifier armslegs/r-foot-scale-decr|incr
 -- UniversalModifier armslegs/r-foot-trans-in|out
 -- UniversalModifier armslegs/r-foot-trans-backward|forward
 -- UniversalModifier armslegs/l-foot-scale-decr|incr
 -- UniversalModifier armslegs/l-foot-trans-in|out
 -- UniversalModifier armslegs/l-foot-trans-backward|forward
 -- UniversalModifier armslegs/r-lowerarm-scale-depth-decr|incr
 -- UniversalModifier armslegs/r-lowerarm-scale-horiz-decr|incr
 -- UniversalModifier armslegs/r-lowerarm-scale-vert-decr|incr
 -- UniversalModifier armslegs/r-lowerarm-fat-decr|incr
 -- UniversalModifier armslegs/r-lowerarm-muscle-decr|incr
 -- UniversalModifier armslegs/r-upperarm-scale-depth-decr|incr
 -- UniversalModifier armslegs/r-upperarm-scale-horiz-decr|incr
 -- UniversalModifier armslegs/r-upperarm-scale-vert-decr|incr
 -- UniversalModifier armslegs/r-upperarm-fat-decr|incr
 -- UniversalModifier armslegs/r-upperarm-shoulder-muscle-decr|incr
 -- UniversalModifier armslegs/r-upperarm-muscle-decr|incr
 -- UniversalModifier armslegs/l-lowerarm-scale-depth-decr|incr
 -- UniversalModifier armslegs/l-lowerarm-scale-horiz-decr|incr
 -- UniversalModifier armslegs/l-lowerarm-scale-vert-decr|incr
 -- UniversalModifier armslegs/l-lowerarm-fat-decr|incr
 -- UniversalModifier armslegs/l-lowerarm-muscle-decr|incr
 -- UniversalModifier armslegs/l-upperarm-scale-depth-decr|incr
 -- UniversalModifier armslegs/l-upperarm-scale-horiz-decr|incr
 -- UniversalModifier armslegs/l-upperarm-scale-vert-decr|incr
 -- UniversalModifier armslegs/l-upperarm-fat-decr|incr
 -- UniversalModifier armslegs/l-upperarm-shoulder-muscle-decr|incr
 -- UniversalModifier armslegs/l-upperarm-muscle-decr|incr
 -- UniversalModifier armslegs/r-leg-valgus-decr|incr
 -- UniversalModifier armslegs/r-lowerleg-scale-depth-decr|incr
 -- UniversalModifier armslegs/r-lowerleg-scale-horiz-decr|incr
 -- UniversalModifier armslegs/r-lowerleg-fat-decr|incr
 -- UniversalModifier armslegs/r-lowerleg-muscle-decr|incr
 -- UniversalModifier armslegs/r-upperleg-scale-depth-decr|incr
 -- UniversalModifier armslegs/r-upperleg-scale-horiz-decr|incr
 -- UniversalModifier armslegs/r-upperleg-scale-vert-decr|incr
 -- UniversalModifier armslegs/r-upperleg-fat-decr|incr
 -- UniversalModifier armslegs/r-upperleg-muscle-decr|incr
 -- UniversalModifier armslegs/l-leg-valgus-decr|incr
 -- UniversalModifier armslegs/l-lowerleg-scale-depth-decr|incr
 -- UniversalModifier armslegs/l-lowerleg-scale-horiz-decr|incr
 -- UniversalModifier armslegs/l-lowerleg-fat-decr|incr
 -- UniversalModifier armslegs/l-lowerleg-muscle-decr|incr
 -- UniversalModifier armslegs/l-upperleg-scale-depth-decr|incr
 -- UniversalModifier armslegs/l-upperleg-scale-horiz-decr|incr
 -- UniversalModifier armslegs/l-upperleg-scale-vert-decr|incr
 -- UniversalModifier armslegs/l-upperleg-fat-decr|incr
 -- UniversalModifier armslegs/l-upperleg-muscle-decr|incr
 -- UniversalModifier armslegs/lowerlegs-height-decr|incr
 -- UniversalModifier armslegs/upperlegs-height-decr|incr
breast
 -- MacroModifier breast/BreastSize
 -- MacroModifier breast/BreastFirmness
 -- UniversalModifier breast/breast-trans-down|up
 -- UniversalModifier breast/breast-dist-decr|incr
 -- UniversalModifier breast/breast-point-decr|incr
 -- UniversalModifier breast/breast-volume-vert-down|up
 -- UniversalModifier breast/nipple-size-decr|incr
 -- UniversalModifier breast/nipple-point-decr|incr
genitals
 -- UniversalModifier genitals/penis-length-decr|incr
 -- UniversalModifier genitals/penis-circ-decr|incr
 -- UniversalModifier genitals/penis-testicles-decr|incr
macrodetails
 -- MacroModifier macrodetails/Gender
 -- MacroModifier macrodetails/Age
 -- EthnicModifier macrodetails/African
 -- EthnicModifier macrodetails/Asian
 -- EthnicModifier macrodetails/Caucasian
macrodetails-universal
 -- MacroModifier macrodetails-universal/Muscle
 -- MacroModifier macrodetails-universal/Weight
macrodetails-height
 -- MacroModifier macrodetails-height/Height
macrodetails-proportions
 -- MacroModifier macrodetails-proportions/BodyProportions
measure
 -- UniversalModifier measure/measure-neck-circ-decr|incr
 -- UniversalModifier measure/measure-neck-height-decr|incr
 -- UniversalModifier measure/measure-upperarm-circ-decr|incr
 -- UniversalModifier measure/measure-upperarm-length-decr|incr
 -- UniversalModifier measure/measure-lowerarm-length-decr|incr
 -- UniversalModifier measure/measure-wrist-circ-decr|incr
 -- UniversalModifier measure/measure-frontchest-dist-decr|incr
 -- UniversalModifier measure/measure-bust-circ-decr|incr
 -- UniversalModifier measure/measure-underbust-circ-decr|incr
 -- UniversalModifier measure/measure-waist-circ-decr|incr
 -- UniversalModifier measure/measure-napetowaist-dist-decr|incr
 -- UniversalModifier measure/measure-waisttohip-dist-decr|incr
 -- UniversalModifier measure/measure-shoulder-dist-decr|incr
 -- UniversalModifier measure/measure-hips-circ-decr|incr
 -- UniversalModifier measure/measure-upperleg-height-decr|incr
 -- UniversalModifier measure/measure-thigh-circ-decr|incr
 -- UniversalModifier measure/measure-lowerleg-height-decr|incr
 -- UniversalModifier measure/measure-calf-circ-decr|incr
 -- UniversalModifier measure/measure-knee-circ-decr|incr
 -- UniversalModifier measure/measure-ankle-circ-decr|incr

'''